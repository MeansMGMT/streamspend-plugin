# StreamSpend for Claude

StreamSpend by MeansMGMT helps independent artists, labels and music marketers decide where ad money goes. This plugin connects Claude to the StreamSpend app and adds two skills that show Claude how to use it well.

You can check how a music ad campaign did, for free and with no account. Share Meta, TikTok, YouTube or Google ad results for a song as a screenshot, an export or typed numbers. StreamSpend compares the price per result with ranges from past MeansMGMT campaigns. The card shows streams before, during and after the ads, streams per click, saves and one next step.

With a free StreamSpend account, you can also ask which of an artist's songs to put money behind next. StreamSpend scores the whole Spotify catalog and shows top picks, sleepers and songs to skip, each with a campaign type, a country tier and one plain reason.

## Install

In Claude Code:

```
/plugin marketplace add MeansMGMT/streamspend-plugin
/plugin install streamspend@streamspend
```

In Claude on the web or desktop, add StreamSpend from the directory once it is listed. You can also add a custom connector with this address: `https://mcp.streamspend.net/mcp`. The connector gives you the tools. The plugin adds the skills.

## Try it

- "How did this campaign do?" with an Ads Manager screenshot or export.
- "Check my campaign" to get a setup card for your Ads Manager and Spotify for Artists exports.
- "Which Northline songs should I put money behind next?"
- "How many StreamSpend plans do I have left?"

## Tools

| Tool | Sign-in | What it does |
| --- | --- | --- |
| `start_campaign_check` | No | Shows a setup card for an Ads Manager export and a Spotify for Artists song export. |
| `analyze_campaign` | No | Runs the check and shows the result card. |
| `inspect_campaign_csv` | No | Reads export text into campaign or listening rows. |
| `plan_next_push` | Free account | Starts a StreamSpend plan for an artist and shows its card. Uses one of your weekly plans. |
| `get_plan_status` | Free account | Checks a plan. The card calls it while the plan runs. |
| `my_streamspend` | Free account | Shows plans used and left this week and your recent reports. |

Free StreamSpend accounts get 4 plans per rolling 7 days. StreamSpend needs artists with at least 2 tracks and 1,000 monthly listeners on Spotify.

## Skills

`campaign-check` tells Claude where to find the numbers and how to keep the check honest. Claude reads what you shared first. If a Meta Ads, Google Ads, TikTok Ads or Spotify for Artists app is already connected in Claude, it may read missing numbers from it. It reads only and tells you what it pulled. Otherwise it shows the setup card.

`next-push` tells Claude how to start a plan, when sign-in comes up and how to talk about the picks without overstating them.

Both skills keep the same rules. Unknown numbers stay unknown and are never counted as zero. Countries and result types are never guessed from campaign names. Feature.fm clicks count clicks to every streaming service, not only Spotify. The checks describe what happened alongside the ads and never claim the ads caused it. Plan scores rank songs within one catalog and are not promised streams.

## Data and privacy

Every tool call goes to `mcp.streamspend.net`, the StreamSpend MCP server run by MeansMGMT.

The campaign check tools read only. Claude sends only the numbers the check needs. That means campaign names, spend, currency, result counts and what they counted, dates, platform and countries. It also sends the genre, the song title and daily Spotify streams and saves if you share them. Export files you drop into the card are read inside the card, and only those numbers are sent. The server keeps nothing after it answers and never adds your numbers to its benchmarks.

The plan tools need a free StreamSpend sign-in. You sign in on StreamSpend's own page, which uses StreamSpend's account system (Supabase), so the server never sees your password. Claude then sends your StreamSpend sign-in token with each plan request. The server checks the token and forwards it to `www.streamspend.net` with the artist name or link, an optional genre and market, or the plan ID. StreamSpend runs the plan with Spotify and other music data sources and saves the report to your account. A connector sign-in can only run plans and read your reports and plan count. It cannot change your account or settings.

Neither the plugin nor the server can reach your ad accounts or Spotify for Artists. When Claude reads an app you already connected, it does so through your own connection in Claude, and it never changes a campaign.

To limit abuse, the server counts requests per network address, and plan requests per StreamSpend account, in memory for up to one minute. Railway, which hosts the server, may keep basic request records such as the time, network address and status code.

Read the full policies: [StreamSpend MCP privacy](https://mcp.streamspend.net/privacy) and [StreamSpend privacy](https://www.streamspend.net/privacy).

## Support

Questions or problems: contact@meansmgmt.com. More about StreamSpend at [streamspend.net](https://www.streamspend.net) and about MeansMGMT at [meansmgmt.com](https://www.meansmgmt.com).

## License

MIT. See [LICENSE](LICENSE).
