---
name: campaign-check
description: Check how a music ad campaign did against StreamSpend benchmark ranges from past MeansMGMT campaigns. Use when someone shares Meta, TikTok, YouTube or Google ad results for a song as a screenshot, an export or typed numbers. Also use when they ask whether a campaign's costs or results were good, or want a check but have not shared numbers yet.
---

# Campaign check

StreamSpend compares a music ad campaign with benchmark ranges from past MeansMGMT campaigns. You cannot know those ranges any other way, so run the check before writing your own analysis. It is free, needs no sign-in, keeps no history and never changes a campaign.

## Where the numbers come from

Use the first source that applies, and fill gaps from the next ones.

1. The user shared numbers. Read every fact you can see in the screenshot, export or message. For an Ads Manager export, pass its text to `inspect_campaign_csv` with `kind` set to `meta` and use the rows it returns. For a Spotify for Artists song export, use `kind` `spotify` and pass the same `trackId` you will give `analyze_campaign`. That tool reads only those two kinds of export. Read TikTok, YouTube and Google exports yourself.
2. Connected apps. If a Meta Ads, Google Ads, TikTok Ads or Spotify for Artists connector is already connected in this chat, pull the facts the user did not share from it. Read only. Never change a campaign, budget, audience or setting, even when the connector allows it. Tell the user in one short line what you pulled and from which account.
3. Nothing to read. Call `start_campaign_check`. It shows a setup card where the user drops an Ads Manager export and a Spotify for Artists song export and picks the genre. Pass `title` or `genre` only if the user said them.

Never ask the user to connect an app just for the check. The setup card and a screenshot both work.

Never open a browser to read Spotify for Artists, Meta Ads Manager or another ad dashboard for the user, even when a browser tool is available. Those sites do not allow automated access. Ask for a screenshot or an export instead.

## Facts to collect

For each campaign:

- Name, platform (`meta`, `tiktok`, `youtube` or `google`), start and end dates, currency and spend.
- The result count and exactly what each result counted (`metric`), for example `FeatureFM_click` or `presave`. If a column only says "Results" with no type, leave `metric` null.
- What the ads were set to optimize for (`conversionGoal`), from the platform's result type or the ad set.
- Countries as two-letter ISO codes (GB for the UK) and the tier. Set `geography.confirmed` to true only when the countries come from a country breakdown, the ad set targeting or the user.
- Any other numbers you can see: impressions, link clicks, landing page views, follows, likes, shares, views, watch minutes.

For the song:

- Title and a short `trackId` you choose, used again in the Spotify rows.
- Daily Spotify for Artists rows (date, streams, and saves and listeners when shown), from about a week before the ads to about a week after. Each date counts once per song.
- The objective: `streaming`, `presave`, `playlist_growth`, `social_growth` or `monetization`. Use `other` or `unknown` when none of those fits or you cannot tell.
- Genre, only when the user's words clearly match one option. "Rock" alone could be Rock / Alt or Rock / Metal, and "rap" could be Rap / HipHop or Rap / Pop. Leave it null and the card asks.

## Call analyze_campaign

Call it as soon as you have spend and a result count, with `factsFrom` set:

| Where the facts came from | `factsFrom` |
| --- | --- |
| Ad platform screenshot | `screenshot` |
| Export file | `export` |
| Numbers the user typed | `typed` |
| Pulled from a connected ad platform or Spotify for Artists connector | `connector` |

Set `confirmedInputs` to true when spend and the result count were typed by the user, read directly from a screenshot or export, or pulled from a connected app. Set it to false when you estimated them or they were only partly visible.

Do not ask the user to confirm numbers you read directly. The card shows what you read, and the user corrects it in the chat.

## Rules that keep the check honest

- Unknown stays unknown. Leave any fact you cannot see null. Never use zero for a missing number and never invent a value.
- Never take countries or the result type from campaign names. A name like "T1 Streaming" proves nothing.
- Feature.fm clicks count clicks to every streaming service, not only Spotify.
- Describe what happened alongside the ads. Never say the ads caused streams, saves or followers.
- Ranges are the low and high of past campaigns, not promises. Streaming, pre-save, playlist and sales ranges come from Meta campaigns. TikTok and YouTube have ranges for social growth only. When no range fits, the card says so; do not fill the gap with your own figures.
- Send the check only the numbers it needs. Leave out account IDs, emails and anything personal.

## After the card

- Do not repeat the card's numbers in the chat. The card already shows them.
- If facts are missing, usually the countries or what a generic Results column counted, ask for only those in one short message.
- When the user corrects a fact or adds Spotify data, call `analyze_campaign` again with the fix.
- If no card appears, share the tool's text answer in plain words without adding numbers it did not give.
- If the user asks which song to push next, use the `next-push` skill.
