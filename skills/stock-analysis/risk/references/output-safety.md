# !risk Output Safety

This is command-local support for !risk. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, or SCORING.md.

Use this for recurring output-safety and no-bloat pitfalls. OUTPUT.md owns visible display templates and section order. ARTIFACTS.md owns global artifact standards.

## Readability hygiene

- Lead with the risk conclusion, then explain the evidence and uncertainty.
- Prefer short paragraphs and bullets over dense field dumps.
- Avoid repeating the same thesis-breaking risk across multiple sections unless the repeat adds a distinct angle.
- Keep monitoring items specific and scannable.
- Keep Source Notes concise; do not bury the risk conclusion under provider metadata or source caveats.
- Do not turn normal output into a full filing audit, full financial statement review, thesis memo, valuation model, or complete packet.

## No-bloat boundaries

- Do not include raw filing dumps, giant excerpt blocks, tool logs, hidden reasoning, validation notes, eval checklists, runtime smoke-test language, or implementation diaries in the report.
- Do not create normal-output Evidence Ledger or Risk Heat Map requirements.
- Do not preserve old output headings or old Full-mode structures as active guidance.
- Do not make old Compact, Full, or Deep behavior active inside !risk.
- Do not create backup, version, pointer, archive, schema, proof-packet, source-manifest, evidence-ledger, fixture, or workspace support files unless the user explicitly asks and the relevant authority allows it.

## Saved-path and artifact safety

- Normal !risk writes only `workspace/tickers/[ticker]/risk.md` after the final report passes the current output/artifact validation path.
- A normal response should not be receipt-only when a risk report was requested; provide the report body and then the final saved-path confirmation.
- Show `Saved to: workspace/tickers/[ticker]/risk.md` only after the write succeeds and only as the final line.
- Do not claim a save if the write failed, was skipped, or was not verified.
- Do not save drafts, scratch work, audit output, validation logs, source dumps, manifests, ledgers, proof packets, schemas, or incomplete reports as `risk.md`.

## Audit boundary

- !risk -audit writes nothing and must not show `Saved to:`.
- Audit mode must not create folders, artifacts, source manifests, extracts, evidence ledgers, proof packets, schemas, fixture files, validation logs, runtime smoke outputs, indexes, watchlist changes, or downstream command outputs.
- If audit no-write behavior cannot be guaranteed, stop and report the blocker instead of gathering sources.
