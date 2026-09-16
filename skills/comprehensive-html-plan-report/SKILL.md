---
name: comprehensive-html-plan-report
description: Universal, evidence-first workflow for creating an HTML implementation plan and an HTML execution report that are readable by AI agents and humans.
---

# Comprehensive HTML Plan + Report

Use this skill for material implementation, refactor, migration, security, CI/CD, release, deployment, or incident work. It creates two plain-language HTML documents with the same structure and interaction quality as the repository reference files:

- `/<project-root>/<PROJECT_SLUG>_PLAN.html` before implementation.
- `/<project-root>/<PROJECT_SLUG>_REPORT.html` after implementation and verification.

If the user gives exact filenames or paths, use them exactly. Reference files define format only, never content to copy blindly. Replace project-specific names, IDs, commands, evidence, and risks with facts from the current project.

The repository also contains project-agnostic examples: `PROJECT_PLAN_TEMPLATE.html` and `PROJECT_REPORT_TEMPLATE.html`. Copy them as a starting point, replace every `[placeholder]`, and never carry over another project’s identifiers or evidence.

## Non-negotiable skill policy

### Ponytail is mandatory for every task

Before planning or changing anything, read the complete canonical Ponytail skill and apply it at 100% intensity `full`:

<https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md>

Ponytail applies to every task type, including backend, infrastructure, documentation, release, and HTML work. Follow its YAGNI ladder, inspect the real flow first, prefer existing/native solutions, make the smallest correct change, and leave a runnable check for non-trivial logic. Never add a dependency or abstraction just to make the documents look sophisticated.

### UI/UX skills are conditional and mutually exclusive with non-UI work

Read both complete UI/UX skills only when the current task changes how a user or reader sees, navigates, or interacts with an interface. Creating or editing these HTML documents, anchor CTAs, responsive layout, accessibility, motion, or visual design is UI/UX work, so both skills apply here:

1. <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md>
2. <https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md>

If the current session task has no UI/UX relationship, reading, invoking, quoting, or applying either UI/UX skill is strictly forbidden. Do not load them “just in case.” Ponytail remains mandatory regardless of this conditional rule. System, developer, repository, and current-user instructions always win if they conflict.

## Audience contract

The plan and report serve two audiences at once:

- **AI Agent:** explicit scope, ordered actions, stable checklist IDs, acceptance evidence, constraints, and safe stopping points that can be followed during implementation.
- **Human:** plain-language explanation, visible status, links to evidence, risks, blockers, owner actions, and a short TL;DR.

The report is the AI Agent’s accountability statement to the human. Never call work “done,” “pass,” “secure,” “released,” or “verified” without the corresponding evidence. Write `BLOCKED`, `SKIPPED`, or `NOT RUN` when evidence is missing, and explain why. Separate facts, inferences, and owner-supplied statements.

## Workflow

### 1. Classify and inspect

1. Read current system/developer/user instructions and applicable repository instructions.
2. Read Ponytail in full. Classify whether the work is also UI/UX; if yes, read both UI/UX skills in full, otherwise do not read them.
3. Identify the project root, platforms, environments, existing scripts, CI providers, secret boundaries, and the smallest set of files that can satisfy the request.
4. Do not invent provider state, credentials, test results, paths, versions, or approvals.

### 2. Write the plan before mutations

Create the plan HTML before implementation changes. It must be actionable without a separate conversation and must include:

- a title, date/context, and one-paragraph purpose;
- a TL;DR for a non-technical reader;
- decisions and environment mapping in a table;
- an ordered checklist with stable `data-key` values and stable detail IDs;
- a definition of done and explicit non-goals;
- security and secret-handling boundaries;
- risks, rollback/stop conditions, and required owner input;
- a bottom “Detail setiap checklist” section with one detail card per checklist item.

Every checklist item must have a small, keyboard-accessible CTA such as `Lihat detail` that links to its matching bottom card (`href="#detail-<stable-slug>"`). The bottom `Detail setiap checklist` section must be a native `<details>` toggle and **must be hidden by default**: never add the `open` attribute or auto-open it on page load. Every card must have a clear title, purpose, concrete actions, acceptance evidence, and a `Kembali ke checklist` link. CTA JavaScript may open the group before native fragment navigation; without JavaScript, the visible summary must still let a reader open the section manually.

### 3. Implement minimally

