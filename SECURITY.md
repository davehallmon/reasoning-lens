# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 0.x.x (pre-release) | Yes |

## Scope

The installed Skill is Markdown only. It has no executable code, no dependencies, and no network calls. The `evals/` folder holds a maintainer-only Python checker that is not installed.

The realistic security surface is:

- Prompt injection through user-supplied idea text. The Skill treats instructions inside pasted or quoted material as content (`reasoning-lens/references/guards.md`, "Untrusted content"), and eval cases I01–I03 test it.
- Accidental exposure of secrets in issue reports or pull requests
- Malicious pull requests that alter skill behavior

## Reporting a Vulnerability

Open a private security advisory on GitHub: [Report a vulnerability](https://github.com/davehallmon/reasoning-lens/security/advisories/new).

Do not open a public issue for security reports.

Include:

- What you found
- Steps to reproduce
- The impact you see
- Any suggested fix

## Response

I aim to acknowledge reports within 5 business days. I will triage within 10 business days and publish a fix or a written response.

## Out of Scope

- Issues caused by the Claude model itself, not the skill
- Social engineering against the maintainer
- Denial of service through repeated use
