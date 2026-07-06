# Compact `!market` Footer Preference

Session learning: the user explicitly prefers normal successful `!market [ticker]` snapshots to omit routine footer/disclaimer language.

Apply this to normal successful compact output:

- Place `Source: [provider]` directly below `As of:`.
- Do not add routine sentences like:
  - “Market data may be delayed or incomplete.”
  - “This is market context only, not a recommendation…”
- Still show specific/material limitations when needed, such as:
  - stale or uncertain timestamps
  - provider failures or fallbacks that materially explain the output
  - rate-limit notices
  - unavailable required fields in failure/debug contexts
- If the user asks for advice, scoring, classification, or business conclusions inside `!market`, boundary language is allowed, but keep it brief and do not turn it into a routine footer.

Rationale: compact `!market` is a utility snapshot. Routine caveats made successful responses feel noisy; the timestamp and source are enough for the default case.