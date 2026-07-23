# Security Policy

This policy is the default for all repositories under `ALeonard9` (the druthers.io
project) that do not define their own `SECURITY.md`.

## Reporting a vulnerability

Please **do not open a public issue** for security problems.

- Preferred: open a [private vulnerability report](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
  via the repository's **Security → Advisories** tab.
- Or email the maintainer at the address on the GitHub profile.

Please include steps to reproduce, affected component/repo, and impact. You'll
get an acknowledgement as soon as practical — this is a small personal project,
so response is best-effort, not SLA-backed.

## Supported versions

Only the latest `main` of each repository is supported. There are no backported
security fixes for older tags.

## Our tooling

These repositories are scanned continuously with open-source tooling — Gitleaks
(secrets), Semgrep (SAST), Trivy (dependencies, containers, IaC), and Dependabot
— plus GitHub secret scanning with push protection. Findings are triaged via the
Security tab and tracked as issues.
