# Test Matrix

Status: `PLANNED`

## Required Checks

| Check | Windows | macOS | Linux |
| --- | --- | --- | --- |
| Health check | Required | Required | Required |
| Payload build | Required | Required | Required |
| Payload dry run | Required | Required | Required |
| Installer build | Required before release | Required before release | Required before release |
| Smoke install into temp folder | Required | Required | Required |
| Secret scan | Required | Required | Required |
| Checksum generation | Required | Required | Required |

## Smoke Test Assertions

- Workspace folder created.
- Core docs exist.
- `.vscode` exists.
- `.prompts` exists.
- Datasheet and component scaffolds exist.
- Health check runs.
- Installed KiCad folders are not modified.

