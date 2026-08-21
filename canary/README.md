# Canary fixture

Deliberately broken files. **Nothing here is real code and nothing runs it.**

A security scanner that has silently stopped working looks exactly like one
that found nothing: both report zero findings and exit 0. That is not a
hypothetical. Between 2026-07-22 and 2026-08-21 semgrep never ran in any repo
(`--error=false` is a usage error, `|| true` swallowed it), trivy matched no
dependency file in `druthers-api` and `druthers-mcp`, and every run of both
was green the whole time.

So the pipeline is tested the only way a detector can be: give it something it
must find, and fail if it does not find it.

| File | Planted for | Must be detected as |
|------|-------------|---------------------|
| `requirements.txt` | trivy | `PyYAML==5.1`, 3 criticals (CVE-2019-20477, CVE-2020-1747, CVE-2020-14343) |
| `vulnerable.py` | semgrep | `subprocess-shell-true` and `eval-detected` |
| *(generated at runtime)* | gitleaks | a high-entropy fake AWS credential |

The gitleaks fixture is **generated during the run, never committed**. A
realistic key in git would trip GitHub's push protection, and committing a
credential-shaped string to make a point is a bad habit even when the string
is worthless. AWS's documented example key (`AKIAIOSFODNN7EXAMPLE`) is not an
option either: gitleaks allowlists it, so it detects nothing and the canary
would pass while proving nothing.

**Do not "fix" these files.** Upgrading the pin or deleting the dangerous
functions disables the test. If a scanner legitimately stops reporting one of
these (a rule is retired, a CVE is withdrawn), update the assertion in
`.github/workflows/canary.yml` and this table together, in the same PR.

Nothing here is installed, imported, deployed, or executed. Dependabot is
scoped to `github-actions` in `/`, so it raises no update PRs against
`requirements.txt`.