Execute the plan using the smallest correct change. Reuse existing project conventions. Keep unrelated modifications out of the commit. Protect trust boundaries and validation even when simplifying other code. If a plan item becomes invalid, update the plan or record the change and reason; do not silently drift.

### 4. Verify proportionately

Run the lightest checks that prove the changed behavior, then run the required build/test/security checks for the actual risk. Record exact commands, target environment, tool versions when relevant, result, and limitations. Never turn a local check into a claim about CI, a remote machine, a store, or production without direct evidence.

### 5. Write the report as accountability

Create the report HTML only after implementation and verification. It must include:

- a TL;DR with separate `SELESAI`, `BUTUH AKSI OWNER`, `BLOCKED`, `SKIPPED`, or `NOT RUN` statuses;
- the final environment/configuration mapping;
- a “Checklist hasil” section with one row per planned result;
- the same CTA-to-detail pattern and bottom detail section as the plan;
- an evidence table containing commands, links, commit SHAs, MR/PR links, and test results;
- explicit gaps, assumptions, rollback notes, and owner next actions;
- secret hygiene confirmation without printing any secret value.

If implementation differs from the plan, show the difference in the report. If a check could not run, state the exact boundary and do not infer a pass.

### 6. Commit and hand off

When the user requests commit/push, commit only the intended plan, report, skill, README, and implementation files. Report commit SHAs, branch names, remote URLs, and MR/PR state. Do not merge, release, delete branches, or promote an artifact unless the user explicitly authorizes that action. Re-check the remote head after pushing.

## HTML format contract

Use dependency-free HTML so the files open offline in Safari, Chrome, or a file viewer. Keep the dark, compact, responsive visual language from the reference without copying project-specific text:

- `<!doctype html>`, `lang="id"` or the project’s requested language, UTF-8, and a viewport meta tag;
- semantic `header`, `main`, `section`, `article`, `details`, `footer`, and sequential headings;
- a readable system font, high-contrast semantic color tokens, responsive tables, and no horizontal page overflow;
- no remote fonts, scripts, images, analytics, CDN, or secret-bearing query strings unless explicitly requested;
- `html { scroll-behavior: smooth; }` plus `@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }`;
- visible `:focus-visible` styling, keyboard-reachable links, and CTA hit areas of at least 44px where practical;
- `:target` highlighting and `scroll-margin-top` so a detail card is obvious after navigation;
- the bottom `Detail setiap checklist` content inside a closed-by-default `<details id="checklist-details">` with a clear `<summary>` toggle;
- only lightweight, purposeful motion. Do not scroll-jack, use `transition: all`, or add decorative animation to every row;
- plan checkboxes may persist completion in `localStorage` under a versioned, project-specific key; never store secrets or report claims there;
- report checkboxes are read-only evidence indicators and must not pretend to be live state.

Use stable lowercase slugs for IDs (for example `detail-plan-ci`, `detail-result-android`). A CTA target must exist exactly once. Do not use duplicate IDs, empty links, or a link that only works after JavaScript loads.

## Validation checklist

At minimum, run checks appropriate to the environment:

```sh
git diff --check
tidy -q -e -utf8 <PLAN.html> <REPORT.html>
```

Also verify all internal CTA links resolve and every detail card has a return link. A dependency-free Python check is sufficient:

```sh
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.detail_groups = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            assert attrs["id"] not in self.ids, f"duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        if attrs.get("href", "").startswith("#"):
            self.hrefs.append(attrs["href"][1:])
        if tag == "details" and attrs.get("id") == "checklist-details":
            self.detail_groups.append(attrs)

for name in ("<PLAN.html>", "<REPORT.html>"):
    parser = Links()
    parser.feed(Path(name).read_text(encoding="utf-8"))
    missing = sorted(set(parser.hrefs) - parser.ids)
    assert not missing, f"{name}: missing targets: {missing}"
    assert len(parser.detail_groups) == 1, f"{name}: expected one checklist detail toggle"
    assert "open" not in parser.detail_groups[0], f"{name}: detail toggle must be closed by default"
print("internal CTA targets: pass")
PY
```

Finally run the project’s relevant build/test/lint/security checks, inspect the diff, scan for secrets, and confirm that the report does not claim anything beyond the evidence.

## Stop conditions

Stop and report a blocker when a required credential, owner permission, provider registration, signing asset, or environment is unavailable; when a destructive action’s target is ambiguous; or when a requested claim cannot be verified. Continue safe read-only investigation, but do not fabricate a value or weaken a security gate to make the report look complete.
