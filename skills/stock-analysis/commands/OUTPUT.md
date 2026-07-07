# `!commands` Output Contract

## Purpose

`OUTPUT.md` defines the user-facing display contract for `!commands`.

`!commands` is a menu-only command. It shows the registered MIDAS command menu and does not run research, perform lookup, write artifacts, classify, score, calculate metrics, or give recommendations.

## Authority

The command registry is the command index:

`docs/COMMAND_REGISTRY.md`

This file defines how the menu is displayed. It must not become a competing registry.

When command availability, status, aliases, artifact behavior, or paths change, update the registry first, then review this display contract for menu consistency.

## Trigger

Use this output contract when the user runs:

```md
!commands
```

Treat command case-insensitively.

Do not use `!help` as a trigger. `!help` is intentionally unsupported to avoid Telegram/global help conflicts.

## Behavior Scope

`!commands` must:

- show the default compact command menu;
- use registered command names and statuses from `docs/COMMAND_REGISTRY.md`;
- include `!market` because it is registered and built;
- display aliases where useful, including registered `!track` aliases;
- show whether commands write artifacts in plain English;
- stay Telegram-readable;
- avoid research execution;
- avoid recommendation language.

`!commands` must not:

- analyze a company;
- fetch filings, market data, earnings, disclosures, or news;
- run another MIDAS command;
- create, modify, or delete artifacts;
- modify the watchlist;
- classify a setup;
- score a company or candidate;
- calculate metrics;
- create scheduled jobs or alerts;
- provide Buy/Hold/Sell language;
- respond to `!help` as an alias.

## Unsupported Variants

Stage 1 is menu-only.

For now, unsupported variants such as:

```md
!commands risk
!commands market
!commands lookup risk
```

should not perform command lookup or personalized routing. Respond with the normal compact menu and, if needed, one short note:

```md
Lookup is not enabled yet; `!commands` currently shows the menu only.
```

Do not ask a follow-up question.

## Default Compact Command Menu

Return the menu in this grouping and order.

Use concise descriptions. Show status labels as `Active`, `Draft`, or `Planned`. Show artifact behavior as `writes artifacts`, `may write artifacts`, or `no artifacts`.

```md
# MIDAS Commands

## Core Research

`!research [ticker]` — Active — Business-model research. Writes artifacts.
Aliases: `/research`, `research`

`!financials [ticker]` — Active — Financial statement review. Writes artifacts.

`!thesis [ticker]` — Draft — Long-term thesis build or update. Writes artifacts.
Aliases: `/thesis`, `thesis`

`!risk [ticker]` — Draft — Filing-backed risk assessment. Writes artifacts.
Aliases: `/risk`, `risk`

Aliases: `/full`, `full analysis`

## Updates / Market

`!earnings [ticker]` — Active — Latest-quarter earnings review. Writes artifacts.
Aliases: `/earnings`, `earnings review`

`!updates [ticker]` — Active — Recent material updates. Writes artifacts.

`!market [ticker]` — Draft — Read-only market-data snapshot. No artifacts.

## Discovery / Tracking

`!gems` — Draft — Hidden-gem discovery screen. Writes artifacts.
Variants: `!gems [theme]`, `!gems [theme] --deep`

`!track [person name]` — Active — Disclosure tracking research lead. Writes artifacts.
Aliases: `!show track`, `!track rm`
Variants: `!track show`, `!track profile [person name]`, `!track positions [person name]`, `!track remove [person name]`, `!track refresh`

## Watchlist / System

`!wl add [ticker]` — Draft — Add a ticker to the watchlist. Writes artifacts.
Variants: `!wl rm [ticker]`, `!wl show`, `!wl updates`, `!wl updates [ticker]`

`!commands` — Active — Show this menu. No artifacts.

## Notes

- `$` before tickers is optional.
- Bang command names are case-insensitive; display them lowercase.
- `!commands` is menu-only for now; command lookup is deferred.
- Use `!commands`, not `!help`.
- MIDAS outputs are research aids, not Buy/Hold/Sell recommendations.
```

## Display Rules

- Keep the response to the menu only, except for the unsupported-variant note when applicable.
- Use backticks around command examples.
- Prefer bullets and short descriptions over tables for Telegram readability.
- Do not expose registry internals unless the user asks for an audit or maintenance details.
- Do not include source citations; this command does not make company-specific factual claims.
- Do not add commands that are not in `docs/COMMAND_REGISTRY.md`.
- Do not show deprecated commands unless the user explicitly asks for deprecated or legacy commands.

## Final Verification Checklist

Before finalizing a `!commands` response, verify:

- The output is menu-only.
- The menu includes registered non-deprecated commands.
- The menu includes `!market`.
- The menu includes registered `!track` aliases, including `!track rm`.
- Status labels are visible.
- Artifact behavior is visible.
- No research, data retrieval, classification, scoring, metric calculation, artifact write, watchlist mutation, or recommendation language is included.
- The response uses `!commands`, not `!help`.
