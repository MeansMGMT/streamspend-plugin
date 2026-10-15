"""Checks the plugin before merge: JSON manifests parse, required fields exist, every skill has name and description frontmatter."""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

def load(path):
    try:
        return json.loads((root / path).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"{path}: {e}")
        return {}

plugin = load(".claude-plugin/plugin.json")
market = load(".claude-plugin/marketplace.json")
mcp = load(".mcp.json")
for key in ("name", "description", "version"):
    if not plugin.get(key):
        errors.append(f"plugin.json: missing {key}")
if not any(p.get("name") == plugin.get("name") for p in market.get("plugins", [])):
    errors.append("marketplace.json: does not list the plugin by name")
for name, server in mcp.get("mcpServers", {}).items():
    if not str(server.get("url", "")).startswith("https://"):
        errors.append(f".mcp.json: server {name} needs an https url")
icon = plugin.get("icon")
if icon and not (root / icon).is_file():
    errors.append(f"plugin.json: icon {icon} not found")

skills = sorted((root / "skills").glob("*/SKILL.md"))
if not skills:
    errors.append("no skills/*/SKILL.md found")
for s in skills:
    text = s.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{s.relative_to(root)}: missing frontmatter")
        continue
    front = m.group(1)
    for key in ("name", "description"):
        if not re.search(rf"^{key}:\s*\S", front, re.M):
            errors.append(f"{s.relative_to(root)}: frontmatter missing {key}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: plugin {plugin.get('name')} {plugin.get('version')}, {len(skills)} skills")
