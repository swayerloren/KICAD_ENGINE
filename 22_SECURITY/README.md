# Security

## PURPOSE

Track repository security policies, script safety, installer safety, and secret-handling rules.

## WHAT_BELONGS_HERE

- Security review notes.
- Secret scan plans.
- Script safety audits.
- Installer security model notes.

## Security Policy Files

- `SECURITY_POLICY.md`
- `SECRET_HANDLING_RULES.md`
- `INSTALLER_SECURITY_RULES.md`
- `SCRIPT_SAFETY_RULES.md`
- `REPORTING_SECURITY_ISSUES.md`

## WHAT_DOES_NOT_BELONG_HERE

- Secrets, API keys, passwords, tokens, private keys, or certificates.
- Exploit code unrelated to defensive testing.
- Credential capture flows.

## AI_AGENT_RULES

- Never store credentials.
- Report unsafe scripts.
- Ensure install scripts ask before installing.
- Do not silently change system or KiCad install folders.

## SAFE_EDIT_RULES

- Add policy docs and review notes.
- Do not write secrets for examples.
- Use placeholders only when clearly marked.

## PUBLIC_RELEASE_NOTES

Public releases must include security policy, no secrets, and no silent credential collection.

Security docs must not include real secrets, tokens, signing keys, or certificates.
