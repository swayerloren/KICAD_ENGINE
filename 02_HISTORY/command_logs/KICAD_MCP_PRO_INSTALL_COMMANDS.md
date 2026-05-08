# kicad-mcp-pro Install Commands

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

Scope: install only `kicad-mcp-pro` in isolated Python environment under `03_TOOLS\python_envs\kicad-mcp-pro`.

No global MCP configuration was applied. No real KiCad project files were modified.

## Inspection And Initial Setup Transcript

# kicad-mcp-pro Install Commands

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

Scope: install only `kicad-mcp-pro` in isolated Python environment under `03_TOOLS\python_envs\kicad-mcp-pro`.

No global MCP configuration was applied. No real KiCad project files were modified.


## Command

```powershell
Get-Location
```

### Output

```text
C:\Users\LJ\KICAD_ENGINE
EXIT_CODE: 0
```

## Command

```powershell
git -C "03_TOOLS\repos\kicad-mcp-pro" status --short --branch
```

### Output

```text
## main...origin/main
EXIT_CODE: 0
```

## Command

```powershell
git -C "03_TOOLS\repos\kicad-mcp-pro" rev-parse HEAD
```

### Output

```text
9991061561d1e3551dee03a525c06bf2e2cbaf02
EXIT_CODE: 0
```

## Command

```powershell
rg --files "03_TOOLS\repos\kicad-mcp-pro"
```

### Output

```text
03_TOOLS\repos\kicad-mcp-pro\uv.lock
03_TOOLS\repos\kicad-mcp-pro\package.json
03_TOOLS\repos\kicad-mcp-pro\CODE_OF_CONDUCT.md
03_TOOLS\repos\kicad-mcp-pro\package-lock.json
03_TOOLS\repos\kicad-mcp-pro\mkdocs.yml
03_TOOLS\repos\kicad-mcp-pro\codecov.yml
03_TOOLS\repos\kicad-mcp-pro\mcp.json
03_TOOLS\repos\kicad-mcp-pro\CITATION.cff
03_TOOLS\repos\kicad-mcp-pro\MAINTAINERS.md
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md
03_TOOLS\repos\kicad-mcp-pro\LICENSE
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml
03_TOOLS\repos\kicad-mcp-pro\GOVERNANCE.md
03_TOOLS\repos\kicad-mcp-pro\.env.example
03_TOOLS\repos\kicad-mcp-pro\ROADMAP.md
03_TOOLS\repos\kicad-mcp-pro\renovate.json
03_TOOLS\repos\kicad-mcp-pro\release-please-config.json
03_TOOLS\repos\kicad-mcp-pro\README.md
03_TOOLS\repos\kicad-mcp-pro\pyrightconfig.json
03_TOOLS\repos\kicad-mcp-pro\pyproject.toml
03_TOOLS\repos\kicad-mcp-pro\server.json
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md
03_TOOLS\repos\kicad-mcp-pro\tests\__init__.py
03_TOOLS\repos\kicad-mcp-pro\scripts\workflow_security.py
03_TOOLS\repos\kicad-mcp-pro\scripts\verify_doppler_secrets.sh
03_TOOLS\repos\kicad-mcp-pro\scripts\verify_doppler_secrets.ps1
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py
03_TOOLS\repos\kicad-mcp-pro\scripts\sync-remotes.sh
03_TOOLS\repos\kicad-mcp-pro\scripts\sync-remotes.ps1
03_TOOLS\repos\kicad-mcp-pro\scripts\security_local.py
03_TOOLS\repos\kicad-mcp-pro\scripts\repo-cleanup.sh
03_TOOLS\repos\kicad-mcp-pro\scripts\publish.sh
03_TOOLS\repos\kicad-mcp-pro\scripts\hook_pre_commit.py
03_TOOLS\repos\kicad-mcp-pro\scripts\check_workflows.py
03_TOOLS\repos\kicad-mcp-pro\scripts\check_package_metadata.py
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py
03_TOOLS\repos\kicad-mcp-pro\Taskfile.yml
03_TOOLS\repos\kicad-mcp-pro\SUPPORT.md
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\schematic-to-pcb.md
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\professional-circuit-design.md
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\manufacturing-export.md
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\high-speed-review.md
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\first-pcb.md
03_TOOLS\repos\kicad-mcp-pro\docs\workflow-security.md
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md
03_TOOLS\repos\kicad-mcp-pro\docs\tools-reference.md
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_schema.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_version_control_helpers.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_units.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_tool_metadata_lint.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_symbol_gen.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_signal_power_properties.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_sexpr_property.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_sexpr.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_router.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_refactor_helper_modules.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_power_integrity.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_placement.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_pcb_file_helpers.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_logging.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_layers.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_intent_model.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_impedance_property.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_impedance.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_gate_logic.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_gate_history.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_footprint_gen.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_fixers.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_dru_utils.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_studio_watcher.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_additional.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_design_intent.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_component_search.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_component_contracts.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_benchmark_latency.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py
03_TOOLS\repos\kicad-mcp-pro\docs\security\threat-model.md
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py
03_TOOLS\repos\kicad-mcp-pro\docs\rfcs\README.md
03_TOOLS\repos\kicad-mcp-pro\docs\repository-operations.md
03_TOOLS\repos\kicad-mcp-pro\docs\release-process.md
03_TOOLS\repos\kicad-mcp-pro\docs\maintenance-policy.md
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\units.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\symbol_gen.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\sexpr.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\schematic_router.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\placement.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\pdn_mesh.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\paths.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\logging.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\layers.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\impedance.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\freerouting.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\footprint_gen.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\dru.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\component_search.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\cache.py
03_TOOLS\repos\kicad-mcp-pro\commitlint.config.cjs
03_TOOLS\repos\kicad-mcp-pro\docs\doppler-setup.md
03_TOOLS\repos\kicad-mcp-pro\docs\development.md
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\variants.md
03_TOOLS\repos\kicad-mcp-pro\docs\demo-media.md
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\time-domain.md
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\graphical-drc.md
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md
03_TOOLS\repos\kicad-mcp-pro\docs\comparison.md
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md
03_TOOLS\repos\kicad-mcp-pro\docs\branch-protection.md
03_TOOLS\repos\kicad-mcp-pro\docs\autonomy.md
03_TOOLS\repos\kicad-mcp-pro\Dockerfile
03_TOOLS\repos\kicad-mcp-pro\docs\index.md
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\library.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\gates.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\fixers.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export_support.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\emc_compliance.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\design_intent_state.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\board_file.py
03_TOOLS\repos\kicad-mcp-pro\CONTRIBUTING.md
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10
03_TOOLS\repos\kicad-mcp-pro\docs\api-stability.md
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic_transfer.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing_rules.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\power_integrity.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_latency_baseline.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\kicad\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\kicad\session.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\discovery.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\security.md
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\repository-topology.md
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\azure-devops.md
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\path_safety.py
03_TOOLS\repos\kicad-mcp-pro\docs\assets\icon.png
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\schematic_backend_capability_matrix.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\connection.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\studio_context.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\gate_history.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\__init__.py
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-desktop.md
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md
03_TOOLS\repos\kicad-mcp-pro\docs\integration\cursor.md
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\common.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\component_contracts.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\jlcpcb_standard.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\jlcpcb_rotations.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\jlcpcb_advanced.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\export.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\pcbway_standard.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\oshpark_2layer.json
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\__init__.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\simulation.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\signal_integrity.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\schematic.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\power_integrity.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\pcb.py
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md
03_TOOLS\repos\kicad-mcp-pro\docs\development\contributing.md
03_TOOLS\repos\kicad-mcp-pro\docs\development\contributing-fixtures.md
03_TOOLS\repos\kicad-mcp-pro\docs\development\architecture.md
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sensor_cluster_spread\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sensor_cluster_spread\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sensor_cluster_spread\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_sensor_node\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_sensor_node\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_sensor_node\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\USB_ESD_protection.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\usb2_typec.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\supercap_backup.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\STM32G0_minimal.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\SPI_flash.yaml
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_label_only_schematic\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\RS485_transceiver.yaml
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_label_only_schematic\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\RP2040_minimal.yaml
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_label_only_schematic\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\Motor_driver_half_bridge.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\mcu_decoupling_template.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\LiPo_charger.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\ldo_linear_generic.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\I2C_pullup.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\ethernet_rj45_mag.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\ESP32_S3_wifi.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\CAN_transceiver.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\buzzer_nmos_driver.yaml
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\buck_converter_generic.yaml
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_footprint_overlap_board\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_footprint_overlap_board\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_footprint_overlap_board\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode-http.mcp.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\generic-mcp-client.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\gemini-settings.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\gemini-http-settings.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\cursor.mcp.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-http-config.toml
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-desktop.json
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-code.mcp.json
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_dfm_edge_clearance\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_dfm_edge_clearance\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_dfm_edge_clearance\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_timedomain\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_timedomain\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_timedomain\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_label_only\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_label_only\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_label_only\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_hierarchy\power.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_hierarchy\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_hierarchy\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_sismosmart_like_hierarchy\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_bad_decoupling_placement\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_bad_decoupling_placement\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_custom_drc\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_custom_drc\demo.kicad_dru
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_custom_drc\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_custom_drc\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_dirty_transfer_wrong_pad_nets\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_dirty_transfer_wrong_pad_nets\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_bad_decoupling_placement\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\fail_dirty_transfer_wrong_pad_nets\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_design_blocks\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_design_blocks\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_design_blocks\demo.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_variants\demo.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_variants\demo.kicad_dru
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_variants\demo.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\kicad10_variants\demo.kicad_sch
EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\README.md" -Raw
```

### Output

```text
# KiCad MCP Pro Server
<!-- mcp-name: io.github.oaslananka/kicad-mcp-pro -->

[![PyPI](https://img.shields.io/pypi/v/kicad-mcp-pro.svg)](https://pypi.org/project/kicad-mcp-pro/)
[![CI](https://github.com/oaslananka-lab/kicad-mcp-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/oaslananka-lab/kicad-mcp-pro/actions/workflows/ci.yml)
[![Codecov](https://codecov.io/gh/oaslananka-lab/kicad-mcp-pro/branch/main/graph/badge.svg)](https://codecov.io/gh/oaslananka-lab/kicad-mcp-pro)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/oaslananka-lab/kicad-mcp-pro/badge)](https://scorecard.dev/viewer/?uri=github.com/oaslananka-lab/kicad-mcp-pro)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](pyproject.toml)
[![KiCad 10](https://img.shields.io/badge/KiCad-10-success.svg)](https://www.kicad.org)

KiCad MCP Pro is a production-focused Model Context Protocol server for KiCad PCB and schematic workflows. It gives agents project setup, schematic editing, PCB inspection and edits, validation gates, DFM checks, SI/PI helpers, simulation helpers, and release-gated manufacturing export.

Use it with Claude Desktop, Claude Code, Cursor, VS Code, Codex, or any MCP-compatible client.

## Quick Start

Install and run with `uvx`:

```bash
uvx kicad-mcp-pro --help
uvx kicad-mcp-pro health --json
uvx kicad-mcp-pro doctor --json
uvx kicad-mcp-pro serve
```

Or install with `pip`:

```bash
pip install kicad-mcp-pro
kicad-mcp-pro --help
kicad-mcp-pro health --json
kicad-mcp-pro serve
```

The default no-subcommand invocation still starts the stdio MCP server for
backward compatibility. `health --json` is safe to run when KiCad is not
running; it reports KiCad IPC as deferred instead of crashing. `doctor --json`
adds deeper CLI and IPC diagnostics for launchers such as `kicad-studio`.

## Minimal MCP Config

Use an absolute KiCad project path:

```json
{
  "servers": {
    "kicad": {
      "type": "stdio",
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_WORKSPACE_ROOT": "/absolute/path/to/your/workspace",
        "KICAD_MCP_PROFILE": "pcb_only"
      }
    }
  }
}
```

More client examples:

- [Client configuration](docs/client-configuration.md)
- [Claude Desktop](docs/integration/claude-desktop.md)
- [Cursor](docs/integration/cursor.md)
- [Claude Code](docs/integration/claude-code.md)
- [KiCad Studio](docs/integration/kicad-studio.md)

## What It Does

- Project-aware setup with safe path handling and recent-project discovery.
- PCB tools for board state, tracks, vias, footprints, layers, zones, placement, and sync.
- Schematic tools for symbols, wires, labels, buses, annotation, templates, routing, and IPC reload.
- Validation gates for schematic quality, connectivity, PCB quality, placement, transfer, DFM, and manufacturing.
- Gated release handoff through `export_manufacturing_package()`.
- Export tools for Gerber, drill, BOM, PDF, netlist, STEP, render, pick-and-place, IPC-2581, SVG, and DXF.
- SI, PI, EMC, routing, simulation, library, and version-control helper surfaces.
- Server profiles such as `minimal`, `pcb_only`, `schematic_only`, `manufacturing`, `analysis`, and `agent_full`.
- Machine-readable CLI diagnostics for editors and MCP clients.

## Common Workflow

```text
kicad_set_project()
project_get_design_spec()
sch_build_circuit()
pcb_sync_from_schematic()
project_quality_gate_report()
export_manufacturing_package()
```

Demo media guidance lives in [docs/demo-media.md](docs/demo-media.md).

## Documentation

- [Installation](docs/installation.md)
- [Configuration](docs/configuration.md)
- [Tools reference](docs/tools-reference.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)
- [API stability](docs/api-stability.md)
- [Release process](docs/release-process.md)
- [Maintenance policy](docs/maintenance-policy.md)
- [Workflow security](docs/workflow-security.md)
- [Security threat model](docs/security/threat-model.md)
- [Comparison](docs/comparison.md)

## Repository Operations

Normal CI and security workflows run on pull requests, pushes, and merge queue
events. Release, publish, mirroring, deployment, and token-backed jobs remain
guarded behind explicit repository checks and protected environments.

The project uses Dependabot, Renovate, CodeQL, Gitleaks, Trivy, OpenSSF
Scorecard, Codecov, release-please, SBOM generation, Sigstore signing, and
GitHub artifact attestations for release hardening.

Operational references:

- [Repository operations](docs/repository-operations.md)
- [Autonomy model](docs/autonomy.md)
- [Doppler setup](docs/doppler-setup.md)
- [Branch protection](docs/branch-protection.md)

## Contributing and Support

- [Contributing](CONTRIBUTING.md)
- [Support](SUPPORT.md)
- [Governance](GOVERNANCE.md)
- [Security policy](SECURITY.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\docs\installation.md" -Raw
```

### Output

```text
# Installation

## Recommended
```bash
uvx kicad-mcp-pro
```

## Package install
```bash
pip install kicad-mcp-pro
```

## HTTP support
```bash
pip install "kicad-mcp-pro[http]"
```

After installation, add the server to your MCP client. See
[Client Configuration](client-configuration.md) for VS Code, Codex, Claude, Cursor,
Gemini CLI, and generic MCP client examples.

EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md" -Raw
```

### Output

```text
# Client Configuration

KiCad MCP Pro works with MCP clients that can start a local `stdio` server or connect to a
Streamable HTTP endpoint. The most portable setup is local `stdio` with `uvx`.

Replace `/absolute/path/to/your/kicad-project` with your KiCad project directory. You can
omit `KICAD_MCP_PROJECT_DIR` and call `kicad_set_project()` from the client instead, but
setting it once in the client config gives you a persistent default project.

## Recommended Local Server

Use this command in clients that ask for a command and arguments:

```text
command: uvx
args: ["kicad-mcp-pro"]
```

Recommended environment:

```text
KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project
KICAD_MCP_PROFILE=pcb_only
```

Use `KICAD_MCP_PROFILE=full` if you want every tool category. Preferred focused profiles are
`minimal`, `pcb_only`, `schematic_only`, `manufacturing`, `high_speed`, `power`,
`simulation`, and `analysis`. Legacy aliases `pcb` and `schematic` still work for older
client configs.

## VS Code And GitHub Copilot

VS Code uses `.vscode/mcp.json` for workspace-level configuration and a user profile MCP
configuration for global setup. GitHub Copilot in VS Code uses the same MCP server setup.

`.vscode/mcp.json`:

```json
{
  "servers": {
    "kicad": {
      "type": "stdio",
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_PROFILE": "pcb_only"
      }
    }
  }
}
```

Use an absolute KiCad project path for `KICAD_MCP_PROJECT_DIR`. Some VS Code MCP setups do
not expand `${workspaceFolder}` and may fail at server startup.

## Codex CLI And Codex IDE Extension

Codex stores MCP servers in `~/.codex/config.toml` or a trusted project-scoped
`.codex/config.toml`.

CLI setup:

```bash
codex mcp add kicad \
  --env KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project \
  --env KICAD_MCP_PROFILE=pcb_only \
  -- uvx kicad-mcp-pro
```

`~/.codex/config.toml`:

```toml
[mcp_servers.kicad]
command = "uvx"
args = ["kicad-mcp-pro"]
startup_timeout_sec = 20
tool_timeout_sec = 120

[mcp_servers.kicad.env]
KICAD_MCP_PROJECT_DIR = "/absolute/path/to/your/kicad-project"
KICAD_MCP_PROFILE = "pcb_only"
```

## Claude Desktop

Add the server to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "kicad": {
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_PROFILE": "pcb_only"
      }
    }
  }
}
```

## Claude Code

Use KiCad MCP Pro 3.0.2 or newer for Claude Code `stdio` setups. That release defers
heavy tool registration until after the MCP `initialize` handshake, avoiding startup races
on slower WSL or cold KiCad environments.

Project-scoped `.mcp.json`:

```json
{
  "mcpServers": {
    "kicad": {
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_PROFILE": "pcb_only"
      }
    }
  }
}
```

CLI setup:

```bash
claude mcp add kicad \
  --scope project \
  --env KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project \
  --env KICAD_MCP_PROFILE=pcb_only \
  -- uvx kicad-mcp-pro
```

## Cursor

Use `.cursor/mcp.json` for project configuration or `~/.cursor/mcp.json` for global
configuration:

```json
{
  "mcpServers": {
    "kicad": {
      "type": "stdio",
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_PROFILE": "pcb_only"
      }
    }
  }
}
```

## Gemini CLI

Add the server to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "kicad": {
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_PROFILE": "pcb_only"
      },
      "timeout": 120000
    }
  }
}
```

## Antigravity And Other MCP Clients

If your client accepts the common `mcpServers` JSON shape, use this as the starting point:

```json
{
  "mcpServers": {
    "kicad": {
      "type": "stdio",
      "command": "uvx",
      "args": ["kicad-mcp-pro"],
      "env": {
        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
        "KICAD_MCP_PROFILE": "pcb_only"
      }
    }
  }
}
```

Client-specific behavior can vary. If the client supports only HTTP servers, use the HTTP
setup below.

## Streamable HTTP Setup

Start KiCad MCP Pro as an HTTP server:

```bash
kicad-mcp-pro --transport http --host 127.0.0.1 --port 3334
```

The default endpoint is:

```text
http://127.0.0.1:3334/mcp
```

VS Code HTTP example:

```json
{
  "servers": {
    "kicad": {
      "type": "http",
      "url": "http://127.0.0.1:3334/mcp"
    }
  }
}
```

Codex HTTP example:

```toml
[mcp_servers.kicad]
url = "http://127.0.0.1:3334/mcp"
tool_timeout_sec = 120
```

Gemini CLI HTTP example:

```json
{
  "mcpServers": {
    "kicad": {
      "httpUrl": "http://127.0.0.1:3334/mcp",
      "timeout": 120000
    }
  }
}
```

## References

- VS Code MCP configuration: https://code.visualstudio.com/docs/copilot/customization/mcp-servers
- Codex MCP configuration: https://developers.openai.com/codex/mcp
- Claude Code MCP configuration: https://docs.anthropic.com/en/docs/claude-code/mcp
- Anthropic MCP overview: https://docs.anthropic.com/en/docs/mcp
- Cursor MCP configuration: https://docs.cursor.com/en/context/mcp
- Gemini CLI MCP setup notes: https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md

EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\pyproject.toml" -Raw
```

### Output

```text
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "kicad-mcp-pro"
version = "3.1.8"
description = "A professional Model Context Protocol server for KiCad EDA."
readme = "README.md"
license = { text = "MIT" }
license-files = []
authors = [{ name = "Osman Aslan" }]
keywords = [
  "kicad",
  "mcp",
  "pcb",
  "eda",
  "ai",
  "llm",
  "schematic",
  "pcb-design",
  "eda-automation",
  "gerber-export",
]
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Intended Audience :: Science/Research",
  "Operating System :: OS Independent",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.13",
  "Programming Language :: Python :: 3.14",
  "Programming Language :: Python :: Implementation :: CPython",
  "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
  "Topic :: Software Development :: Code Generators",
  "Topic :: Software Development :: Libraries :: Python Modules",
]
requires-python = ">=3.12"
dependencies = [
  "authlib>=1.6.11",
  "anyio>=4.4.0",
  "kicad-sch-api>=0.5.0,<0.6",
  "kicad-python>=0.6,<0.8",
  "mcp[cli]>=1.23.0",
  "pydantic>=2.7.0",
  "pydantic-settings>=2.3.0",
  "rich>=13.7.0",
  "structlog>=24.2.0",
  "typer>=0.12.0",
]

[project.optional-dependencies]
components = ["gql>=3.5.0", "httpx>=0.27.0"]
dev = [
  "bandit>=1.7.9",
  "hypothesis>=6.100.0",
  "mkdocs-material>=9.5.32",
  "mkdocs-git-revision-date-localized-plugin>=1.2.9",
  "mkdocs-glightbox>=0.4.0",
  "mkdocs-minify-plugin>=0.8.0",
  "mkdocs-redirects>=1.2.1",
  "mkdocstrings[python]>=0.25.0",
  "mutmut>=3.0.0",
  "mypy>=1.10.0",
  "pytest>=8.2.0",
  "pytest-benchmark>=4.0.0",
  "pytest-cov>=5.0.0",
  "pytest-mock>=3.14.0",
  "pytest-testmon>=2.1.1",
  "pytest-xdist>=3.6.0",
  "pyright>=1.1.390",
  "radon>=6.0.1",
  "ruff>=0.4.0",
  "safety>=3.2.0",
  "vulture>=2.11",
  "zizmor>=1.24.1",
]
freerouting = ["docker>=7.0.0"]
http = ["httpx>=0.27.0", "uvicorn[standard]>=0.30.0"]
simulation = ["numpy>=1.26.0"]
vcs = ["gitpython>=3.1.47,<4.0.0"]

[project.scripts]
kicad-mcp-pro = "kicad_mcp.server:main"

[project.urls]
Homepage = "https://github.com/oaslananka/kicad-mcp-pro"
Documentation = "https://oaslananka.github.io/kicad-mcp-pro"
Repository = "https://github.com/oaslananka/kicad-mcp-pro"
"Bug Tracker" = "https://github.com/oaslananka/kicad-mcp-pro/issues"
Changelog = "https://github.com/oaslananka/kicad-mcp-pro/blob/main/CHANGELOG.md"
Funding = "https://github.com/sponsors/oaslananka"

[tool.hatch.build.targets.wheel]
packages = ["src/kicad_mcp"]

[tool.hatch.build.targets.sdist]
include = ["src/kicad_mcp", "README.md", "LICENSE", "pyproject.toml"]

[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "S", "ANN"]
ignore = ["S603"]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["ANN001", "ANN202", "S101"]

[tool.mypy]
python_version = "3.12"
strict = true
plugins = ["pydantic.mypy"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"
markers = [
  "benchmark: lightweight performance regression checks with committed baselines",
  "slow: tests that are useful for scheduled/full validation but skipped by fast loops",
]

[tool.interrogate]
ignore-init-method = true
ignore-init-module = true
ignore-magic = true
ignore-module = false
ignore-nested-functions = true
ignore-private = true
fail-under = 80
verbose = 1

[tool.coverage.run]
source = ["src/kicad_mcp"]
omit = ["tests/*"]

[tool.coverage.report]
fail_under = 90

EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\mcp.json" -Raw
```

### Output

```text
{
  "name": "io.github.oaslananka/kicad-mcp-pro",
  "displayName": "KiCad MCP Pro Server",
  "description": "Compatibility metadata for KiCad MCP Pro. Prefer server.json for official MCP Registry publication.",
  "version": "3.1.8",
  "license": "MIT",
  "repository": "https://github.com/oaslananka/kicad-mcp-pro",
  "homepage": "https://oaslananka.github.io/kicad-mcp-pro",
  "tools": true,
  "transports": [
    "stdio",
    "streamable-http"
  ],
  "resources": true,
  "prompts": true,
  "platforms": [
    "windows",
    "macos",
    "linux"
  ]
}

EXIT_CODE: 0
```

## Command

```powershell
rg -n "uvx|venv|pip|install|health|doctor|server|stdio|profile|KICAD_|MCP|environment|env|codex|read-only|analysis|write" "03_TOOLS\repos\kicad-mcp-pro"
```

### Output

```text
03_TOOLS\repos\kicad-mcp-pro\.env.example:1:# KiCad MCP Pro Server environment configuration
03_TOOLS\repos\kicad-mcp-pro\.env.example:4:# KICAD_MCP_KICAD_CLI=/usr/bin/kicad-cli
03_TOOLS\repos\kicad-mcp-pro\.env.example:5:# KICAD_CLI_PATH=/usr/bin/kicad-cli
03_TOOLS\repos\kicad-mcp-pro\.env.example:6:# KICAD_MCP_FREEROUTING_JAR=/path/to/freerouting.jar
03_TOOLS\repos\kicad-mcp-pro\.env.example:7:# KICAD_MCP_FREEROUTING_IMAGE=ghcr.io/freerouting/freerouting:2.1.0
03_TOOLS\repos\kicad-mcp-pro\.env.example:8:# KICAD_MCP_FREEROUTING_TIMEOUT_SEC=900
03_TOOLS\repos\kicad-mcp-pro\.env.example:9:# KICAD_MCP_DOCKER_EXECUTABLE=docker
03_TOOLS\repos\kicad-mcp-pro\.env.example:10:# KICAD_MCP_JAVA_EXECUTABLE=java
03_TOOLS\repos\kicad-mcp-pro\.env.example:11:# KICAD_MCP_NGSPICE_CLI=/usr/bin/ngspice
03_TOOLS\repos\kicad-mcp-pro\.env.example:14:# KICAD_MCP_KICAD_SOCKET_PATH=/tmp/kicad.sock
03_TOOLS\repos\kicad-mcp-pro\.env.example:15:# KICAD_MCP_KICAD_TOKEN=replace-with-your-kicad-ipc-token
03_TOOLS\repos\kicad-mcp-pro\.env.example:16:# KICAD_API_TOKEN=replace-with-your-kicad-ipc-token
03_TOOLS\repos\kicad-mcp-pro\.env.example:19:# KICAD_MCP_WORKSPACE_ROOT=/path/to/allowed/workspace
03_TOOLS\repos\kicad-mcp-pro\.env.example:20:KICAD_MCP_PROJECT_DIR=/path/to/your/kicad/project
03_TOOLS\repos\kicad-mcp-pro\.env.example:21:# KICAD_MCP_PROJECT_FILE=/path/to/project.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\.env.example:22:# KICAD_MCP_PCB_FILE=/path/to/board.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\.env.example:23:# KICAD_MCP_SCH_FILE=/path/to/schematic.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\.env.example:24:# KICAD_MCP_OUTPUT_DIR=/path/to/output
03_TOOLS\repos\kicad-mcp-pro\.env.example:27:# KICAD_MCP_SYMBOL_LIBRARY_DIR=/path/to/kicad/symbols
03_TOOLS\repos\kicad-mcp-pro\.env.example:28:# KICAD_MCP_FOOTPRINT_LIBRARY_DIR=/path/to/kicad/footprints
03_TOOLS\repos\kicad-mcp-pro\.env.example:31:# KICAD_MCP_TRANSPORT=stdio
03_TOOLS\repos\kicad-mcp-pro\.env.example:32:# KICAD_MCP_HOST=127.0.0.1
03_TOOLS\repos\kicad-mcp-pro\.env.example:33:# KICAD_MCP_PORT=3334
03_TOOLS\repos\kicad-mcp-pro\.env.example:35:# KICAD_MCP_MOUNT_PATH=/mcp
03_TOOLS\repos\kicad-mcp-pro\.env.example:36:# KICAD_MCP_CORS_ORIGINS=https://app.example.com,http://127.0.0.1:3334
03_TOOLS\repos\kicad-mcp-pro\.env.example:37:# KICAD_MCP_AUTH_TOKEN=replace-with-a-local-bearer-token
03_TOOLS\repos\kicad-mcp-pro\.env.example:38:# KICAD_MCP_LEGACY_SSE=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:39:# KICAD_MCP_STATEFUL_HTTP=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:40:# KICAD_MCP_ENABLE_METRICS=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:41:# KICAD_MCP_STUDIO_WATCH_DIR=/path/to/projects
03_TOOLS\repos\kicad-mcp-pro\.env.example:42:# KICAD_MCP_PROFILE=full
03_TOOLS\repos\kicad-mcp-pro\.env.example:45:# KICAD_MCP_LOG_LEVEL=INFO
03_TOOLS\repos\kicad-mcp-pro\.env.example:46:# KICAD_MCP_LOG_FORMAT=console
03_TOOLS\repos\kicad-mcp-pro\.env.example:49:# KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:50:# KICAD_MCP_IPC_CONNECTION_TIMEOUT=10.0
03_TOOLS\repos\kicad-mcp-pro\.env.example:51:# KICAD_MCP_TIMEOUT_MS=10000
03_TOOLS\repos\kicad-mcp-pro\.env.example:52:# KICAD_MCP_RETRIES=2
03_TOOLS\repos\kicad-mcp-pro\.env.example:53:# KICAD_MCP_HEADLESS=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:54:# KICAD_MCP_CLI_TIMEOUT=120.0
03_TOOLS\repos\kicad-mcp-pro\.env.example:55:# KICAD_MCP_MAX_ITEMS_PER_RESPONSE=200
03_TOOLS\repos\kicad-mcp-pro\.env.example:56:# KICAD_MCP_MAX_TEXT_RESPONSE_CHARS=50000
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:45:          - script: python -m pip install --upgrade uv
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:64:            displayName: Run pip-audit
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:67:              set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:78:                  echo "Safety scan could not complete cleanly (exit ${safety_exit}); pip-audit remains the enforced SCA gate for this pipeline."
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:81:                echo "SAFETY_API_KEY is not set; pip-audit already ran as the enforced SCA gate."
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:84:            env:
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:88:              set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:90:                (curl -Ls --tlsv1.2 --proto "=https" --retry 3 https://cli.doppler.com/install.sh || wget -t 3 -qO- https://cli.doppler.com/install.sh) | sudo sh
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:96:                  echo "Doppler-backed Safety scan could not complete cleanly (exit ${safety_exit}); pip-audit remains the enforced SCA gate for this pipeline."
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:102:            env:
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:121:          - script: python -m pip install --upgrade uv
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:160:          - script: python -m pip install --upgrade uv
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:194:          - script: python -m pip install --upgrade twine
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:198:              set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:201:                (curl -Ls --tlsv1.2 --proto "=https" --retry 3 https://cli.doppler.com/install.sh || wget -t 3 -qO- https://cli.doppler.com/install.sh) | sudo sh
03_TOOLS\repos\kicad-mcp-pro\azure-pipelines.yml:227:            env:
03_TOOLS\repos\kicad-mcp-pro\CITATION.cff:2:message: "If you use KiCad MCP Pro in research, please cite it using this metadata."
03_TOOLS\repos\kicad-mcp-pro\CITATION.cff:3:title: "KiCad MCP Pro"
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:30:* resolve open KiCad MCP issue set ([1adb506](https://github.com/oaslananka-lab/kicad-mcp-pro/commit/1adb5066c3499d6028cd5fc2d0a70100d76f44ad))
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:43:- Published the CLI diagnostics surface with `health`, `doctor`, `serve`, and
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:44:  `version` commands so `uvx kicad-mcp-pro health --json` and
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:45:  `uvx kicad-mcp-pro doctor --json` work from the released package.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:52:* keep task install non-admin on windows ([3b020cf](https://github.com/oaslananka-lab/kicad-mcp-pro/commit/3b020cf55e866e32e74c2834a580d5b8c36b0ae8))
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:53:* keep task install non-admin on windows ([9d4b7b4](https://github.com/oaslananka-lab/kicad-mcp-pro/commit/9d4b7b426815f67983d219d852597eaef6554bd8))
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:61:* install workflow lint tool in release ([#22](https://github.com/oaslananka-lab/kicad-mcp-pro/issues/22)) ([be85674](https://github.com/oaslananka-lab/kicad-mcp-pro/commit/be8567489c540338ff2c2572d9474eb83316bca9))
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:99:- Fixed Claude Code `stdio` startup races by deferring heavy tool/resource registration
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:100:  until after the MCP `initialize` handshake can bind.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:111:- Added HTTP token rotation, per-tool metrics, request audit logging, heavy-tool rate limiting, and expanded server-card capability negotiation.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:114:- Added release-hardening tests for profile discovery, fixer imports, gate-history migrations, watcher locking, CLI retry behavior, structured errors, metadata linting, and benchmark latency.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:119:- Tool execution failures now return MCP `isError` results with structured `error_code`, `message`, and `hint` content for capable clients.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:125:- Fixed discovery gaps for validation CLI tools and the `builder`, `critic`, and `release_manager` profile surface.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:142:- Schematic wire writes now deduplicate duplicate segments and merge collinear runs before persisting.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:193:- Made Azure DevOps release validation resilient to expired or unavailable `SAFETY_API_KEY` credentials so `pip-audit` remains the enforced dependency gate instead of breaking the publish pipeline on auth failures.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:213:- Project manifest, gate-history, design-intent, and layer-coverage MCP resources plus high-speed, bringup, DFM polish, and regression prompt workflows.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:214:- An opt-in Prometheus `/metrics` endpoint for Streamable HTTP deployments when `KICAD_MCP_ENABLE_METRICS=true`.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:224:- Extended high-speed preflight checks with critical-frequency via-stub resonance warnings, package-envelope thermal via sizing, and design-intent-driven EMC return-path continuity sweeps.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:229:- Added SPICE directive validation for simulation sidecar entries while keeping existing analysis directives backward compatible.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:236:- Removed the optional `InSpice` extra dependency from published package metadata so the vulnerable transitive `diskcache` runtime dependency is no longer installed with `simulation`.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:241:- Clarified simulation documentation to describe `ngspice` CLI as the default backend with manual `InSpice` support when users install it explicitly.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:248:- Wired the root Azure pipeline to the shared PyPI credential group and removed the environment gate from the publish stage so automated release runs complete end-to-end.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:256:- Time-domain routing helpers, tuning profiles, graphical DRC rule management, 3D PDF export, and manufacturing import commands.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:257:- KiCad Studio context resource support, local HTTP bridge documentation, `.well-known` discovery metadata, and Azure DevOps pipeline definition.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:262:- Added inferred MCP tool annotations, progress reporting for long-running tools, and client-side sampling integration in the auto-fix loop.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:270:- Aligned quality gates, router profile declarations, lint/type expectations, and release metadata for full-suite validation.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:276:- Restored complete sdist/wheel contents for package installs and `uvx` entrypoints.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:277:- Preserved environment-based MCP client configuration unless CLI options explicitly override it.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:279:- Rejected export output traversal/absolute path writes and escaped custom symbol strings.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:305:- Signal integrity, power integrity, EMC compliance, DFM profile, HDI/multilayer, and Git checkpoint tool families.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:306:- Focused v2 server profiles for `schematic_only`, `pcb_only`, `high_speed`, `power`, `simulation`, and `analysis`.
03_TOOLS\repos\kicad-mcp-pro\CHANGELOG.md:329:- MCP resources, prompts, profiles, and refactored project/PCB/schematic/export tooling.
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:8:    environment:
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:9:      KICAD_MCP_PROJECT_DIR: /projects
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:10:      KICAD_MCP_LOG_LEVEL: INFO
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:11:      KICAD_MCP_LOG_FORMAT: json
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:12:      KICAD_MCP_TRANSPORT: http
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:13:      KICAD_MCP_OUTPUT_DIR: /tmp/kicad-mcp-output
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:15:      - ${KICAD_PROJECT_DIR:-./example}:/projects:ro
03_TOOLS\repos\kicad-mcp-pro\docker-compose.yml:21:      - ${KICAD_PROJECT_DIR:-./example}:/data
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:5:RUN pip install --no-cache-dir uv
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:13:COPY --from=builder --chown=kicadmcp:kicadmcp /app/.venv .venv
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:16:LABEL org.opencontainers.image.description="KiCad MCP Pro - kicad-cli export and validation tools require a KiCad installation mounted at /usr/bin/kicad-cli"
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:17:ENV PATH="/app/.venv/bin:$PATH"
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:18:ENV KICAD_MCP_TRANSPORT=streamable-http
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:19:ENV KICAD_MCP_HOST=0.0.0.0
03_TOOLS\repos\kicad-mcp-pro\Dockerfile:20:ENV KICAD_MCP_KICAD_CLI=/usr/bin/kicad-cli
03_TOOLS\repos\kicad-mcp-pro\CONTRIBUTING.md:6:uv python install 3.12
03_TOOLS\repos\kicad-mcp-pro\CONTRIBUTING.md:15:  and `.nvmrc`, then install with `corepack npm ci` so `package-lock.json`
03_TOOLS\repos\kicad-mcp-pro\CONTRIBUTING.md:31:- `corepack npm run security` runs `bandit` and `pip-audit`.
03_TOOLS\repos\kicad-mcp-pro\CONTRIBUTING.md:51:- Keep `mcp.json` and `server.json` generated from `pyproject.toml` with `npm run metadata:sync`.
03_TOOLS\repos\kicad-mcp-pro\CONTRIBUTING.md:56:- Prefer `uv run python -m pytest`, `uv run python -m mypy`, `uv run python -m bandit`, `uv run python -m pip_audit`, and `uv run python -m safety` for cross-platform local commands.
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:5:ARG KICAD_APPIMAGE_URL
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:6:RUN test -n "${KICAD_APPIMAGE_URL}" || (echo "Set KICAD_APPIMAGE_URL to an official KiCad 10 x86_64 AppImage URL from https://www.kicad.org/download/linux/" && exit 1)
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:8:    && apt-get install -y --no-install-recommends ca-certificates curl fuse libfuse2 file \
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:10:RUN curl -fL "${KICAD_APPIMAGE_URL}" -o /tmp/kicad.AppImage \
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:18:RUN pip install --no-cache-dir uv
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:26:    && apt-get install -y --no-install-recommends ca-certificates libgl1 libglib2.0-0 \
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:30:COPY --from=builder --chown=kicadmcp:kicadmcp /app/.venv .venv
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:34:ENV PATH="/app/.venv/bin:/opt/kicad-appimage/usr/bin:$PATH"
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:35:ENV KICAD_MCP_TRANSPORT=streamable-http
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:36:ENV KICAD_MCP_HOST=0.0.0.0
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:37:ENV KICAD_MCP_KICAD_CLI=/opt/kicad-appimage/usr/bin/kicad-cli
03_TOOLS\repos\kicad-mcp-pro\Dockerfile.kicad10:38:LABEL org.opencontainers.image.description="KiCad MCP Pro with KiCad 10 kicad-cli extracted from an official AppImage. Intended for CI, not shared hosting."
03_TOOLS\repos\kicad-mcp-pro\GOVERNANCE.md:3:KiCad MCP Pro is maintained by `@oaslananka`. The project uses maintainer-led decisions with lazy consensus for routine changes.
03_TOOLS\repos\kicad-mcp-pro\GOVERNANCE.md:8:- User-facing behavior, public tool contracts, profile changes, transport behavior, and release policy changes need an issue or discussion before implementation.
03_TOOLS\repos\kicad-mcp-pro\mcp.json:3:  "displayName": "KiCad MCP Pro Server",
03_TOOLS\repos\kicad-mcp-pro\mcp.json:4:  "description": "Compatibility metadata for KiCad MCP Pro. Prefer server.json for official MCP Registry publication.",
03_TOOLS\repos\kicad-mcp-pro\mcp.json:11:    "stdio",
03_TOOLS\repos\kicad-mcp-pro\package-lock.json:529:        "env-paths": "^2.2.1",
03_TOOLS\repos\kicad-mcp-pro\package-lock.json:587:    "node_modules/env-paths": {
03_TOOLS\repos\kicad-mcp-pro\package-lock.json:589:      "resolved": "https://registry.npmjs.org/env-paths/-/env-paths-2.2.1.tgz",
03_TOOLS\repos\kicad-mcp-pro\package-lock.json:1033:        "tsserver": "bin/tsserver"
03_TOOLS\repos\kicad-mcp-pro\mkdocs.yml:1:site_name: KiCad MCP Pro
03_TOOLS\repos\kicad-mcp-pro\mkdocs.yml:46:  - Installation: installation.md
03_TOOLS\repos\kicad-mcp-pro\pyrightconfig.json:3:  "exclude": ["**/__pycache__", ".venv", "dist", "site"],
03_TOOLS\repos\kicad-mcp-pro\pyproject.toml:8:description = "A professional Model Context Protocol server for KiCad EDA."
03_TOOLS\repos\kicad-mcp-pro\pyproject.toml:84:kicad-mcp-pro = "kicad_mcp.server:main"
03_TOOLS\repos\kicad-mcp-pro\package.json:9:    "metadata:sync": "uv run python scripts/sync_mcp_metadata.py --write",
03_TOOLS\repos\kicad-mcp-pro\renovate.json:41:      "description": "Require approval for core KiCad/MCP/Pydantic/Typer ecosystem packages.",
03_TOOLS\repos\kicad-mcp-pro\release-please-config.json:20:          "path": "server.json",
03_TOOLS\repos\kicad-mcp-pro\release-please-config.json:25:          "path": "server.json",
03_TOOLS\repos\kicad-mcp-pro\README.md:1:# KiCad MCP Pro Server
03_TOOLS\repos\kicad-mcp-pro\README.md:12:KiCad MCP Pro is a production-focused Model Context Protocol server for KiCad PCB and schematic workflows. It gives agents project setup, schematic editing, PCB inspection and edits, validation gates, DFM checks, SI/PI helpers, simulation helpers, and release-gated manufacturing export.
03_TOOLS\repos\kicad-mcp-pro\README.md:14:Use it with Claude Desktop, Claude Code, Cursor, VS Code, Codex, or any MCP-compatible client.
03_TOOLS\repos\kicad-mcp-pro\README.md:18:Install and run with `uvx`:
03_TOOLS\repos\kicad-mcp-pro\README.md:21:uvx kicad-mcp-pro --help
03_TOOLS\repos\kicad-mcp-pro\README.md:22:uvx kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\README.md:23:uvx kicad-mcp-pro doctor --json
03_TOOLS\repos\kicad-mcp-pro\README.md:24:uvx kicad-mcp-pro serve
03_TOOLS\repos\kicad-mcp-pro\README.md:27:Or install with `pip`:
03_TOOLS\repos\kicad-mcp-pro\README.md:30:pip install kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\README.md:32:kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\README.md:36:The default no-subcommand invocation still starts the stdio MCP server for
03_TOOLS\repos\kicad-mcp-pro\README.md:37:backward compatibility. `health --json` is safe to run when KiCad is not
03_TOOLS\repos\kicad-mcp-pro\README.md:38:running; it reports KiCad IPC as deferred instead of crashing. `doctor --json`
03_TOOLS\repos\kicad-mcp-pro\README.md:41:## Minimal MCP Config
03_TOOLS\repos\kicad-mcp-pro\README.md:47:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\README.md:49:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\README.md:50:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\README.md:52:      "env": {
03_TOOLS\repos\kicad-mcp-pro\README.md:53:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\README.md:54:        "KICAD_MCP_WORKSPACE_ROOT": "/absolute/path/to/your/workspace",
03_TOOLS\repos\kicad-mcp-pro\README.md:55:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\README.md:79:- Server profiles such as `minimal`, `pcb_only`, `schematic_only`, `manufacturing`, `analysis`, and `agent_full`.
03_TOOLS\repos\kicad-mcp-pro\README.md:80:- Machine-readable CLI diagnostics for editors and MCP clients.
03_TOOLS\repos\kicad-mcp-pro\README.md:97:- [Installation](docs/installation.md)
03_TOOLS\repos\kicad-mcp-pro\README.md:113:guarded behind explicit repository checks and protected environments.
03_TOOLS\repos\kicad-mcp-pro\server.json:2:  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
03_TOOLS\repos\kicad-mcp-pro\server.json:4:  "title": "KiCad MCP Pro Server",
03_TOOLS\repos\kicad-mcp-pro\server.json:5:  "description": "A professional Model Context Protocol server for KiCad EDA.",
03_TOOLS\repos\kicad-mcp-pro\server.json:18:        "type": "stdio"
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md:13:- Affected versions, environments, and likely impact
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md:30:Bandit, the pip-audit backed dependency audit, Gitleaks, actionlint, and zizmor.
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md:32:enforced pip-audit gate.
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md:41:`diskcache` is pulled transitively by InSpice when installing the optional
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md:42:`simulation` extra. The default KiCad MCP Pro install does not include it. Until
03_TOOLS\repos\kicad-mcp-pro\SECURITY.md:44:keep cache directories trusted and isolated, especially for remote HTTP servers.
03_TOOLS\repos\kicad-mcp-pro\uv.lock:585:    { name = "python-dotenv" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:1344:    { name = "python-dotenv" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:1394:    { name = "pyyaml-env-tag" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:1745:name = "nodeenv"
03_TOOLS\repos\kicad-mcp-pro\uv.lock:1748:sdist = { url = "https://files.pythonhosted.org/packages/24/bf/d1bda4f6168e0b2e9e5958945e01910052158313224ada5ce1fb2e1113b8/nodeenv-1.10.0.tar.gz", hash = "sha256:996c191ad80897d076bdfba80a41994c2b47c68e224c542b48feba42ba00f8bb", size = 55611, upload-time = "2025-12-20T14:08:54.006Z" }
03_TOOLS\repos\kicad-mcp-pro\uv.lock:1750:    { url = "https://files.pythonhosted.org/packages/88/b2/d0896bdcdc8d28a7fc5717c305f1a861c26e18c05047949fb371034d98bd/nodeenv-1.10.0-py2.py3-none-any.whl", hash = "sha256:5bb13e3eed2923615535339b3c620e76779af4cb4c6a90deccc9e36b274d3827", size = 23438, upload-time = "2025-12-20T14:08:52.782Z" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:1992:    { name = "pyyaml-env-tag" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2154:    { name = "python-dotenv" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2253:    { name = "nodeenv" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2355:name = "python-dotenv"
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2358:sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2360:    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2444:name = "pyyaml-env-tag"
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2450:sdist = { url = "https://files.pythonhosted.org/packages/eb/2e/79c822141bfd05a853236b504869ebc6b70159afc570e1d5a20641782eaa/pyyaml_env_tag-1.1.tar.gz", hash = "sha256:2eb38b75a2d21ee0475d6d97ec19c63287a7e140231e4214969d0eac923cd7ff", size = 5737, upload-time = "2025-05-13T15:24:01.64Z" }
03_TOOLS\repos\kicad-mcp-pro\uv.lock:2452:    { url = "https://files.pythonhosted.org/packages/04/11/432f32f8097b03e3cd5fe57e88efb685d964e2e5178a48ed61e841f7fdce/pyyaml_env_tag-1.1-py3-none-any.whl", hash = "sha256:17109e1a528561e32f026364712fee1264bc2ea6715120891174ed1b980d2e04", size = 4722, upload-time = "2025-05-13T15:23:59.629Z" },
03_TOOLS\repos\kicad-mcp-pro\uv.lock:3143:    { name = "python-dotenv" },
03_TOOLS\repos\kicad-mcp-pro\docs\development.md:5:Install Task from <https://taskfile.dev/installation/>.
03_TOOLS\repos\kicad-mcp-pro\docs\development.md:8:task install
03_TOOLS\repos\kicad-mcp-pro\docs\development.md:45:This command requires Gitleaks, actionlint, and zizmor. It reports clear install
03_TOOLS\repos\kicad-mcp-pro\docs\development.md:58:- `task: command not found`: install Task from the official installation page.
03_TOOLS\repos\kicad-mcp-pro\docs\development.md:59:- Hook setup fails: run `uvx pre-commit install --install-hooks`.
03_TOOLS\repos\kicad-mcp-pro\SUPPORT.md:24:- Include KiCad, Python, MCP client, transport, and install method.
03_TOOLS\repos\kicad-mcp-pro\ROADMAP.md:3:KiCad MCP Pro follows a monthly minor release cadence and keeps roadmap items visible enough for users to plan around them. Dates are targets, not promises.
03_TOOLS\repos\kicad-mcp-pro\ROADMAP.md:20:- Revisit profile names and tool grouping only through an RFC.
03_TOOLS\repos\kicad-mcp-pro\Taskfile.yml:4:  install:
03_TOOLS\repos\kicad-mcp-pro\Taskfile.yml:13:      - uvx pre-commit install --install-hooks
03_TOOLS\repos\kicad-mcp-pro\Taskfile.yml:14:      - uvx pre-commit install --hook-type commit-msg
03_TOOLS\repos\kicad-mcp-pro\Taskfile.yml:15:      - uvx pre-commit install --hook-type pre-push
03_TOOLS\repos\kicad-mcp-pro\Taskfile.yml:23:    desc: Run read-only lint and metadata checks
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md:3:## Which MCP client should I use?
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md:5:Use the client that already fits your workflow. VS Code, Cursor, Claude Desktop, Claude Code, Codex, and generic MCP clients are documented in the client configuration guide.
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md:11:## Why does the server need a project directory?
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md:13:Project-scoped paths let the server keep writes inside the active KiCad project, generate outputs predictably, and avoid accidental edits outside the board workspace.
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md:15:## Why are there profiles?
03_TOOLS\repos\kicad-mcp-pro\docs\faq.md:17:Profiles reduce the tool surface for agents. `pcb_only`, `schematic_only`, `manufacturing`, `analysis`, and `agent_full` help clients expose only the tools needed for a workflow.
03_TOOLS\repos\kicad-mcp-pro\docs\doppler-setup.md:11:The token must be a read-only Doppler service token scoped to project `all`, config `main`.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:3:KiCad MCP Pro works with MCP clients that can start a local `stdio` server or connect to a
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:4:Streamable HTTP endpoint. The most portable setup is local `stdio` with `uvx`.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:7:omit `KICAD_MCP_PROJECT_DIR` and call `kicad_set_project()` from the client instead, but
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:15:command: uvx
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:19:Recommended environment:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:22:KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:23:KICAD_MCP_PROFILE=pcb_only
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:26:Use `KICAD_MCP_PROFILE=full` if you want every tool category. Preferred focused profiles are
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:28:`simulation`, and `analysis`. Legacy aliases `pcb` and `schematic` still work for older
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:33:VS Code uses `.vscode/mcp.json` for workspace-level configuration and a user profile MCP
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:34:configuration for global setup. GitHub Copilot in VS Code uses the same MCP server setup.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:40:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:42:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:43:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:45:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:46:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:47:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:54:Use an absolute KiCad project path for `KICAD_MCP_PROJECT_DIR`. Some VS Code MCP setups do
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:55:not expand `${workspaceFolder}` and may fail at server startup.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:59:Codex stores MCP servers in `~/.codex/config.toml` or a trusted project-scoped
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:60:`.codex/config.toml`.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:65:codex mcp add kicad \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:66:  --env KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:67:  --env KICAD_MCP_PROFILE=pcb_only \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:68:  -- uvx kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:71:`~/.codex/config.toml`:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:74:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:75:command = "uvx"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:80:[mcp_servers.kicad.env]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:81:KICAD_MCP_PROJECT_DIR = "/absolute/path/to/your/kicad-project"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:82:KICAD_MCP_PROFILE = "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:87:Add the server to `claude_desktop_config.json`:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:93:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:95:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:96:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:97:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:106:Use KiCad MCP Pro 3.0.2 or newer for Claude Code `stdio` setups. That release defers
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:107:heavy tool registration until after the MCP `initialize` handshake, avoiding startup races
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:108:on slower WSL or cold KiCad environments.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:116:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:118:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:119:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:120:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:132:  --env KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:133:  --env KICAD_MCP_PROFILE=pcb_only \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:134:  -- uvx kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:146:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:147:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:149:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:150:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:151:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:160:Add the server to `~/.gemini/settings.json`:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:166:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:168:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:169:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:170:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:178:## Antigravity And Other MCP Clients
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:186:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:187:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:189:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:190:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:191:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:198:Client-specific behavior can vary. If the client supports only HTTP servers, use the HTTP
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:203:Start KiCad MCP Pro as an HTTP server:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:219:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:231:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:251:- VS Code MCP configuration: https://code.visualstudio.com/docs/copilot/customization/mcp-servers
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:252:- Codex MCP configuration: https://developers.openai.com/codex/mcp
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:253:- Claude Code MCP configuration: https://docs.anthropic.com/en/docs/claude-code/mcp
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:254:- Anthropic MCP overview: https://docs.anthropic.com/en/docs/mcp
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:255:- Cursor MCP configuration: https://docs.cursor.com/en/context/mcp
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:256:- Gemini CLI MCP setup notes: https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:5:uvx kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:8:## Package install
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:10:pip install kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:15:pip install "kicad-mcp-pro[http]"
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:18:After installation, add the server to your MCP client. See
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:20:Gemini CLI, and generic MCP client examples.
03_TOOLS\repos\kicad-mcp-pro\docs\index.md:1:# KiCad MCP Pro
03_TOOLS\repos\kicad-mcp-pro\docs\index.md:3:KiCad MCP Pro is a project-aware Model Context Protocol server for KiCad PCB and schematic workflows.
03_TOOLS\repos\kicad-mcp-pro\docs\index.md:5:Use the documentation in this folder for installation, client configuration, tool reference, and development notes.
03_TOOLS\repos\kicad-mcp-pro\docs\index.md:9:- [Installation](installation.md)
03_TOOLS\repos\kicad-mcp-pro\docs\autonomy.md:32:Automation does not publish releases or push tags without an explicit manual release workflow invocation and release environment approval.
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\time-domain.md:5:- `route_create_tuning_profile(...)`
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\time-domain.md:6:- `route_list_tuning_profiles()`
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\time-domain.md:7:- `route_apply_tuning_profile(net_pattern, profile_name)`
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\time-domain.md:12:Profile definitions are stored in `.kicad-mcp/tuning_profiles.json`. When a stackup is available, `route_tune_time_domain(...)` derives an effective dielectric constant from the selected layer context and converts delay targets into a computed length target. The resulting delay and length constraints are then written into `.kicad_dru`.
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\time-domain.md:14:If no usable stackup context exists, the helper falls back to the legacy propagation-speed-factor path so mixed KiCad 9/10 environments still get a practical constraint rule.
03_TOOLS\repos\kicad-mcp-pro\docs\api-stability.md:3:KiCad MCP Pro treats public MCP tools, resource URIs, prompt names, server profiles, environment variables, and documented CLI behavior as public API.
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\variants.md:10:- `variant_set_component_override(...)` writes per-component enabled/value/footprint overrides.
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\variants.md:12:- `variant_export_bom(variant, format="csv")` writes a variant-specific BOM under `output/variants/`.
03_TOOLS\repos\kicad-mcp-pro\docs\kicad10\variants.md:19:When no valid `.kicad_pro` file is available, the tools fall back to the historical `.kicad-mcp/variants.json` sidecar so older or fixture-style environments still work safely.
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py:1:"""Audit locked project dependencies without auditing the active venv bootstrap tools."""
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py:38:                "pip",
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py:45:                _executable("uvx"),
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py:47:                "pip-audit==2.10.0",
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py:48:                "pip-audit",
03_TOOLS\repos\kicad-mcp-pro\scripts\audit_dependencies.py:51:                "--disable-pip",
03_TOOLS\repos\kicad-mcp-pro\scripts\hook_pre_commit.py:31:        sys.stderr.write(completed.stderr)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:1:"""Shared test fixtures for KiCad MCP Pro."""
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:20:    """Extract text from a FastMCP tool result."""
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:41:async def call_tool_text(server: object, name: str, arguments: dict[str, object]) -> str:
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:42:    """Call a FastMCP tool and normalize its textual output."""
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:43:    result = await server.call_tool(name, arguments)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:47:async def call_tool_payload(server: object, name: str, arguments: dict[str, object]) -> object:
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:48:    """Call a FastMCP tool and extract structured payloads when available."""
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:49:    result = await server.call_tool(name, arguments)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:58:async def read_resource_text(server: object, uri: str) -> str:
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:59:    """Read an MCP resource and normalize its textual output."""
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:60:    result = await server.read_resource(uri)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:64:async def get_prompt_text(server: object, name: str, arguments: dict[str, object]) -> str:
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:65:    """Read an MCP prompt and normalize the returned text content."""
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:66:    result = await server.get_prompt(name, arguments)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:82:    monkeypatch.delenv("KICAD_MCP_PROJECT_DIR", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:83:    monkeypatch.delenv("KICAD_MCP_PROJECT_FILE", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:84:    monkeypatch.delenv("KICAD_MCP_PCB_FILE", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:85:    monkeypatch.delenv("KICAD_MCP_SCH_FILE", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:86:    monkeypatch.delenv("KICAD_MCP_OUTPUT_DIR", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:87:    monkeypatch.delenv("KICAD_MCP_SYMBOL_LIBRARY_DIR", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:88:    monkeypatch.delenv("KICAD_MCP_FOOTPRINT_LIBRARY_DIR", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:89:    monkeypatch.delenv("KICAD_MCP_KICAD_CLI", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:90:    monkeypatch.delenv("KICAD_CLI_PATH", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:91:    monkeypatch.delenv("KICAD_API_TOKEN", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:92:    monkeypatch.delenv("KICAD_MCP_TIMEOUT_MS", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:93:    monkeypatch.delenv("KICAD_MCP_RETRIES", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:94:    monkeypatch.delenv("KICAD_MCP_HEADLESS", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:95:    monkeypatch.delenv("KICAD_MCP_WORKSPACE_ROOT", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:96:    monkeypatch.delenv("KICAD_MCP_TRANSPORT", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:97:    monkeypatch.delenv("KICAD_MCP_LEGACY_SSE", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:98:    monkeypatch.delenv("KICAD_MCP_STATEFUL_HTTP", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:99:    monkeypatch.delenv("KICAD_MCP_ENABLE_METRICS", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:100:    monkeypatch.delenv("KICAD_MCP_CORS_ORIGINS", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:101:    monkeypatch.delenv("KICAD_MCP_AUTH_TOKEN", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:102:    monkeypatch.delenv("KICAD_MCP_HOST", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:103:    monkeypatch.delenv("KICAD_MCP_PORT", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:104:    monkeypatch.delenv("KICAD_MCP_LOG_LEVEL", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:105:    monkeypatch.delenv("KICAD_MCP_LOG_FORMAT", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:106:    monkeypatch.delenv("KICAD_MCP_PROFILE", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:107:    monkeypatch.delenv("KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:114:    cli.write_text("#!/bin/sh\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:116:    monkeypatch.setenv("KICAD_MCP_KICAD_CLI", str(cli))
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:126:    (project_dir / "demo.kicad_pro").write_text('{"meta": {"version": 1}}', encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:127:    (project_dir / "demo.kicad_pcb").write_text("(kicad_pcb)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:128:    (project_dir / "demo.kicad_dru").write_text("(rules)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:129:    (project_dir / "demo.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:148:    (symbols_dir / "Device.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:165:    (symbols_dir / "power.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:183:    (symbols_dir / "Extended.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:202:    (symbols_dir / "MultiUnit.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:238:    (resistor_lib / "R_0805.kicad_mod").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:261:    (resistor_lib / "R_1206.kicad_mod").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:285:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(project_dir))
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:286:    monkeypatch.setenv("KICAD_MCP_SYMBOL_LIBRARY_DIR", str(symbols_dir))
03_TOOLS\repos\kicad-mcp-pro\tests\conftest.py:287:    monkeypatch.setenv("KICAD_MCP_FOOTPRINT_LIBRARY_DIR", str(footprints_dir))
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py:20:    parser = argparse.ArgumentParser(description="Bump KiCad MCP Pro release metadata.")
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py:45:    path.write_text(updated, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py:56:    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py:77:    path.write_text(updated, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py:98:    update_json(ROOT / "server.json", version)
03_TOOLS\repos\kicad-mcp-pro\scripts\bump_version.py:105:    print(f"Bumped KiCad MCP Pro to {version}")
03_TOOLS\repos\kicad-mcp-pro\scripts\publish.sh:1:#!/usr/bin/env bash
03_TOOLS\repos\kicad-mcp-pro\scripts\publish.sh:2:set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\scripts\publish.sh:6:python -m pip install --upgrade twine
03_TOOLS\repos\kicad-mcp-pro\scripts\repo-cleanup.sh:1:#!/usr/bin/env bash
03_TOOLS\repos\kicad-mcp-pro\scripts\repo-cleanup.sh:3:set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:1:"""Configuration for KiCad MCP Pro."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:43:class KiCadMCPConfig(BaseSettings):
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:44:    """All server configuration in one place."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:47:        env_prefix="KICAD_MCP_",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:48:        env_file=".env",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:49:        env_file_encoding="utf-8",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:77:    transport: Literal["stdio", "http", "sse", "streamable-http"] = Field(default="stdio")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:87:    profile: Literal[
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:99:        "analysis",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:121:        env_settings: PydanticBaseSettingsSource,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:122:        dotenv_settings: PydanticBaseSettingsSource,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:127:            env_settings,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:128:            dotenv_settings,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:135:    def _apply_env_aliases(cls, values: object) -> object:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:136:        """Apply interoperability aliases that do not fit the KICAD_MCP_ prefix."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:141:            "kicad_token": ("KICAD_API_TOKEN", "KICAD_MCP_KICAD_TOKEN"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:142:            "kicad_cli": ("KICAD_CLI_PATH", "KICAD_MCP_KICAD_CLI"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:143:            "workspace_root": ("KICAD_MCP_WORKSPACE_ROOT",),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:144:            "ipc_retries": ("KICAD_MCP_RETRIES",),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:145:            "headless": ("KICAD_MCP_HEADLESS",),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:148:        for field_name, env_names in aliases.items():
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:151:            for env_name in env_names:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:152:                raw = os.environ.get(env_name)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:161:            timeout_ms = os.environ.get("KICAD_MCP_TIMEOUT_MS")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:209:                    "KICAD_MCP_CORS_ORIGINS cannot contain '*'. "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:215:                    "KICAD_MCP_CORS_ORIGINS entries must be fully qualified "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:237:    @field_validator("log_format", "profile", mode="before")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:251:                    "until KICAD_MCP_KICAD_CLI points to a valid executable."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:258:    def resolve_paths(self) -> KiCadMCPConfig:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:378:        """Return sanitized config values for health and doctor output."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:395:_config: KiCadMCPConfig | None = None
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:398:def get_config() -> KiCadMCPConfig:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\config.py:403:            _config = KiCadMCPConfig()
03_TOOLS\repos\kicad-mcp-pro\scripts\security_local.py:13:    "zizmor": "Install zizmor with `uv tool install zizmor`.",
03_TOOLS\repos\kicad-mcp-pro\scripts\sync-remotes.ps1:7:$pushTags = if ($env:PUSH_TAGS) { $env:PUSH_TAGS } else { "true" }
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:4:server through the public CLI and MCP surfaces instead of importing Python
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:10:uvx kicad-mcp-pro --help
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:11:uvx kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:12:uvx kicad-mcp-pro doctor --json
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:13:uvx kicad-mcp-pro serve
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:16:`health --json` must succeed when the package is installed, even if KiCad is not
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:17:running. `doctor --json` may report degraded KiCad IPC status but should not
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:28:- `mcp.profile`
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:47:| 0.x-2.6.x | >=3.0,<4.0 | Initial CLI health/doctor contract |
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:52:KICAD_MCP_TRANSPORT=http
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:53:KICAD_MCP_HOST=127.0.0.1
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:54:KICAD_MCP_PORT=27185
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:55:KICAD_MCP_CORS_ORIGINS=vscode-webview://kicad-studio
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:56:KICAD_MCP_AUTH_TOKEN=replace-with-local-token
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:57:KICAD_MCP_STUDIO_WATCH_DIR=/absolute/path/to/projects
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:58:KICAD_MCP_WORKSPACE_ROOT=/absolute/path/to/projects
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:59:KICAD_MCP_PROFILE=full
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:62:`27185` is the recommended Studio bridge port for local setups. The server still defaults to `3334`, so set the port explicitly if you want this convention.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:70:This starts the primary MCP endpoint at `http://127.0.0.1:27185/mcp`.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:71:`/.well-known/mcp-server` reports the same endpoint for discovery. Legacy SSE
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:73:`http://127.0.0.1:27185/sse` must start the server with
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:74:`KICAD_MCP_LEGACY_SSE=true` and enable their own legacy fallback setting.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:78:- `studio_push_context()` pushes active file, DRC errors, selected net/reference, and cursor state into the server.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:80:- `KICAD_MCP_STUDIO_WATCH_DIR` watches for `.kicad_pro` updates and auto-selects the active project.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\kicad-studio.md:81:- `KICAD_MCP_WORKSPACE_ROOT` constrains project artifact reads and writes for safe extension-driven operation.
03_TOOLS\repos\kicad-mcp-pro\scripts\workflow_security.py:24:            "`uv tool install zizmor` or see https://docs.zizmor.sh/installation/.",
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:9:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:43:    def run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:56:            analysis="ac",
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:129:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:130:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:133:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:138:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:161:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:166:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:170:    package = await call_tool_text(server, "export_manufacturing_package", {})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:185:    server = build_server("high_speed")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:186:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:189:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:194:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:213:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:224:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:235:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:252:    server = build_server("power")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:253:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:256:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:261:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:265:    sheets = await call_tool_text(server, "sch_list_sheets", {})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:266:    info = await call_tool_text(server, "sch_get_sheet_info", {"sheet_name": "buck_5v"})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:268:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:273:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:297:    netlist.write_text("* rf\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:299:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:300:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:303:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:308:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:313:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:318:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:319:        "sim_run_ac_analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:332:    assert "AC analysis" in ac
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:341:    server = build_server("analysis")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:342:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:345:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:350:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:355:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_professional_workflows.py:360:    assert "Differential-pair skew analysis" in skew
03_TOOLS\repos\kicad-mcp-pro\scripts\sync-remotes.sh:1:#!/usr/bin/env bash
03_TOOLS\repos\kicad-mcp-pro\scripts\sync-remotes.sh:2:set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:14:def test_stdio_initialize_does_not_require_client_warmup() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:15:    env = {key: value for key, value in os.environ.items() if not key.startswith("KICAD_MCP_")}
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:16:    env["KICAD_MCP_LOG_LEVEL"] = "ERROR"
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:17:    env["KICAD_MCP_LOG_FORMAT"] = "json"
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:18:    env["KICAD_MCP_KICAD_CLI"] = "kicad-cli-missing-for-stdio-startup-test"
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:19:    env["KICAD_MCP_TRANSPORT"] = "stdio"
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:23:        [sys.executable, "-m", "kicad_mcp.server", "--profile", "full"],
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:28:        env=env,
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:47:            "clientInfo": {"name": "stdio-startup-test", "version": "0"},
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:50:    process.stdin.write(json.dumps(initialize) + "\n")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:57:        process.stdin.write(json.dumps(initialized) + "\n")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:58:        process.stdin.write(
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_stdio_startup.py:72:    assert "serverInfo" in payload["result"]
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\schematic_backend_capability_matrix.json:110:    "notes": "Power-flag analysis can be derived from ERC/validation output, but there is no direct one-shot helper."
03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\schematic_backend_capability_matrix.json:185:    "notes": "Connectivity summaries are composed from verified wire and component helpers to match the existing textual MCP surface."
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:9:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:112:                output_path.write_text("ref,value\nR1,10k\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:114:                output_path.write_text("generated\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:119:                (output_path / "board_F_Cu.gbr").write_text("G04*\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:121:                (output_path / "board.drl").write_text("M48\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:189:                summary="Copper-to-edge clearance violates the active DFM profile.",
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:207:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:208:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:210:    gate = await call_tool_text(server, "project_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:211:    release = await call_tool_text(server, "export_manufacturing_package", {})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:235:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:236:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:238:    gate = await call_tool_text(server, "project_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_release_gates.py:239:    release = await call_tool_text(server, "export_manufacturing_package", {})
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json:2:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json:4:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json:5:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json:9:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json:10:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode.mcp.json:11:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\scripts\verify_doppler_secrets.sh:1:#!/usr/bin/env bash
03_TOOLS\repos\kicad-mcp-pro\scripts\verify_doppler_secrets.sh:2:set -euo pipefail
03_TOOLS\repos\kicad-mcp-pro\docs\integration\cursor.md:5:- Stdio: `uvx kicad-mcp-pro`
03_TOOLS\repos\kicad-mcp-pro\docs\integration\cursor.md:8:For larger tool surfaces, it is often helpful to set `KICAD_MCP_PROFILE=pcb_only`, `schematic_only`, or `high_speed`.
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:22:standard local profile.
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:34:- `sim_run_ac_analysis`
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:40:The default backend is direct `ngspice` CLI execution. If `InSpice` is installed
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:41:manually in the runtime environment, the server can still use it as an optional
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:92:v2 adds bundled manufacturer profiles and dedicated DFM tools:
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:94:- `dfm_load_manufacturer_profile`
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:98:The initial bundled profiles target:
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:106:through the same bundled profile engine so manufacturing checks and cost
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:111:v2 expands the PCB write category with first-layout helpers:
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:137:`pcb_set_stackup` writes a file-backed stackup profile and updates the board
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:162:v2 broadens the recommended server profiles:
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:172:- `analysis`
03_TOOLS\repos\kicad-mcp-pro\docs\development\v2-migration.md:175:config examples should prefer the explicit `*_only` profile names.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\__init__.py:1:"""KiCad MCP Pro package."""
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\manufacturing-export.md:8:6. If you need low-level debug or interchange artifacts, switch to a broader profile
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:5:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:9:async def test_server_registers_tools_resources_and_prompts(sample_project, mock_board) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:10:    server = build_server("minimal")
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:11:    tool_names = {tool.name for tool in await server.list_tools()}
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:12:    resource_uris = {str(resource.uri) for resource in await server.list_resources()}
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:13:    prompt_names = {prompt.name for prompt in await server.list_prompts()}
03_TOOLS\repos\kicad-mcp-pro\tests\e2e\test_server.py:15:        template.uriTemplate for template in await server.list_resource_templates()
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:1:"""Synchronize MCP registry metadata from pyproject.toml."""
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:15:MCP_JSON = ROOT / "mcp.json"
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:16:SERVER_JSON = ROOT / "server.json"
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:55:        "Compatibility metadata for KiCad MCP Pro. Prefer server.json for official MCP "
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:65:def _updated_server_json(metadata: dict[str, Any], original: dict[str, Any]) -> dict[str, Any]:
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:84:        MCP_JSON: _dump_json(_updated_mcp_json(metadata, _load_json(MCP_JSON))),
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:85:        SERVER_JSON: _dump_json(_updated_server_json(metadata, _load_json(SERVER_JSON))),
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:93:    mode.add_argument("--write", action="store_true", help="Update generated metadata files.")
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:105:            if args.write:
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:106:                path.write_text(rendered, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:110:        print(f"MCP metadata is out of sync: {rel}", file=sys.stderr)
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:114:    if args.write:
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:117:                "Updated MCP metadata: " + ", ".join(str(path.relative_to(ROOT)) for path in drift)
03_TOOLS\repos\kicad-mcp-pro\scripts\sync_mcp_metadata.py:120:            print("MCP metadata already synchronized.")
03_TOOLS\repos\kicad-mcp-pro\scripts\verify_doppler_secrets.ps1:3:$project = if ($env:DOPPLER_PROJECT) { $env:DOPPLER_PROJECT } else { "all" }
03_TOOLS\repos\kicad-mcp-pro\scripts\verify_doppler_secrets.ps1:4:$config = if ($env:DOPPLER_CONFIG) { $env:DOPPLER_CONFIG } else { "main" }
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\vscode-http.mcp.json:2:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\discovery.py:1:"""KiCad installation and project discovery helpers."""
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-desktop.md:3:Claude Desktop can use either stdio or streamable HTTP.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-desktop.md:11:If you want a local bridge, start the server first:
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-desktop.md:17:Then point the client at `http://127.0.0.1:3334/mcp`, or at your custom port if you override `KICAD_MCP_PORT`. If you want the same port convention as KiCad Studio, use `27185`.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:13:    available_profiles,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:20:    """Return server discovery metadata for ``/.well-known/mcp-server``."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:23:    transport_type = "stdio" if cfg.transport == "stdio" else "streamable-http"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:25:    if transport_type != "stdio":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:29:        "$schema": "https://static.modelcontextprotocol.io/schemas/mcp-server-card/v1.json",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:32:        "serverInfo": {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:34:            "title": "KiCad MCP Pro",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:53:            "profiles": {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:54:                profile: list(PROFILE_CATEGORIES[profile]) for profile in available_profiles()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\wellknown.py:60:        "profiles": available_profiles(),
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\high-speed-review.md:3:This workflow uses only MCP tools and headless-safe checks where possible. It is
03_TOOLS\repos\kicad-mcp-pro\docs\workflows\high-speed-review.md:80:tool accepts both the legacy `power_w` mode and the package-envelope mode:
03_TOOLS\repos\kicad-mcp-pro\docs\development\architecture.md:8:- `tools/` for domain-specific MCP tools
03_TOOLS\repos\kicad-mcp-pro\docs\development\architecture.md:9:- `resources/` and `prompts/` for MCP-native context surfaces
03_TOOLS\repos\kicad-mcp-pro\docs\development\architecture.md:20:     sensor clusters, RF keepouts, critical nets, and fab profile hints
03_TOOLS\repos\kicad-mcp-pro\docs\development\architecture.md:48:The MCP resource layer exposes the current review state as text-first surfaces:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:1:"""Health and doctor diagnostics for CLI and integrations."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:45:    """MCP server runtime settings."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:48:    profile: str
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:62:    """Sanitized server configuration fields."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:78:    """Machine-readable health/doctor report."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:133:                hint="Install KiCad or set KICAD_CLI_PATH/KICAD_MCP_KICAD_CLI.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:155:                    hint="Start KiCad, enable the IPC API server, and open a board.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:163:                message="KiCad IPC probe deferred for fast health check.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:164:                hint="Run doctor --json for a deeper probe.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:173:        mcp=McpDiagnostics(transport_default=cfg.transport, profile=cfg.profile),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:186:def build_health_report() -> DiagnosticReport:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:187:    """Build a fast health report that never requires KiCad IPC."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:191:def build_doctor_report() -> DiagnosticReport:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\diagnostics.py:192:    """Build a deeper doctor report with non-fatal KiCad probes."""
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\generic-mcp-client.json:4:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\generic-mcp-client.json:5:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\generic-mcp-client.json:7:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\generic-mcp-client.json:8:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\generic-mcp-client.json:9:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:3:The simplest Claude Code setup uses `stdio`. For longer-lived multi-client setups, prefer streamable HTTP.
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:5:KiCad MCP Pro 3.0.2 and newer defer heavy tool registration in `stdio` mode so Claude
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:6:Code can send `initialize` immediately after spawning the server. If Claude Code reports
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:10:pipx upgrade kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:11:# or, for uv tool installs:
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:17:- Local single-user session: `stdio`
03_TOOLS\repos\kicad-mcp-pro\docs\integration\claude-code.md:19:- If you need local auth, set `KICAD_MCP_AUTH_TOKEN`
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:1:"""Typed error model for KiCad MCP Pro."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:18:    """Base class for stable KiCad MCP domain errors."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:20:    code = "KICAD_MCP_ERROR"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:37:    code = "KICAD_NOT_RUNNING"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:38:    hint = "Start KiCad and enable the IPC API server, or run doctor for diagnostics."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:45:    code = "KICAD_CONNECTION_TIMEOUT"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:46:    hint = "Increase KICAD_MCP_TIMEOUT_MS or verify that the KiCad IPC API is responding."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:53:    code = "KICAD_VERSION_MISMATCH"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:61:    code = "KICAD_PROJECT_NOT_FOUND"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:62:    hint = "Set KICAD_MCP_PROJECT_DIR or call kicad_set_project() with an existing project."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:69:    code = "KICAD_BOARD_NOT_OPEN"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:78:    hint = "Use a relative path inside KICAD_MCP_WORKSPACE_ROOT or the active project."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\errors.py:105:        "hint": "Run doctor for diagnostics and retry with corrected configuration.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\kicad\session.py:164:                "the IPC API server is enabled."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\simulation.py:16:    """Operating-point analysis parameters."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\simulation.py:20:    """Small-signal AC analysis parameters."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\simulation.py:28:    """Transient analysis parameters."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\simulation.py:35:    """DC sweep analysis parameters."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\simulation.py:55:    """Persisted MCP simulation directive parameters."""
03_TOOLS\repos\kicad-mcp-pro\docs\workflow-security.md:7:  job-scoped permissions and explicit repository or environment guards.
03_TOOLS\repos\kicad-mcp-pro\docs\workflow-security.md:16:- Shell steps must pass GitHub expression values through `env:` before using
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\dfm_profiles\__init__.py:1:"""Bundled manufacturer DFM profiles."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\pcb.py:240:    name: str = Field(default="MCP_Keepout", min_length=1, max_length=100)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\signal_integrity.py:1:"""Pydantic models for signal-integrity calculations and board analysis."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\signal_integrity.py:45:    """Differential-pair skew analysis request."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\signal_integrity.py:71:    """Via-stub analysis request."""
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\gemini-settings.json:4:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\gemini-settings.json:6:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\gemini-settings.json:7:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\gemini-settings.json:8:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_schema.py:6:def test_wellknown_payload_contains_required_server_card_fields() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_schema.py:11:        == "https://static.modelcontextprotocol.io/schemas/mcp-server-card/v1.json"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_schema.py:15:    assert payload["serverInfo"]["title"] == "KiCad MCP Pro"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_schema.py:16:    assert payload["transport"]["type"] in {"stdio", "streamable-http"}
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_schema.py:22:    assert "profiles" in payload["capabilities"]
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\security.md:5:- Enable bearer-token protection with `KICAD_MCP_AUTH_TOKEN`.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\security.md:6:- Limit `KICAD_MCP_CORS_ORIGINS` to only the origins you actually need.
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:5:Set `KICAD_MCP_KICAD_CLI` to the absolute path of `kicad-cli`.
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:21:Open KiCad and enable the IPC API server:
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:28:KICAD_MCP_KICAD_SOCKET_PATH=/path/to/socket
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:29:KICAD_MCP_KICAD_TOKEN=token
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:37:KICAD_MCP_PROJECT_DIR=/absolute/path/to/project
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:42:When a directory contains both `<directory>.kicad_pro` and sync-conflict duplicates such as `<directory> 2.kicad_pro`, the server prefers the canonical basename match and ignores numbered duplicates during automatic discovery. `kicad_set_project()` echoes the resolved project file in its response.
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:46:Some KiCad IPC and CLI operations can fail while the GUI is modal, saving, or actively editing. The server retries transient busy responses, then returns an actionable message if KiCad still cannot respond. Close modal dialogs, finish the current drag/edit operation, save the file, and retry the tool.
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:58:Use absolute paths and avoid relying on client-side expansion such as `${workspaceFolder}` unless your MCP client documents support for it.
03_TOOLS\repos\kicad-mcp-pro\docs\troubleshooting.md:72:Check `KICAD_MCP_HOST`, `KICAD_MCP_PORT`, `KICAD_MCP_AUTH_TOKEN`, and `KICAD_MCP_CORS_ORIGINS`. For local-only Studio bridge deployments, port `27185` is a good convention; the default server port is `3334`.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py:5:compliance targets, cost budgets, and thermal envelopes.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py:27:    Used by placement analysis (minimum trace width) and PDN checks
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py:167:    Consumed by placement analysis to enforce connector edge positions,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py:168:    mount-hole clearances, and height envelopes.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py:254:# Thermal envelope
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\intent.py:261:    """Thermal operating environment for heat-path and via-count recommendations."""
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\repository-topology.md:52:GitHub organization workflows, Azure DevOps, and GitLab all use the same pattern: install the Doppler CLI, then execute sensitive commands through `doppler run -- ...` so Doppler injects secrets as environment variables at runtime.
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:9:from kicad_mcp.server import build_server, create_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:14:def test_wellknown_metadata_matches_server_card_shape() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:16:    assert metadata["$schema"].endswith("/mcp-server-card/v1.json")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:17:    assert metadata["serverInfo"]["name"] == "kicad-mcp-pro"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:19:    assert "full" in metadata["profiles"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:24:    monkeypatch.setenv("KICAD_MCP_TRANSPORT", "http")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:25:    monkeypatch.setenv("KICAD_MCP_HOST", "127.0.0.1")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:26:    monkeypatch.setenv("KICAD_MCP_PORT", "3334")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:27:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:28:    client = TestClient(server.streamable_http_app())
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:30:    dotted = client.get("/.well-known/mcp-server")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:31:    compat = client.get("/well-known/mcp-server")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:47:        for route in build_server("minimal").streamable_http_app().routes
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:56:        for route in build_server("minimal").streamable_http_app().routes
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:66:    monkeypatch.setenv("KICAD_MCP_TRANSPORT", "http")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:67:    monkeypatch.setenv("KICAD_MCP_ENABLE_METRICS", "true")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:68:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:69:    client = TestClient(server.streamable_http_app())
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:80:    server = create_server()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:84:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_wellknown_and_studio.py:94:    resource_items = list(await server.read_resource("kicad://studio/context"))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\connection.py:46:            "  KICAD_MCP_KICAD_SOCKET_PATH\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\connection.py:47:            "  KICAD_MCP_KICAD_TOKEN"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\connection.py:78:                "server at the expected project files."
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\cursor.mcp.json:4:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\cursor.mcp.json:5:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\cursor.mcp.json:7:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\cursor.mcp.json:8:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\cursor.mcp.json:9:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\__init__.py:1:"""Utility helpers for KiCad MCP Pro."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\studio_context.py:10:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\studio_context.py:34:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\docs\tools-reference.md:29:The `manufacturing` profile keeps its export surface narrow: use `get_board_stats()`
03_TOOLS\repos\kicad-mcp-pro\docs\tools-reference.md:31:tools remain available in broader profiles such as `full` and `minimal` for debugging
03_TOOLS\repos\kicad-mcp-pro\docs\tools-reference.md:94:Tool execution failures are returned as MCP tool errors with `isError: true` and
03_TOOLS\repos\kicad-mcp-pro\docs\tools-reference.md:100:The MCP resource surface mirrors the current review state so an agent can iterate safely:
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:3:The server can run in `streamable-http` mode in addition to `stdio`.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:7:- MCP endpoint: `/mcp`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:8:- Discovery endpoint: `/.well-known/mcp-server`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:10:- Optional `/metrics` endpoint when `KICAD_MCP_ENABLE_METRICS=true`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:14:- Legacy `/sse` and `/messages` routes stay disabled unless `KICAD_MCP_LEGACY_SSE=true`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:20:- `KICAD_MCP_TRANSPORT=http`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:21:- `KICAD_MCP_HOST=127.0.0.1`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:22:- `KICAD_MCP_PORT=3334`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:23:- `KICAD_MCP_CORS_ORIGINS=https://app.example.com,http://127.0.0.1:3334`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:24:- `KICAD_MCP_AUTH_TOKEN=...`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:25:- `KICAD_MCP_STATEFUL_HTTP=true`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:26:- `KICAD_MCP_ENABLE_METRICS=true`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:27:- `KICAD_MCP_LEGACY_SSE=true`
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:31:- `GET /.well-known/mcp-server` returns the server card plus `capabilities.toolCategories`,
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:32:  `capabilities.profiles`, and `capabilities.experimentalTools` so clients can negotiate a
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:33:  profile before listing tools.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:36:- `POST /.well-known/mcp-server/token-rotate` rotates the in-memory bearer token. The request
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:41:- When bearer auth is enabled, cross-origin `POST /mcp` requests are checked against `KICAD_MCP_CORS_ORIGINS`.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:42:- If you run over `stdio`, `KICAD_MCP_AUTH_TOKEN` is ignored and a startup warning is emitted.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\http-mode.md:44:- Token rotation is intentionally in-memory; update your environment or TOML config separately for persistence.
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_version_control_helpers.py:13:class FakeMCP:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_version_control_helpers.py:106:    pcb_file.write_text("board", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_version_control_helpers.py:148:    mcp = FakeMCP()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_version_control_helpers.py:171:        lambda _root: ["user.name=KiCad MCP Pro"],
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_version_control_helpers.py:253:    assert "No KiCad MCP checkpoints were found" in vcs_list_checkpoints()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\models\component_contracts.py:171:            "Amplifier_Operational:MCP6002",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:1:"""MCP resources exposing live KiCad state."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:11:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:189:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:331:        from ..tools.validation import _format_placement_score, _placement_analysis
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:334:            analysis, blocked = _placement_analysis()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:343:            if analysis is None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:344:                return "Placement score: BLOCKED\n- Placement analysis returned no data."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\board_state.py:345:            return _format_placement_score(analysis)
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-http-config.toml:1:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\resources\gate_history.py:53:                    f"Gate history schema version {version} is newer than this server supports."
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:19:    project_file.write_text("{broken", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:27:    project_file.write_text('["not-an-object"]', encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:39:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(sample_project))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:40:    monkeypatch.setenv("KICAD_MCP_SCH_FILE", str(sample_project / "demo.kicad_sch"))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:58:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(sample_project))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:59:    monkeypatch.setenv("KICAD_MCP_PROJECT_FILE", str(project_file))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:60:    monkeypatch.setenv("KICAD_MCP_SCH_FILE", str(sample_project / "demo.kicad_sch"))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:61:    project_file.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:86:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(sample_project))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:87:    monkeypatch.setenv("KICAD_MCP_PROJECT_FILE", str(project_file))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:88:    monkeypatch.setenv("KICAD_MCP_SCH_FILE", str(sample_project / "demo.kicad_sch"))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:89:    project_file.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:111:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(sample_project))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_helpers.py:112:    monkeypatch.setenv("KICAD_MCP_SCH_FILE", str(sample_project / "demo.kicad_sch"))
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:1:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:2:command = "uvx"
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:7:[mcp_servers.kicad.env]
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:8:KICAD_MCP_PROJECT_DIR = "/absolute/path/to/your/kicad-project"
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:9:KICAD_MCP_PROFILE = "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\LiPo_charger.yaml:3:description: MCP73831 single-cell LiPo charger with status LED.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\LiPo_charger.yaml:6:    value: MCP73831
03_TOOLS\repos\kicad-mcp-pro\docs\security\threat-model.md:3:KiCad MCP Pro runs local automation against KiCad projects. The main risks are filesystem access, untrusted MCP clients, supply-chain compromise, and release artifact integrity.
03_TOOLS\repos\kicad-mcp-pro\docs\security\threat-model.md:8:- MCP clients are not automatically trusted; use the smallest practical profile.
03_TOOLS\repos\kicad-mcp-pro\docs\security\threat-model.md:14:- A client asks the server to read or write unexpected paths.
03_TOOLS\repos\kicad-mcp-pro\docs\security\threat-model.md:21:- Project path resolution keeps normal writes inside the active project.
03_TOOLS\repos\kicad-mcp-pro\docs\security\threat-model.md:23:- Dependabot, CodeQL, Gitleaks, Scorecard, Trivy, Hadolint, Bandit, pip-audit, and Safety cover the main automated scan layers.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:9:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:16:_CHECKPOINT_TRAILER = "KiCad-MCP-Checkpoint: true"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:17:_DEFAULT_GIT_NAME = "KiCad MCP Pro"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:98:    gitignore.write_text(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:182:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:256:        """List checkpoint commits created by the MCP tool."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\version_control.py:265:            return "No KiCad MCP checkpoints were found for the active project."
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md:10:  -e KICAD_MCP_TRANSPORT=http \
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md:11:  -e KICAD_MCP_PORT=27185 \
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md:12:  -e KICAD_MCP_HOST=0.0.0.0 \
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md:16:For production-style deployments, set `KICAD_MCP_AUTH_TOKEN` and keep `KICAD_MCP_CORS_ORIGINS` narrowly scoped.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md:30:  --build-arg KICAD_APPIMAGE_URL="https://downloads.kicad.org/path/to/KiCad-10.x-x86_64.AppImage" \
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\docker.md:44:network isolation, and read/write project volume boundaries.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:36:    analysis: SimulationKind
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:96:    """Create a simulation-ready copy of a SPICE deck with optional MCP directives."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:102:        prepared.write_text(content, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:107:    merged = f"{trimmed}\n* Added by KiCad MCP Pro simulation tools\n{directive_block}\n.end\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:109:    prepared.write_text(merged, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:246:                "KICAD_MCP_NGSPICE_CLI to a valid executable."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:256:        """Run an operating-point analysis."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:259:    def run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:269:        """Run a small-signal AC analysis."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:280:    def run_transient_analysis(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:289:        """Run a transient analysis."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:310:        """Run a DC sweep analysis."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:324:        analysis: SimulationKind,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:335:                    analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:343:                    analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:347:        return self._run_cli(analysis, netlist_path, output_dir, probe_nets, **kwargs)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:352:        analysis: SimulationKind,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:370:        if analysis == "operating-point":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:371:            analysis_obj = simulation.operating_point(**call_kwargs)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:372:        elif analysis == "ac":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:373:            analysis_obj = simulation.ac(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:380:        elif analysis == "transient":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:381:            analysis_obj = simulation.transient(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:386:        elif analysis == "dc":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:387:            analysis_obj = simulation.dc(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:398:            raise ValueError(f"Unsupported simulation analysis '{analysis}'.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:400:        return self._result_from_inspice(analysis, netlist_path, analysis_obj)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:404:        analysis: SimulationKind,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:406:        analysis_obj: object,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:408:        if analysis == "operating-point":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:409:            op_analysis = cast(_OperatingPointLike, analysis_obj)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:412:                for name, waveform in sorted(op_analysis.nodes.items())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:416:                for name, waveform in sorted(op_analysis.branches.items())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:420:                analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:425:        if analysis == "ac":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:426:            ac_analysis = cast(_AcAnalysisLike, analysis_obj)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:428:            for name, waveform in sorted(ac_analysis.nodes.items()):
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:442:                analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:445:                x_values=_as_real_list(ac_analysis.frequency),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:449:        if analysis == "transient":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:450:            transient_analysis = cast(_TransientAnalysisLike, analysis_obj)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:453:                for name, waveform in sorted(transient_analysis.nodes.items())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:457:                analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:460:                x_values=_as_real_list(transient_analysis.time),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:464:        dc_analysis = cast(_DcAnalysisLike, analysis_obj)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:467:            for name, waveform in sorted(dc_analysis.nodes.items())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:471:            analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:474:            x_values=_as_real_list(dc_analysis.sweep),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:480:        analysis: SimulationKind,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:488:        data_path = output_dir / f"{analysis.replace('-', '_')}.data"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:489:        raw_path = output_dir / f"{analysis.replace('-', '_')}.raw"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:490:        log_path = output_dir / f"{analysis.replace('-', '_')}.log"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:491:        deck_path = output_dir / f"{analysis.replace('-', '_')}.cir"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:493:            analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:500:        deck_path.write_text(deck_text, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:513:            raise RuntimeError(f"ngspice {analysis} analysis failed: {detail}")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:517:            analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:528:        analysis: SimulationKind,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:537:        if analysis == "operating-point":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:539:            analysis_cmd = "op"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:540:        elif analysis == "ac":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:544:            analysis_cmd = (
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:548:        elif analysis == "transient":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:550:            analysis_cmd = f"tran {float(kwargs['step_time_s'])} {float(kwargs['stop_time_s'])}"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:551:        elif analysis == "dc":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:557:            analysis_cmd = (
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:562:            raise ValueError(f"Unsupported simulation analysis '{analysis}'.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:573:            f"{analysis_cmd}\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:574:            f'write "{raw_path}" all\n'
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:583:        analysis: SimulationKind,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:591:        if analysis == "operating-point":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:599:                analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:607:        if analysis == "ac":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:626:                analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:636:        x_label = "time" if analysis == "transient" else "sweep"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\ngspice.py:655:            analysis=analysis,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:8:from kicad_mcp.server import create_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:13:def _write_variant_schematic(sample_project) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:15:    schematic.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:37:    _write_variant_schematic(sample_project)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:38:    server = create_server()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:40:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:41:    await call_tool_text(server, "variant_create", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:43:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:47:    await call_tool_text(server, "variant_set_active", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:49:    listing = json.loads(await call_tool_text(server, "variant_list", {}))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:55:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:62:    exported = await call_tool_text(server, "variant_export_bom", {"variant": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:73:    _write_variant_schematic(sample_project)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:74:    server = create_server()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:76:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:77:    await call_tool_text(server, "variant_create", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:79:    empty_error = await call_tool_text(server, "variant_create", {"name": "   "})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:80:    duplicate_error = await call_tool_text(server, "variant_create", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:82:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:92:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:104:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:110:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_variant_diff.py:123:        server,
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-desktop.json:4:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-desktop.json:6:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-desktop.json:7:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-desktop.json:8:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1:"""KiCad MCP Pro server entrypoint."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:25:from mcp.server.auth.provider import AccessToken
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:26:from mcp.server.auth.settings import AuthSettings
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:27:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:28:from mcp.server.fastmcp.exceptions import ToolError
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:29:from mcp.server.lowlevel.helper_types import ReadResourceContents
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:40:from .config import KiCadMCPConfig, get_config, reset_config
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:42:from .diagnostics import DiagnosticReport, build_doctor_report, build_health_report
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:47:from .tools.router import EXPERIMENTAL_TOOL_NAMES, available_profiles, categories_for_profile
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:52:app = typer.Typer(help="KiCad MCP Pro server for PCB and schematic workflows.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:58:        """Start deferred MCP surface registration."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:194:        return "Call kicad_set_project() or set the relevant KICAD_MCP_*_FILE variable."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:196:        return "Install KiCad or set KICAD_MCP_KICAD_CLI to the kicad-cli executable."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:286:    if get_config().transport == "stdio":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:301:    def __init__(self, server: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:302:        self._server = server
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:309:            return asyncio.run(self._server.list_tools())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:310:        sync_list = getattr(self._server, "list_tools_sync", None)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:320:                result = list(asyncio.run(self._server.list_tools()))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:332:        return getattr(self._server, name)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:347:        """Replace the accepted bearer token without restarting the server."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:351:class KiCadFastMCP(FastMCP):
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:352:    """FastMCP extension that auto-infers tool annotations and adds CORS support."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:363:        """Defer heavy tool/resource registration until after stdio initialize can bind."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:430:                        f"{published_description.rstrip()} This KiCad MCP Pro tool "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:431:                        "supports production EDA automation workflows for MCP clients."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:433:            return super(KiCadFastMCP, self).tool(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:497:                    "MCP-Protocol-Version",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:498:                    "MCP-Session-Id",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:511:        """Materialize resources before discovery when stdio startup was deferred."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:526:        """Materialize prompts before discovery when stdio startup was deferred."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:594:                return PlainTextResponse("Origin not allowed for this MCP server.", status_code=403)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:598:def _server_base_url(cfg: KiCadMCPConfig) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:613:        "# HELP kicad_mcp_tool_calls_total Total MCP tool calls observed by this process.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:658:def _register_profile_components(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:659:    server: KiCadFastMCP,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:661:    cfg: KiCadMCPConfig,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:663:    """Register all profile-specific MCP surfaces on an already-created server."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:686:    router.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:687:    project.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:689:    if "pcb_read" in enabled or "pcb_write" in enabled:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:690:        pcb.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:692:        schematic.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:693:        variants.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:695:        library.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:697:        export.register(server, include_low_level_exports="export" in enabled)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:699:        validation.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:701:        dfm.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:703:        routing.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:705:        power_integrity.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:707:        emc_compliance.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:709:        signal_integrity.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:711:        simulation.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:713:        version_control.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:715:        manufacturing.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:717:    board_state.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:718:    studio_context.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:719:    workflows.register(server)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:725:def build_server(profile: str | None = None, *, defer_registration: bool = False) -> FastMCP:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:726:    """Build a FastMCP server instance for the active profile."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:728:    selected_profile = profile or cfg.profile
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:729:    enabled = set(categories_for_profile(selected_profile))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:733:        base_url = _server_base_url(cfg)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:736:            resource_server_url=base_url,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:740:    server = KiCadFastMCP(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:743:            "KiCad MCP Pro Server for project setup, schematic capture, PCB editing, "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:758:    server.allow_experimental_tools = selected_profile == "agent_full"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:759:    server.allowed_tool_names = {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:763:    @server.custom_route("/.well-known/mcp-server", methods=["GET"], include_in_schema=False)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:767:    @server.custom_route("/well-known/mcp-server", methods=["GET"], include_in_schema=False)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:771:    @server.custom_route(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:772:        "/.well-known/mcp-server/token-rotate",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:796:        @server.custom_route("/metrics", methods=["GET"], include_in_schema=False)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:804:        _register_profile_components(server, enabled, cfg)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:807:        server.set_lazy_registration(register)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:811:    return server
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:814:def create_server(profile: str | None = None) -> _SyncServerHandle:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:816:    return _SyncServerHandle(build_server(profile))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:827:def _print_startup_diagnostics(cfg: KiCadMCPConfig, *, probe_runtime: bool = True) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:828:    """Emit a concise startup summary without writing directly to stdio transport."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:829:    if cfg.transport == "stdio" and cfg.auth_token:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:831:            "stdio_auth_token_ignored",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:832:            message="KICAD_MCP_AUTH_TOKEN has no effect when the server runs over stdio.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:838:        profile=cfg.profile,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:847:def _apply_cli_env(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:854:    profile: str | None = None,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:857:    cli_env = {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:858:        "KICAD_MCP_TRANSPORT": transport,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:859:        "KICAD_MCP_HOST": host,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:860:        "KICAD_MCP_PORT": (
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:863:        "KICAD_MCP_LOG_LEVEL": log_level,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:864:        "KICAD_MCP_LOG_FORMAT": log_format,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:865:        "KICAD_MCP_PROFILE": profile,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:866:        "KICAD_MCP_PROJECT_DIR": project_dir,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:868:    for key, value in cli_env.items():
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:870:            os.environ[key] = value
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:872:        os.environ["KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS"] = "true" if experimental else "false"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:875:def _run_server_from_options(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:883:    profile: str | None = None,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:886:    """Apply CLI overrides and start the MCP server."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:887:    _apply_cli_env(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:894:        profile=profile,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:901:    selected_transport = "stdio" if cfg.transport == "stdio" else "streamable-http"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:912:                message="Ignoring KICAD_MCP_TRANSPORT=sse because KICAD_MCP_LEGACY_SSE is false.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:914:    defer_registration = selected_transport == "stdio"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:915:    server = build_server(cfg.profile, defer_registration=defer_registration)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:921:        profile=cfg.profile,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:924:    if selected_transport == "stdio":
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:925:        if hasattr(server, "start_lazy_registration_background"):
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:926:            cast(_LazyRegistrationServer, server).start_lazy_registration_background()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:927:        server.run(transport="stdio")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:931:        server.run(transport="sse", mount_path=cfg.mount_path)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:934:    server.run(transport="streamable-http", mount_path=cfg.mount_path)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:939:    transport: str | None = typer.Option(None, help="Transport: stdio, http, sse, streamable-http"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:945:    profile: str | None = typer.Option(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:946:        None, help=f"Server profile: {', '.join(available_profiles())}"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:950:    """Start the KiCad MCP Pro server when no subcommand is supplied."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:951:    _apply_cli_env(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:958:        profile=profile,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:964:    _run_server_from_options()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:969:    transport: str | None = typer.Option(None, help="Transport: stdio, http, sse, streamable-http"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:975:    profile: str | None = typer.Option(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:976:        None, help=f"Server profile: {', '.join(available_profiles())}"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:980:    """Start the MCP server explicitly."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:981:    _run_server_from_options(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:988:        profile=profile,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1017:                "hint": "Fix malformed KiCad MCP configuration and retry.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1030:def health(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1033:    """Report fast package and configuration health without requiring KiCad IPC."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1034:    _diagnostic_command(build_health_report, as_json=json_output)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1038:def doctor(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1042:    _diagnostic_command(build_doctor_report, as_json=json_output)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\server.py:1054:        "mcp": {"transport_default": cfg.transport, "profile": cfg.profile},
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:11:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:28:            "Help: https://oaslananka.github.io/kicad-mcp-pro/installation/"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:87:        path.write_text(json.dumps(state, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:130:        project_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:133:    path.write_text(json.dumps(state, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:187:def _write_bom(path: Path, rows: list[dict[str, Any]], format_name: str) -> Path:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:189:        path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:193:    writer = csv.DictWriter(buffer, fieldnames=["reference", "value", "footprint"])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:194:    writer.writeheader()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:195:    writer.writerows(rows)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:196:    path.write_text(buffer.getvalue(), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:210:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\variants.py:325:        _write_bom(out_file, rows, fmt)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:5:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:48:   - `check_design_for_manufacture(profile="{target_fab}")`
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:56:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:141:step, not a debugging shortcut. In the `manufacturing` profile it is the only gated
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:151:8. If you need low-level debug or interchange artifacts, switch to a broader profile
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:220:5. If you need low-level debug artifacts, switch to a broader profile such as `full`
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:221:   or `minimal`; the `manufacturing` profile stays focused on gated release handoff.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:263:Polish the design against a manufacturer profile.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\prompts\workflows.py:265:1. Load the target profile with `dfm_load_manufacturer_profile()`.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\azure-devops.md:7:The primary Azure pipeline definition lives in the repository root as `azure-pipelines.yml`.
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\azure-devops.md:17:Preferred setup: store a single Doppler service token in Azure DevOps and let the pipeline fetch release secrets at runtime:
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\azure-devops.md:27:The root `azure-pipelines.yml` still supports native Azure variables as a fallback:
03_TOOLS\repos\kicad-mcp-pro\docs\deployment\azure-devops.md:33:You can store these in a variable group if you want to share them across multiple pipelines.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\templates\subcircuits\SPI_flash.yaml:3:description: W25Qxx-style SPI flash with decoupling and hold/write-protect bias.
03_TOOLS\repos\kicad-mcp-pro\docs\repository-operations.md:28:privilege workflow permissions and protected environments rather than disabling
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1:"""PCB read/write tools backed by KiCad IPC."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:31:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:88:STACKUP_STATE_FILE = "stackup_profile.json"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:207:def _write_stackup_state(layers: list[StackupLayerSpec]) -> Path:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:209:    path.write_text(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:519:        raise ValueError("Refusing to write an invalid PCB file with unbalanced parentheses.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:542:            "No PCB file is configured. Call kicad_set_project() or set KICAD_MCP_PCB_FILE."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:545:        path.write_text(_default_board_text(), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:581:def _transactional_board_write(mutator: Callable[[str], str]) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:587:        handle.write(updated)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1088:    _transactional_board_write(lambda current: _replace_board_blocks(current, replacements, []))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1267:        path.write_text(json.dumps(default, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1274:    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1572:            "No schematic file is configured. Call kicad_set_project() or set KICAD_MCP_SCH_FILE."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1675:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1903:        """Set the active board stackup using a file-backed profile."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1909:        state_path = _write_stackup_state(payload.layers)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:1910:        _transactional_board_write(lambda current: _apply_stackup_to_board(current, payload.layers))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:2021:            return "No pad pairs on different named nets were available for creepage analysis."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:2152:            path.write_text(content, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:2495:        _transactional_board_write(lambda current: _append_board_blocks(current, [board_block]))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:2640:        _transactional_board_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:2810:            _transactional_board_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:2940:            _transactional_board_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3051:        _transactional_board_write(lambda current: _replace_board_blocks(current, replacements, []))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3141:        _transactional_board_write(lambda current: _replace_board_blocks(current, replacements, []))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3200:        _transactional_board_write(lambda current: _replace_board_blocks(current, replacements, []))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3323:        name: str = "MCP_Keepout",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3421:        _transactional_board_write(lambda current: _replace_board_blocks(current, {}, additions))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3469:        _transactional_board_write(lambda current: _replace_board_blocks(current, {}, additions))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3567:        _transactional_board_write(lambda current: _replace_board_blocks(current, {}, additions))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\pcb.py:3684:                    f"MCP_Teardrop_{getattr(pad.parent.reference_field.text, 'value', 'PAD')}"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\logging.py:34:    """Configure structured logging for the MCP server."""
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-code.mcp.json:4:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-code.mcp.json:6:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-code.mcp.json:7:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\claude-code.mcp.json:8:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_tool_metadata_lint.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_tool_metadata_lint.py:23:    server = build_server("agent_full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_tool_metadata_lint.py:25:    for tool in await server.list_tools():
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export_support.py:54:            "kicad-cli is not available. Set KICAD_MCP_KICAD_CLI to a valid executable."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export_support.py:117:            "No PCB file is configured. Call kicad_set_project() or set KICAD_MCP_PCB_FILE."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export_support.py:126:            "No schematic file is configured. Call kicad_set_project() or set KICAD_MCP_SCH_FILE."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\library.py:10:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\library.py:241:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\library.py:437:        library_file.write_text(content, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\library.py:723:        out_file.write_text(sexpr, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\library.py:802:        out_file.write_text(sexpr, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:20:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:32:_ROTATIONS_JSON = Path(__file__).parent.parent / "dfm_profiles" / "jlcpcb_rotations.json"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:130:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:148:        Requires ``kikit`` to be installed (``pip install kikit``).
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:167:                "KiKit is not installed. "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:168:                "Install it with: pip install kikit\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:251:                "Panelization requires explicit confirmation because it writes a PCB file.\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:257:                "Refusing to overwrite an existing panel file without choosing a new output_path.\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:285:    def mfg_generate_test_plan(output_path: str = "", confirm_overwrite: bool = False) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:297:            confirm_overwrite: If True, allow overwriting an existing output file.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:389:                        "Read/write device registers to confirm communication.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:438:            if out_file.exists() and not confirm_overwrite:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:440:                    "Refusing to overwrite an existing test plan without confirmation.\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:442:                    "Rerun with confirm_overwrite=true or choose a different output_path."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:445:            out_file.write_text(text, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:509:        manifest_json_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:525:        manifest_txt_path.write_text("\n".join(txt_lines), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:549:        offsets from the bundled ``jlcpcb_rotations.json`` table, and writes a
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:637:                "CPL rotation correction writes a new CSV and requires explicit confirmation.\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:643:                "Refusing to overwrite an existing corrected CPL CSV.\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:652:                writer = csv.DictWriter(fh, fieldnames=fieldnames)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:653:                writer.writeheader()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:654:                writer.writerows(rows)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\manufacturing.py:656:            return f"Failed to write corrected CPL CSV: {exc}"
03_TOOLS\repos\kicad-mcp-pro\docs\demo-media.md:11:1. Configure a VS Code MCP session.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py:1:"""Tool metadata decorators used for discovery and profile documentation."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py:13:    """Discovery metadata attached to a public MCP tool."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py:120:    """Infer MCP 2026-style annotations from existing tool metadata and naming."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py:124:    is_write = (
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py:140:    is_read_only = not is_write and (
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\metadata.py:152:    if is_write:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing_rules.py:60:            "Refusing to write an invalid design rules file with unbalanced parentheses."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing_rules.py:82:        raise ValueError(f"Refusing to write invalid design rules after updating {rule_name}.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing_rules.py:86:def _write_rule(rule_name: str, rule_body: str) -> Path:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing_rules.py:90:    path.write_text(updated, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:7:from kicad_mcp.server import KiCadFastMCP, _print_startup_diagnostics, build_server, main_callback
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:21:    monkeypatch.setattr("kicad_mcp.server.find_kicad_version", lambda _cli: "10.0.1")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:23:        "kicad_mcp.server.get_board",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:26:    monkeypatch.setattr("kicad_mcp.server.logger.info", fake_info)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:32:    assert payload["profile"] == "full"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:39:def test_print_startup_diagnostics_warns_when_stdio_uses_auth_token(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:45:    cfg.transport = "stdio"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:49:    monkeypatch.setattr("kicad_mcp.server.find_kicad_version", lambda _cli: "10.0.1")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:51:        "kicad_mcp.server.get_board",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:55:        "kicad_mcp.server.logger.warning",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:58:    monkeypatch.setattr("kicad_mcp.server.logger.info", lambda *_args, **_kwargs: None)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:62:    assert warnings == ["stdio_auth_token_ignored"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:65:def test_main_callback_runs_startup_diagnostics_before_server_run(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:80:    monkeypatch.setattr("kicad_mcp.server.setup_logging", lambda *_args: None)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:82:    def fake_build_server(profile: str, *, defer_registration: bool = False) -> FakeServer:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:83:        observed["build_profile"] = profile
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:87:    monkeypatch.setattr("kicad_mcp.server.build_server", fake_build_server)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:90:        observed["profile"] = cfg.profile
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:94:    monkeypatch.setattr("kicad_mcp.server._print_startup_diagnostics", fake_diagnostics)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:97:        transport="stdio",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:103:        profile="full",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:107:    assert observed["profile"] == "full"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:108:    assert observed["build_profile"] == "full"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:113:    assert observed["transport"] == "stdio"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:118:    server = build_server("minimal", defer_registration=True)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:120:    assert isinstance(server, KiCadFastMCP)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:121:    assert server._lazy_registration_complete is False
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:123:    tool_names = {tool.name for tool in server.list_tools_sync()}
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_server_startup.py:125:    assert server._lazy_registration_complete is True
03_TOOLS\repos\kicad-mcp-pro\docs\release-process.md:8:workflow permission at read-only while still allowing release-please to open
03_TOOLS\repos\kicad-mcp-pro\docs\release-process.md:17:5. Approve the `release` environment gate.
03_TOOLS\repos\kicad-mcp-pro\docs\release-process.md:36:`publish=true` and the protected environment is approved. Doppler remains the
03_TOOLS\repos\kicad-mcp-pro\docs\release-process.md:56:`pyproject.toml` is the source of truth for `mcp.json` and `server.json`.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:13:from mcp.server.fastmcp import Context, FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:43:from .router import TOOL_CATEGORIES, available_profiles
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:77:    """Structured design-spec payload returned to capable MCP clients."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:155:            f"- Server profile: {cfg.profile}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:293:    path.write_text(json.dumps(normalized.model_dump(), indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:770:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1059:        """Run the project quality gate and automatically apply server-side fixes.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1064:           underlying fix implementation directly on the server, then re-evaluates.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1170:                break  # Nothing left for the server to do   hand off to agent
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1495:    def kicad_create_new_project(path: str, name: str, confirm_overwrite: bool = False) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1503:        if project_dir.exists() and any(project_dir.iterdir()) and not confirm_overwrite:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1507:                "Choose a new name/path or rerun with confirm_overwrite=true."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1512:        project_file.write_text(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1523:        pcb_file.write_text(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1527:        sch_file.write_text(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1564:        lines = [f"# KiCad MCP Pro Server v{__version__}", f"CLI path: {cfg.kicad_cli}"]
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1593:            "# KiCad MCP Pro Quick Start",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\project.py:1606:        lines.extend(f"- `{profile}`" for profile in available_profiles())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:1:"""Manufacturer-specific DFM profile tools."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:14:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:28:    """Subset of board access used by the DFM profile helpers."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:40:def _profile_resource_name(manufacturer: str, tier: str) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:44:def _available_profile_names() -> list[str]:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:45:    profile_root = resources.files("kicad_mcp.dfm_profiles")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:47:        entry.name[:-5] for entry in profile_root.iterdir() if entry.name.endswith(".json")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:51:def _load_profile(manufacturer: str, tier: str) -> dict[str, Any]:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:52:    resource_name = _profile_resource_name(manufacturer, tier)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:53:    resource_root = resources.files("kicad_mcp.dfm_profiles")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:56:        available = ", ".join(_available_profile_names())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:58:            f"Unknown DFM profile '{manufacturer}/{tier}'. Available profiles: {available}"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:63:def _active_profile_path() -> Path:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:64:    return _ensure_output_dir() / "active_dfm_profile.json"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:67:def _write_active_profile_selection(manufacturer: str, tier: str) -> Path:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:68:    path = _active_profile_path()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:70:    path.write_text(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:77:def _selected_profile() -> dict[str, Any]:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:78:    path = _active_profile_path()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:81:        return _load_profile(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:85:    return _load_profile(*DEFAULT_PROFILE)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:214:    profile: dict[str, Any],
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:218:    rules = cast(dict[str, float | int], profile["rules"])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:220:    _, report, error = _run_drc_report("dfm_profile_check.json")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:229:        heading or "DFM profile check:",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:230:        f"- Profile: {profile['manufacturer']} / {profile['tier']}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:324:            f"against {profile['manufacturer']} {profile['tier']} fab notes.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:332:    profile: dict[str, Any],
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:335:    pricing = cast(dict[str, float], profile["pricing"])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:351:        f"- Profile: {profile['manufacturer']} / {profile['tier']}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:372:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:377:    def dfm_load_manufacturer_profile(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:381:        """Load a bundled manufacturer DFM profile for subsequent checks."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:382:        profile = _load_profile(manufacturer, tier)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:383:        state_path = _write_active_profile_selection(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:384:            str(profile["manufacturer"]),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:385:            str(profile["tier"]),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:389:                "DFM profile loaded.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:390:                f"- Active profile: {profile['manufacturer']} / {profile['tier']}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:398:        """Run a manufacturer-aware DFM review using the active bundled profile."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:399:        profile = _selected_profile()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:400:        return "\n".join(_dfm_check_lines(profile))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:412:        profile = _load_profile(manufacturer, tier)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\dfm.py:413:        return "\n".join(_cost_lines(profile, quantity))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export.py:11:from mcp.server.fastmcp import Context, FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export.py:118:def register(mcp: FastMCP, *, include_low_level_exports: bool = True) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export.py:244:                        writer = csv.DictWriter(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export.py:248:                        writer.writeheader()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\export.py:249:                        writer.writerows(rows)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\freerouting.py:197:                    "KICAD_MCP_FREEROUTING_JAR."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\freerouting.py:237:                    "Set KICAD_MCP_FREEROUTING_JAR or pass freerouting_jar_path."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\fixers.py:6:underlying implementation directly   without going through MCP transport.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\fixers.py:28:    ``auto_applicable`` indicates the server can apply the fix without agent
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\fixers.py:221:    """Build a compact prompt for MCP client-side sampling when supported."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:14:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:62:    """Machine-readable gate outcome for MCP clients that support structured output."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:80:    """Structured placement analysis payload."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:856:def _placement_analysis() -> tuple[PlacementAnalysis | None, GateOutcome | None]:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1259:def _format_placement_score(analysis: PlacementAnalysis) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1261:        f"Placement score: {analysis.score}/100",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1262:        f"- Footprints analysed: {analysis.footprint_count}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1263:        f"- Board frame: {analysis.board_width_mm:.2f} x {analysis.board_height_mm:.2f} mm",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1264:        f"- Density: {analysis.density_pct:.2f}%",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1265:        f"- Connector checks: {analysis.checked_connectors}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1266:        f"- Decoupling pair checks: {analysis.checked_decoupling_pairs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1267:        f"- RF keepout checks: {analysis.checked_keepouts}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1268:        f"- Power-tree refs checked: {analysis.checked_power_tree_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1269:        f"- Analog refs checked: {analysis.checked_analog_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1270:        f"- Digital refs checked: {analysis.checked_digital_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1271:        f"- Sensor-cluster refs checked: {analysis.checked_sensor_cluster_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1272:        f"- Critical-net Manhattan proxy: {analysis.critical_net_proxy_mm:.2f} mm",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1273:        f"- Critical-net proxy density: {analysis.critical_net_proxy_density:.2f} mm per 1000 mm^2",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1274:        f"- Thermal hotspot refs checked: {analysis.checked_thermal_hotspot_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1275:        f"- Thermal hotspot proximity: {analysis.thermal_proximity_sum:.4f}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1276:        f"- Hard failures: {len(analysis.hard_failures)}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1277:        f"- Warnings: {len(analysis.warnings)}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1279:    lines.extend(f"- FAIL: {item}" for item in analysis.hard_failures[:12])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1280:    lines.extend(f"- WARN: {item}" for item in analysis.warnings[:12])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1285:    analysis, blocked = _placement_analysis()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1288:    if analysis is None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1289:        raise RuntimeError("Placement analysis unexpectedly returned no result.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1291:    status: GateStatus = "PASS" if not analysis.hard_failures else "FAIL"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1293:        f"Footprints analysed: {analysis.footprint_count}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1294:        f"Board frame: {analysis.board_width_mm:.2f} x {analysis.board_height_mm:.2f} mm",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1295:        f"Density: {analysis.density_pct:.2f}%",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1296:        f"Connector checks: {analysis.checked_connectors}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1297:        f"Decoupling pair checks: {analysis.checked_decoupling_pairs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1298:        f"RF keepout checks: {analysis.checked_keepouts}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1299:        f"Power-tree refs checked: {analysis.checked_power_tree_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1300:        f"Analog refs checked: {analysis.checked_analog_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1301:        f"Digital refs checked: {analysis.checked_digital_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1302:        f"Sensor-cluster refs checked: {analysis.checked_sensor_cluster_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1303:        f"Critical-net Manhattan proxy: {analysis.critical_net_proxy_mm:.2f} mm",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1304:        f"Critical-net proxy density: {analysis.critical_net_proxy_density:.2f} mm per 1000 mm^2",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1305:        f"Thermal hotspot refs checked: {analysis.checked_thermal_hotspot_refs}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1306:        f"Thermal hotspot proximity: {analysis.thermal_proximity_sum:.4f}",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1307:        f"Placement score: {analysis.score}/100",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1309:    details.extend(f"FAIL: {item}" for item in analysis.hard_failures[:12])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1310:    details.extend(f"WARN: {item}" for item in analysis.warnings[:12])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1327:    from .dfm import _dfm_check_lines, _load_profile, _selected_profile
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1337:    profile = (
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1338:        _load_profile(manufacturer, tier)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1340:        else cast(dict[str, object], _selected_profile())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1343:        cast(dict[str, object], profile),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1349:    details = [f"Profile: {profile['manufacturer']} / {profile['tier']}"]
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1430:    analysis, blocked = _placement_analysis()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1438:    if analysis is None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1439:        raise RuntimeError("Placement analysis unexpectedly returned no result.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1445:        score=analysis.score,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1446:        footprint_count=analysis.footprint_count,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1447:        checked_connectors=analysis.checked_connectors,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1448:        checked_decoupling_pairs=analysis.checked_decoupling_pairs,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1449:        checked_keepouts=analysis.checked_keepouts,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1450:        checked_power_tree_refs=analysis.checked_power_tree_refs,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1451:        checked_analog_refs=analysis.checked_analog_refs,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1452:        checked_digital_refs=analysis.checked_digital_refs,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1453:        checked_sensor_cluster_refs=analysis.checked_sensor_cluster_refs,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1454:        hard_failures=analysis.hard_failures,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1455:        warnings=analysis.warnings,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1508:        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1515:    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1609:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1661:        path.write_text(dump_dru(root), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1678:        path.write_text(dump_dru(root), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1718:        path.write_text(dump_dru(root), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1737:        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1828:        """Return a structured placement-quality report for capable MCP clients."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1841:        analysis, blocked = _placement_analysis()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1850:        if analysis is None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1851:            raise RuntimeError("Placement analysis unexpectedly returned no result.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1852:        return _format_placement_score(analysis)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1860:        """Evaluate manufacturing readiness against the active or requested DFM profile."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1886:        """Return the full project gate in structured form for capable MCP clients."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1897:        from .dfm import _dfm_check_lines, _load_profile
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1899:        profile = _load_profile("JLCPCB" if jlcpcb else "PCBWay", "standard")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1900:        heading = f"DFM check ({'JLCPCB' if jlcpcb else 'generic'} profile):"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\validation.py:1901:        return "\n".join(_dfm_check_lines(profile, heading=heading))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\power_integrity.py:12:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\power_integrity.py:211:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\power_integrity.py:471:                "package thermal-envelope workflow or legacy 'power_w'."
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:7:3. `.env`
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:16:kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:17:kicad-mcp-pro doctor --json
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:21:`health --json` is a fast install/configuration check and does not require a
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:22:running KiCad IPC server. `doctor --json` adds deeper KiCad CLI and IPC probes
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:28:Existing `KICAD_MCP_*` variables continue to work. The server also accepts these
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:33:| `KICAD_API_TOKEN` | KiCad IPC token |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:34:| `KICAD_CLI_PATH` | `kicad-cli` path |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:35:| `KICAD_MCP_TIMEOUT_MS` | IPC timeout in milliseconds |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:36:| `KICAD_MCP_RETRIES` | IPC connection retries |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:37:| `KICAD_MCP_HEADLESS` | Headless preference |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:38:| `KICAD_MCP_WORKSPACE_ROOT` | Workspace root for path safety |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:45:When `KICAD_MCP_WORKSPACE_ROOT` is set, project artifact reads and writes must
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:1:"""Tool routing, metadata labels, and server profiles."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:7:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:51:        "description": "Project setup, server discovery, and quick help.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:99:    "pcb_write": {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:293:        "description": "Load bundled manufacturer profiles, run DFM checks, and estimate cost.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:295:            "dfm_load_manufacturer_profile",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:315:            "route_create_tuning_profile",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:316:            "route_list_tuning_profiles",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:317:            "route_apply_tuning_profile",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:372:            "sim_run_ac_analysis",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:396:    "pcb_only": ("project", "pcb_read", "pcb_write", "routing"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:410:        "pcb_write",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:437:        "pcb_write",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:450:        "pcb_write",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:456:    "analysis": ("project", "pcb_read", "signal_integrity", "power_integrity", "emc", "validation"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:459:    "pcb": ("project", "pcb_read", "pcb_write", "routing", "export", "validation"),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:464:def categories_for_profile(profile: str) -> tuple[str, ...]:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:465:    """Resolve categories enabled by the named server profile."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:466:    return PROFILE_CATEGORIES.get(profile, PROFILE_CATEGORIES["full"])
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:469:def available_profiles() -> tuple[str, ...]:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:470:    """Return the supported server profile names."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:483:        "analysis",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:491:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:497:        lines = ["# KiCad MCP Pro Tool Categories", ""]
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\router.py:505:        lines.extend(f"- `{profile}`" for profile in available_profiles())
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:15:from mcp.server.fastmcp import Context, FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:27:from .routing_rules import _load_rules_content, _mm, _rules_file_path, _upsert_rule, _write_rule
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:35:    "_write_rule",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:38:_TUNING_PROFILES_FILENAME = "tuning_profiles.json"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:39:_TUNING_ASSIGNMENTS_FILENAME = "tuning_profile_assignments.json"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:223:        path.write_text(json.dumps(default, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:230:    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:259:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:497:            path = _write_rule(rule_name, rule_body)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:533:            path = _write_rule(rule_name, rule_body)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:562:            path = _write_rule(rule_name, rule_body)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:577:    def route_create_tuning_profile(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:583:        """Create or update a KiCad 10-style time-domain tuning profile."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:588:        state = _load_state_file(_TUNING_PROFILES_FILENAME, {"profiles": {}})
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:589:        profiles = cast(dict[str, object], state.setdefault("profiles", {}))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:590:        profiles[name] = {
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:596:        return f"Tuning profile '{name}' saved to {path}."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:600:    def route_list_tuning_profiles() -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:601:        """List configured time-domain tuning profiles."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:602:        state = _load_state_file(_TUNING_PROFILES_FILENAME, {"profiles": {}})
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:603:        return json.dumps(state.get("profiles", {}), indent=2)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:607:    def route_apply_tuning_profile(net_pattern: str, profile_name: str) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:608:        """Assign a named tuning profile to a net or wildcard net group."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:609:        profiles_state = _load_state_file(_TUNING_PROFILES_FILENAME, {"profiles": {}})
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:610:        profiles = cast(dict[str, dict[str, object]], profiles_state.get("profiles", {}))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:611:        profile = profiles.get(profile_name)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:612:        if profile is None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:613:            return f"Tuning profile '{profile_name}' was not found."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:618:            "profile_name": profile_name,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:619:            "layer": profile.get("layer", ""),
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:623:            f"Tuning profile '{profile_name}' assigned to '{net_pattern}'.\n"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:636:        profiles_state = _load_state_file(_TUNING_PROFILES_FILENAME, {"profiles": {}})
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:637:        profiles = cast(dict[str, dict[str, object]], profiles_state.get("profiles", {}))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:639:        profile_impedance_ohm = 50.0
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:645:                    for item in profiles.values()
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:654:                raw_impedance = matching.get("trace_impedance_ohm", profile_impedance_ohm)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:656:                    profile_impedance_ohm = float(raw_impedance)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:670:                    profile_impedance_ohm,
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:709:            path = _write_rule(rule_name, rule_body)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\routing.py:760:                path = _write_rule(rule_name, rule_body)
03_TOOLS\repos\kicad-mcp-pro\docs\maintenance-policy.md:8:task install
03_TOOLS\repos\kicad-mcp-pro\docs\maintenance-policy.md:19:Gitleaks, actionlint, and zizmor, and runs OSV Scanner and Trivy when installed.
03_TOOLS\repos\kicad-mcp-pro\docs\maintenance-policy.md:20:Missing required binaries fail with install guidance instead of silently
03_TOOLS\repos\kicad-mcp-pro\docs\maintenance-policy.md:30:KiCad/MCP/Pydantic/Typer ecosystem updates require Dependency Dashboard approval
03_TOOLS\repos\kicad-mcp-pro\docs\maintenance-policy.md:35:Required gates are Ruff, mypy, pytest with coverage, Bandit, the pip-audit backed
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:12:    transactional_write,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:41:    schematic_file.write_text("(kicad_sch)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:52:        def transactional_write(self, mutator):
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:77:        def transactional_write(self, mutator):
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:78:            calls.append(("transactional_write", (mutator,)))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:91:    assert transactional_write(lambda text: text) == "written"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_schematic_backend_adapter.py:95:        "transactional_write",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic_transfer.py:73:            "No schematic file is configured. Call kicad_set_project() or set KICAD_MCP_SCH_FILE."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\design_intent_state.py:79:        description="Thermal operating-environment specification.",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\emc_compliance.py:10:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\emc_compliance.py:419:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:1:"""Schematic tools with parser-based reads and transactional writes."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:17:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:259:            "Power-flag analysis can be derived from ERC/validation output, but there is "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:326:            "to match the existing textual MCP surface."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:359:    def transactional_write(self, mutator: Callable[[str], str]) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:587:    def transactional_write(self, mutator: Callable[[str], str]) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:588:        return _transactional_write_to_schematic(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:706:_KICAD_FP_SEARCH_PATHS: list[Path] = [
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:718:    roots = [p for p in _KICAD_FP_SEARCH_PATHS if p.exists()]
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:1641:            "No schematic file is configured. Call kicad_set_project() or set KICAD_MCP_SCH_FILE."
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:1669:    Renumbers all schematic references sequentially without requiring an MCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:1703:    transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:1712:    transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2570:    lines = ["Net compilation analysis:"]
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2742:    return "KiCadMCP"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2854:    project_name: str = "KiCadMCP",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2940:        raise ValueError("Refusing to write an invalid schematic with unbalanced parentheses.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2943:            'Refusing to write an invalid schematic with incomplete (paper "User") dimensions.'
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2988:        path.write_text(json.dumps(default, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:2995:    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3022:def _transactional_write_to_schematic(mutator: Callable[[str], str]) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3023:    """Read, mutate, validate, and atomically rewrite the active schematic."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3029:        handle.write(updated)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3036:def transactional_write(mutator: Callable[[str], str]) -> str:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3037:    """Read, mutate, validate, and atomically rewrite the active schematic."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3038:    return get_schematic_backend().transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3089:    _transactional_write_to_schematic(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3201:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3312:        project_name = cfg.project_file.stem if cfg.project_file is not None else "KiCadMCP"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3342:        transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3375:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3402:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3461:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3486:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3501:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3534:        cfg.project_file.write_text(json.dumps(project_payload, indent=2), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3639:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3691:            transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3766:            transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3823:            transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3884:        """Build (overwrite) the active schematic from structured symbol, wire, and label inputs.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:3948:        project_name = cfg.project_file.stem if cfg.project_file is not None else "KiCadMCP"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4056:        _get_schematic_file().write_text(content, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4138:        transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4226:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4262:        transactional_write(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4414:        transactional_write(mutator)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4772:            sch_file.write_text(new_text, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\schematic.py:4774:            return f"Could not write schematic file: {exc}"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\component_search.py:291:        self._client_id = os.getenv("NEXAR_CLIENT_ID")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\component_search.py:292:        self._client_secret = os.getenv("NEXAR_CLIENT_SECRET")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\component_search.py:319:        self._client_id = os.getenv("DIGIKEY_CLIENT_ID")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\component_search.py:320:        self._client_secret = os.getenv("DIGIKEY_CLIENT_SECRET")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\component_search.py:336:            "DigiKey live search wiring is not enabled in the default zero-auth profile. "
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:9:from mcp.server.fastmcp import Context, FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:73:        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:138:    lines = _format_result_header("Operating point analysis", result)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:271:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:277:        """Persist a SPICE directive used by future MCP simulation runs."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:286:        """Run a DC operating-point analysis."""
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:298:    def sim_run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:314:        result = _runner().run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:322:        return _format_series_result("AC analysis", result)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:342:        await _report_progress(ctx, 35, 100, "Running ngspice transient analysis...")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:343:        result = _runner().run_transient_analysis(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:350:        await _report_progress(ctx, 100, 100, "Transient analysis complete.")
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:351:        return _format_series_result("Transient analysis", result)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:382:        return _format_series_result("DC sweep analysis", result)
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\simulation.py:404:        result = _runner().run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:9:from mcp.server.fastmcp import FastMCP
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:44:def _write_nc_rule(
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:52:    from .routing import _mm, _write_rule  # local import avoids a module cycle
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:76:    return str(_write_rule(name, body))
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:400:def register(mcp: FastMCP) -> None:
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:530:                f"Differential-pair skew analysis ({verdict}):",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:664:            f"Via stub analysis at {payload.frequency_ghz:.3f} GHz:",
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:1035:                "Set dry_run=False to write all net class rules to the .kicad_dru file._"
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:1038:            # Actually write each net class rule to the design rules file.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\tools\signal_integrity.py:1052:                    rules_file = _write_nc_rule(nc, cl, tw, dg)
03_TOOLS\repos\kicad-mcp-pro\docs\comparison.md:3:| Capability | KiCad MCP Pro | Generic KiCad scripts | Raw `kicad-cli` |
03_TOOLS\repos\kicad-mcp-pro\docs\comparison.md:5:| MCP tools/resources/prompts | Yes | No | No |
03_TOOLS\repos\kicad-mcp-pro\docs\comparison.md:12:KiCad MCP Pro is designed for agentic workflows where the server needs project context, safe path handling, structured validation, and release-gated manufacturing output.
03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\cache.py:1:"""Small in-process TTL cache helpers for repeated read-only tool calls."""
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:14:    source_dsn.write_text("dsn", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:38:    dsn_path.write_text("dsn", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:44:        ses_path.write_text("ses", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:84:    dsn_path.write_text("(pcb (net A) (net B))", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:85:    jar_path.write_text("jar", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:93:        ses_path.write_text("ses", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:115:    dsn_path.write_text("dsn", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py:125:    ses_path.write_text("ses", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:7:from kicad_mcp.config import KiCadMCPConfig
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:12:    monkeypatch.setenv("KICAD_API_TOKEN", "secret-token")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:13:    monkeypatch.setenv("KICAD_CLI_PATH", str(fake_cli))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:14:    monkeypatch.setenv("KICAD_MCP_TIMEOUT_MS", "15000")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:15:    monkeypatch.setenv("KICAD_MCP_RETRIES", "4")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:16:    monkeypatch.setenv("KICAD_MCP_HEADLESS", "true")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:17:    monkeypatch.setenv("KICAD_MCP_WORKSPACE_ROOT", str(workspace))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:18:    monkeypatch.setenv("KICAD_MCP_LOG_LEVEL", "debug")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:20:    cfg = KiCadMCPConfig()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:34:    monkeypatch.setenv("KICAD_MCP_TIMEOUT_MS", "not-a-number")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:37:        KiCadMCPConfig()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:40:def test_project_dir_env_prefers_canonical_project_over_numbered_duplicate(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:52:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(project_dir))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:54:    cfg = KiCadMCPConfig(kicad_cli=fake_cli)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config_aliases.py:61:    cfg = KiCadMCPConfig(cors_origins="vscode-webview://kicad-studio")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_additional.py:35:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_additional.py:93:    kipy_cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_additional.py:94:    path_cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_additional.py:95:    candidate_cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_additional.py:132:    (config_dir / "kicad_common.json").write_text("{invalid json", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:18:from kicad_mcp.server import main_callback
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:21:DOCKER_BIND_HOST = "0.0.0.0"  # noqa: S104 - regression fixture for Docker env preservation.
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:30:    fake_server = MagicMock()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:32:        "kicad_mcp.server.build_server",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:33:        lambda profile, *, defer_registration=False: fake_server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:35:    monkeypatch.setattr("kicad_mcp.server.setup_logging", lambda *args: None)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:44:        profile="minimal",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:48:    fake_server.run.assert_called_once_with(transport="streamable-http", mount_path="/mcp")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:51:def test_main_callback_runs_stdio(sample_project: Path, monkeypatch) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:52:    fake_server = MagicMock()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:54:        "kicad_mcp.server.build_server",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:55:        lambda profile, *, defer_registration=False: fake_server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:57:    monkeypatch.setattr("kicad_mcp.server.setup_logging", lambda *args: None)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:60:        transport="stdio",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:66:        profile="full",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:70:    fake_server.run.assert_called_once_with(transport="stdio")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:73:def test_main_callback_preserves_env_when_cli_options_missing(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:77:    fake_server = MagicMock()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:78:    profiles: list[str] = []
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:79:    monkeypatch.setenv("KICAD_MCP_TRANSPORT", "http")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:80:    monkeypatch.setenv("KICAD_MCP_HOST", DOCKER_BIND_HOST)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:81:    monkeypatch.setenv("KICAD_MCP_PORT", "4444")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:82:    monkeypatch.setenv("KICAD_MCP_LOG_LEVEL", "DEBUG")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:83:    monkeypatch.setenv("KICAD_MCP_LOG_FORMAT", "json")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:84:    monkeypatch.setenv("KICAD_MCP_PROFILE", "pcb_only")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:85:    monkeypatch.setenv("KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS", "true")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:86:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(sample_project))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:88:        "kicad_mcp.server.build_server",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:89:        lambda profile, *, defer_registration=False: profiles.append(profile) or fake_server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:91:    monkeypatch.setattr("kicad_mcp.server.setup_logging", lambda *args: None)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:93:        "kicad_mcp.server._print_startup_diagnostics",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:104:        profile=None,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:108:    assert os.environ["KICAD_MCP_HOST"] == DOCKER_BIND_HOST
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:109:    assert os.environ["KICAD_MCP_PORT"] == "4444"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:110:    assert os.environ["KICAD_MCP_PROFILE"] == "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:111:    assert os.environ["KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS"] == "true"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:112:    assert profiles == ["pcb_only"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:113:    fake_server.run.assert_called_once_with(transport="streamable-http", mount_path="/mcp")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:116:def test_main_callback_explicit_cli_options_override_env(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:120:    fake_server = MagicMock()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:121:    profiles: list[str] = []
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:122:    monkeypatch.setenv("KICAD_MCP_TRANSPORT", "http")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:123:    monkeypatch.setenv("KICAD_MCP_HOST", DOCKER_BIND_HOST)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:124:    monkeypatch.setenv("KICAD_MCP_PORT", "4444")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:125:    monkeypatch.setenv("KICAD_MCP_PROFILE", "pcb_only")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:126:    monkeypatch.setenv("KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS", "true")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:128:        "kicad_mcp.server.build_server",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:129:        lambda profile, *, defer_registration=False: profiles.append(profile) or fake_server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:131:    monkeypatch.setattr("kicad_mcp.server.setup_logging", lambda *args: None)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:133:        "kicad_mcp.server._print_startup_diagnostics",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:138:        transport="stdio",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:144:        profile="minimal",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:148:    assert os.environ["KICAD_MCP_TRANSPORT"] == "stdio"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:149:    assert os.environ["KICAD_MCP_HOST"] == "127.0.0.1"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:150:    assert os.environ["KICAD_MCP_PORT"] == "3334"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:151:    assert os.environ["KICAD_MCP_PROFILE"] == "minimal"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:152:    assert os.environ["KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS"] == "false"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:153:    assert profiles == ["minimal"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:154:    fake_server.run.assert_called_once_with(transport="stdio")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:161:    project_file.write_text("{}", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:165:    (config_dir / "kicad_common.json").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:181:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:213:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:250:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:278:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_runtime_helpers.py:298:    cli.write_text("changed", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:8:from kicad_mcp.config import KiCadMCPConfig
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:19:    cfg = KiCadMCPConfig(kicad_cli=fake_cli, ipc_retries=2)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:44:    cfg = KiCadMCPConfig(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:85:    cfg = KiCadMCPConfig(kicad_cli=fake_cli, ipc_retries=0)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:97:    cfg = KiCadMCPConfig(kicad_cli=fake_cli, ipc_retries=0)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:109:    cfg = KiCadMCPConfig(kicad_cli=fake_cli, ipc_retries=2)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:131:    cfg = KiCadMCPConfig(kicad_cli=fake_cli, ipc_retries=1)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_connection_session.py:152:    assert "KICAD_MCP_KICAD_SOCKET_PATH" in str(error)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_studio_watcher.py:13:    (project_dir / "demo.kicad_pro").write_text("{}", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_studio_watcher.py:14:    (project_dir / "demo.kicad_pcb").write_text("(kicad_pcb)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_studio_watcher.py:15:    (project_dir / "demo.kicad_sch").write_text("(kicad_sch)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_discovery_studio_watcher.py:22:    (project_dir / "demo.kicad_pro").write_text('{"meta": {"version": 2}}', encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:7:from kicad_mcp.config import KiCadMCPConfig
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:13:    cfg = KiCadMCPConfig(project_dir=sample_project)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:24:    outside.write_text("x", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:26:    cfg = KiCadMCPConfig(kicad_cli=fake_cli, workspace_root=workspace, project_dir=project)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:33:    cfg = KiCadMCPConfig(project_dir=sample_project)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:43:    nested.write_text("(kicad_pcb)", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:56:        "hint": "Run doctor for diagnostics and retry with corrected configuration.",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_path_safety.py:69:    assert payload["code"] == "KICAD_NOT_RUNNING"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py:5:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py:10:async def test_profile_tool_matrix_matches_declared_categories() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py:11:    for profile_name, categories in PROFILE_CATEGORIES.items():
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py:12:        server = build_server(profile_name)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py:13:        listed = [tool.name for tool in await server.list_tools()]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_profile_matrix.py:21:        if profile_name == "agent_full":
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py:9:from kicad_mcp.server import app
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py:12:def test_cli_health_json_does_not_require_kicad(sample_project: Path) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py:14:    result = CliRunner().invoke(app, ["health", "--json"])
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py:25:def test_cli_doctor_json_reports_unavailable_kicad_without_stack_trace(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py:36:    result = CliRunner().invoke(app, ["doctor", "--json"])
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_cli_diagnostics.py:56:    assert "Start the MCP server explicitly" in serve_help.output
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:15:from kicad_mcp.server import CLI_FAILURE_TOOL_NAMES, HEAVY_TOOL_NAMES, build_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:23:    assert build_server("minimal").settings.stateless_http is False
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:28:    assert build_server("minimal").settings.stateless_http is True
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:37:    server = build_server("minimal")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:39:    await call_tool_text(server, "kicad_get_version", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:41:    response = TestClient(server.streamable_http_app()).get("/metrics")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:51:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:69:    monkeypatch.setattr(server._tool_manager, "call_tool", fake_call_tool)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:72:        server.call_tool("export_gerber", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:73:        server.call_tool("export_gerber", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:74:        server.call_tool("export_gerber", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:112:    from kicad_mcp import server as server_module
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:118:        server_module.logger,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:123:    server_module._audit_tool_call(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:140:    server = build_server("minimal")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:143:        "kicad_mcp.server.logger.info",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:147:    await call_tool_text(server, "kicad_get_version", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:160:    server = build_server("minimal")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:161:    client = TestClient(server.streamable_http_app())
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:164:        "/.well-known/mcp-server/token-rotate",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:170:        "/.well-known/mcp-server/token-rotate",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:177:    assert asyncio.run(server._token_verifier.verify_token("old-token")) is None
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:178:    assert asyncio.run(server._token_verifier.verify_token("new-token")) is not None
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:186:    server = build_server("minimal")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:187:    client = TestClient(server.streamable_http_app())
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:203:    server = build_server("minimal")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:204:    client = TestClient(server.streamable_http_app())
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:207:        "/.well-known/mcp-server/token-rotate",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:218:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:220:    result = await server.call_tool("export_gerber", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:252:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:253:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:254:    result = await server.call_tool("export_gerber", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:283:        (output_path / "board-F_Cu.gbr").write_text("gerber\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:299:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:300:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:301:    result = await call_tool_text(server, "export_gerber", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:322:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:323:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:324:    result = await server.call_tool("export_manufacturing_package", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:418:def test_release_workflow_installs_actionlint_before_ci_check() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:424:    install_index = workflow.index("Install workflow lint tools")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:427:    assert setup_index < install_index < check_index
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:428:    assert "go install github.com/rhysd/actionlint/cmd/actionlint@v1.7.7" in workflow
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:438:    assert "contents: write" in workflow
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:439:    assert "pull-requests: write" in workflow
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:457:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:458:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:460:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:478:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:492:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:493:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:497:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:517:            output_path.write_text("generated\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:520:            (output_path / "board-F_Cu.gbr").write_text("gerber\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:539:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:540:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:541:    await call_tool_text(server, "variant_create", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:543:    result = await call_tool_text(server, "export_manufacturing_package", {"variant": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_hardening.py:548:    active = await call_tool_text(server, "variant_list", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_refactor_helper_modules.py:148:    with pytest.raises(RuntimeError, match="newer than this server supports"):
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_refactor_helper_modules.py:152:def test_routing_rules_load_upsert_and_write(sample_project: Path) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_refactor_helper_modules.py:168:    written_path = routing_rules._write_rule("min-width", replacement)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_refactor_helper_modules.py:173:    bad.write_text('(rules (rule "unterminated")', encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_refactor_helper_modules.py:209:        out_path.write_text(netlist, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:17:REGISTRY_SCHEMA = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:45:    pyproject.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:68:    server_json = json.loads((ROOT / "server.json").read_text(encoding="utf-8"))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:74:    assert server_json["$schema"] == REGISTRY_SCHEMA
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:75:    assert server_json["version"] == version
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:76:    assert server_json["packages"][0]["version"] == version
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:90:    assert "KICAD_MCP_LEGACY_SSE=true" in studio_doc
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:118:    assert "kicad_mcp/server.py" in names
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:122:    assert "kicad_mcp/dfm_profiles/jlcpcb_standard.json" in names
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:123:    assert "kicad-mcp-pro = kicad_mcp.server:main" in entry_points
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:127:    assert any(name.endswith("/src/kicad_mcp/server.py") for name in sdist_names)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:130:    install_dir = tmp_path / "install"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:131:    install = subprocess.run(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:134:            "pip",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:135:            "install",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:140:            str(install_dir),
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:148:    assert install.returncode == 0, install.stdout + install.stderr
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:150:    env = os.environ.copy()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:151:    env["PYTHONPATH"] = str(install_dir)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:156:            "import kicad_mcp.server; print(kicad_mcp.server.__name__)",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:159:        env=env,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_release_metadata.py:165:    assert smoke.stdout.strip() == "kicad_mcp.server"
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:5:from kicad_mcp.server import build_server, create_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:10:    available_profiles,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:11:    categories_for_profile,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:16:def test_available_profiles_include_v2_surface() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:29:        "analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:35:    assert expected.issubset(set(available_profiles()))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:36:    assert categories_for_profile("analysis") == PROFILE_CATEGORIES["analysis"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:37:    for agent_profile in ("builder", "critic", "release_manager"):
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:38:        assert categories_for_profile(agent_profile) == PROFILE_CATEGORIES[agent_profile]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:39:        assert categories_for_profile(agent_profile)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:42:    assert categories_for_profile("agent_full") == PROFILE_CATEGORIES["agent_full"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:43:    assert categories_for_profile("unknown-profile") == PROFILE_CATEGORIES["full"]
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:54:def test_create_server_sync_wrapper_materializes_tool_list() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:55:    server = create_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:56:    tools = server.list_tools()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:63:async def test_create_server_sync_wrapper_materializes_tool_list_inside_event_loop() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:64:    server = create_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:65:    tools = server.list_tools()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:73:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:75:    routing = await call_tool_text(server, "kicad_get_tools_in_category", {"category": "routing"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:76:    pcb_read = await call_tool_text(server, "kicad_get_tools_in_category", {"category": "pcb_read"})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:78:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:90:async def test_manufacturing_profile_exposes_release_exports_only() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:91:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:92:    tool_names = {tool.name for tool in await server.list_tools()}
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:102:async def test_full_profile_keeps_low_level_exports_available() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:103:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:104:    tool_names = {tool.name for tool in await server.list_tools()}
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:113:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_router_profiles.py:114:    registered = {tool.name for tool in await server.list_tools()}
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_benchmark_latency.py:10:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_benchmark_latency.py:21:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_benchmark_latency.py:26:        await call_tool_text(server, "kicad_list_tool_categories", {})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_benchmark_latency.py:31:    output_path = os.environ.get("KICAD_MCP_BENCHMARK_JSON")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_benchmark_latency.py:35:        path.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:8:from kicad_mcp.config import KiCadMCPConfig, get_config
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:12:def test_config_reads_env_vars(sample_project: Path, monkeypatch) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:13:    monkeypatch.setenv("KICAD_MCP_LOG_LEVEL", "DEBUG")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:14:    cfg = KiCadMCPConfig()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:20:    cfg = KiCadMCPConfig()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:27:    cfg = KiCadMCPConfig()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:34:    cfg = KiCadMCPConfig(mount_path="api/")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:40:    cfg = KiCadMCPConfig(cors_origins="https://example.com,http://localhost:3334")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:44:        KiCadMCPConfig(cors_origins="*")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:46:    vscode_cfg = KiCadMCPConfig(cors_origins="vscode-webview://panel")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:50:        KiCadMCPConfig(cors_origins="file://panel")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:56:    (explicit_project / "explicit.kicad_pro").write_text("{}", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:57:    (explicit_project / "explicit.kicad_pcb").write_text("(kicad_pcb)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:58:    (explicit_project / "explicit.kicad_sch").write_text("(kicad_sch)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:62:    (watch_project / "demo.kicad_pro").write_text("{}", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:63:    (watch_project / "demo.kicad_pcb").write_text("(kicad_pcb)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:64:    (watch_project / "demo.kicad_sch").write_text("(kicad_sch)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:66:    monkeypatch.setenv("KICAD_MCP_PROJECT_DIR", str(explicit_project))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:80:        (project / f"{project.name}.kicad_pro").write_text("{}", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:81:        (project / f"{project.name}.kicad_pcb").write_text("(kicad_pcb)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_config.py:82:        (project / f"{project.name}.kicad_sch").write_text("(kicad_sch)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:12:class FakeMCP:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:68:    (tmp_path / "demo.kicad_pro").write_text("{}", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:69:    (tmp_path / "demo.kicad_pcb").write_text("(kicad_pcb)", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:79:    analysis = PlacementAnalysis(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:129:        "kicad_mcp.tools.validation._placement_analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:130:        lambda: (analysis, None),
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:137:    mcp = FakeMCP()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:200:    mcp = FakeMCP()
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:222:        "kicad_mcp.tools.validation._placement_analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:231:        "kicad_mcp.tools.validation._placement_analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:236:        == "Placement score: BLOCKED\n- Placement analysis returned no data."
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_board_state_resources.py:240:        "kicad_mcp.tools.validation._placement_analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_intent_model.py:221:def test_thermal_envelope_defaults() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:21:    base.write_text("* deck\nR1 in out 1k\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:32:    data.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:72:    configured.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:85:    data.write_text("* comment\n0 1.0\n1 2.0\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:91:    empty.write_text("* only comments\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:96:    non_numeric.write_text("time out\nnot numbers\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:106:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:108:    netlist.write_text("* deck\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:171:    cli.write_text("", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:173:    netlist.write_text("* deck\nV1 in 0 5\nR1 in out 1k\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:182:        data_path.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:186:        log_path.write_text("ngspice ok\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:187:        raw_path.write_text("raw\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:200:    result = NgspiceRunner().run_transient_analysis(
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:215:def test_ngspice_runner_cli_builds_and_parses_all_analysis_modes(tmp_path: Path) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:218:    netlist.write_text("* deck\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_ngspice.py:295:    netlist.write_text("* deck\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_component_search.py:217:    monkeypatch.delenv("NEXAR_CLIENT_ID", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_component_search.py:218:    monkeypatch.delenv("NEXAR_CLIENT_SECRET", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_component_search.py:224:    monkeypatch.delenv("DIGIKEY_CLIENT_ID", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_component_search.py:225:    monkeypatch.delenv("DIGIKEY_CLIENT_SECRET", raising=False)
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_impedance.py:20:def test_microstrip_impedance_matches_expected_envelope() -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:13:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:14:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:16:    result = await call_tool_text(server, "sch_set_hop_over", {"enabled": False})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:28:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:29:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:31:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:48:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:49:        "route_create_tuning_profile",
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:63:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:80:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:81:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:84:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:94:    listing = json.loads(await call_tool_text(server, "drc_list_rules", {}))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:96:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:100:    relisted = json.loads(await call_tool_text(server, "drc_list_rules", {}))
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:103:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:126:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:127:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:129:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:147:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_kicad10_parity_tools.py:157:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:107:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:108:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:110:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:116:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:121:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:126:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:131:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:136:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:141:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:146:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:151:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:156:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:180:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:181:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:184:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_emc_tools.py:189:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:13:async def test_dfm_profile_load_run_and_cost(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:21:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:41:            sample_project / "output" / "dfm_profile_check.json",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:50:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:51:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:54:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:55:        "dfm_load_manufacturer_profile",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:58:    report = await call_tool_text(server, "dfm_run_manufacturer_check", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:60:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:65:    assert "Active profile: JLCPCB / standard" in loaded
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:75:async def test_legacy_dfm_validation_uses_profile_backend(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:86:            sample_project / "output" / "dfm_profile_check.json",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:95:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:96:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:98:    jlcpcb = await call_tool_text(server, "check_design_for_manufacture", {"jlcpcb": True})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:99:    generic = await call_tool_text(server, "check_design_for_manufacture", {"jlcpcb": False})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:101:    assert "DFM check (JLCPCB profile):" in jlcpcb
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_dfm_tools.py:103:    assert "DFM check (generic profile):" in generic
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:12:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:85:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:89:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:138:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:139:    text = await call_tool_text(server, "pcb_get_board_summary", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:148:    monkeypatch.setenv("KICAD_MCP_MAX_TEXT_RESPONSE_CHARS", "1000")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:193:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:195:    tracks = await call_tool_text(server, "pcb_get_tracks", {"filter_layer": "F_Cu"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:196:    track_page = await call_tool_text(server, "pcb_get_tracks", {"page": 2, "page_size": 1})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:197:    vias = await call_tool_text(server, "pcb_get_vias", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:198:    footprints = await call_tool_text(server, "pcb_get_footprints", {"filter_layer": "B_Cu"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:199:    nets = await call_tool_text(server, "pcb_get_nets", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:200:    zones = await call_tool_text(server, "pcb_get_zones", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:201:    shapes = await call_tool_text(server, "pcb_get_shapes", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:202:    pads = await call_tool_text(server, "pcb_get_pads", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:203:    layers = await call_tool_text(server, "pcb_get_layers", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:204:    selection = await call_tool_text(server, "pcb_get_selection", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:205:    board_text = await call_tool_text(server, "pcb_get_board_as_string", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:206:    ratsnest = await call_tool_text(server, "pcb_get_ratsnest", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:225:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:226:    await server.call_tool(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:243:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:245:    await server.call_tool(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:281:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:284:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:310:    result = await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:338:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:340:    result = await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:370:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:372:    result = await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:408:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:410:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:427:    result = await call_tool_text(server, "pcb_sync_from_schematic", {"force": True})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:442:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:445:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:473:    result = await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:490:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:514:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:517:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:534:    result = await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:563:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:566:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:592:    result = await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:622:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:625:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:650:    await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:652:    result = await call_tool_text(server, "pcb_transfer_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:680:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:683:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:708:    await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:712:    pcb_path.write_text(pcb_text.replace('(net "GND")', '(net "BROKEN")', 1), encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:714:    result = await call_tool_text(server, "pcb_transfer_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:731:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:755:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:758:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:776:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:797:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:800:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:826:    await call_tool_text(server, "pcb_sync_from_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:845:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:852:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:855:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:882:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:903:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:910:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:913:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:933:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:942:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:945:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:970:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:978:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:981:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1005:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1007:    result = await call_tool_text(server, "pcb_add_mounting_holes", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1022:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1024:    result = await call_tool_text(server, "pcb_add_fiducial_marks", {"count": 3})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1038:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1039:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1040:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1049:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1081:    empty_blocks = await call_tool_text(server, "pcb_block_list", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1083:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1088:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1092:    listed = await call_tool_text(server, "pcb_block_list", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1094:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1099:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1104:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1116:    layers = await call_tool_text(server, "pcb_get_footprint_layers", {"reference": "R1"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1134:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1137:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1152:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1155:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1203:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1205:    result = await call_tool_text(server, "pcb_add_teardrops", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1214:async def test_pcb_set_design_rules_writes_board_level_constraints(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1218:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1219:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1222:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1252:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1253:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1256:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1296:    stackup = await call_tool_text(server, "pcb_get_stackup", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1298:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1304:    state_text = (sample_project / "output" / "stackup_profile.json").read_text(encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1322:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1325:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1336:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1385:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_tools.py:1388:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:21:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:22:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:25:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:32:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:38:    (sample_project / "demo.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:44:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:48:    checkpoints_text = await call_tool_text(server, "vcs_list_checkpoints", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:50:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:55:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:77:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:78:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:79:    await call_tool_text(server, "vcs_init_git", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:81:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:95:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:110:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:111:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:112:    await call_tool_text(server, "vcs_init_git", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:114:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_version_control_tools.py:125:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:5:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:11:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:13:    first = await get_prompt_text(server, "first_pcb", {"component_count": "5"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:14:    schematic = await get_prompt_text(server, "schematic_to_pcb", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:16:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:20:    post_route = await get_prompt_text(server, "post_placement_routing", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:21:    manufacturing = await get_prompt_text(server, "manufacturing_export", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:22:    review = await get_prompt_text(server, "design_review_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:23:    blocking = await get_prompt_text(server, "fix_blocking_issues", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:24:    release = await get_prompt_text(server, "manufacturing_release_checklist", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:25:    high_speed = await get_prompt_text(server, "high_speed_review_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:26:    bringup = await get_prompt_text(server, "new_board_bringup", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:27:    dfm = await get_prompt_text(server, "dfm_polish_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:28:    regression = await get_prompt_text(server, "regression_sweep", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_prompt_workflows.py:41:    assert "manufacturer profile" in dfm
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:72:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:73:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:76:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:86:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:96:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:106:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:111:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:116:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:127:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:154:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:155:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:158:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:163:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:168:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:173:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:178:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_power_integrity_tools.py:183:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:10:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:17:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:19:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:24:    labels = await call_tool_text(server, "sch_get_labels", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:30:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:33:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:39:    labels = await call_tool_text(server, "sch_get_labels", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:49:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:52:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:57:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:62:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:67:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:72:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:77:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:81:    hop = await call_tool_text(server, "sch_set_hop_over", {"enabled": True})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:82:    labels = await call_tool_text(server, "sch_get_labels", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:83:    nets = await call_tool_text(server, "sch_get_net_names", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:84:    wires = await call_tool_text(server, "sch_get_wires", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:112:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:115:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:131:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:134:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:150:async def test_schematic_end_to_end_editing_and_analysis_tools(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:154:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:156:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:184:    symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:186:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:191:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:195:    swappable = await call_tool_text(server, "sch_list_swappable_pins", {"component_ref": "R1"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:197:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:202:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:207:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:211:    connectivity = await call_tool_text(server, "sch_get_connectivity_graph", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:212:    trace = await call_tool_text(server, "sch_trace_net", {"net_name": "MID"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:213:    bounding = await call_tool_text(server, "sch_get_bounding_boxes", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:215:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:219:    resized = await call_tool_text(server, "sch_set_sheet_size", {"paper": "A3"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:220:    invalid_resize = await call_tool_text(server, "sch_set_sheet_size", {"paper": "BAD"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:221:    auto_resize = await call_tool_text(server, "sch_auto_resize_sheet", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:223:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:228:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:233:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:237:    annotated = await call_tool_text(server, "sch_annotate", {"start_number": 10, "order": "sheet"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:241:    deleted_wire = await call_tool_text(server, "sch_delete_wire", {"wire_id": wire_id.group(1)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:242:    missing_wire = await call_tool_text(server, "sch_delete_wire", {"wire_id": "missing"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:243:    deleted_symbol = await call_tool_text(server, "sch_delete_symbol", {"reference": "R10"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:244:    missing_symbol = await call_tool_text(server, "sch_delete_symbol", {"reference": "R404"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:245:    reload_result = await call_tool_text(server, "sch_reload", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:277:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:280:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:319:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:322:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:371:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:374:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:408:    assert "Net compilation analysis:" in result
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:420:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:423:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:461:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:464:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:497:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:500:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:521:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:524:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:538:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:541:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:555:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:558:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:582:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:585:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:605:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:608:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:624:    symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:633:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:636:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:657:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:660:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:706:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:709:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:763:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:766:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:815:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:816:    await server.call_tool(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:830:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:839:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:840:    await server.call_tool(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:855:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:871:    (sample_project / "demo.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:898:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:900:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:920:    (symbol_dir / "Connector_Audio.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:938:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:940:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:961:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:964:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1003:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1006:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1014:    listing = await call_tool_text(server, "sch_list_sheets", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1018:    info = await call_tool_text(server, "sch_get_sheet_info", {"sheet_name": "Power"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1029:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1032:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1037:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1054:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1057:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1084:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1089:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1094:    graph = await call_tool_text(server, "sch_get_connectivity_graph", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1106:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1109:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1114:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1119:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1143:    (sample_project / "power.kicad_sch").write_text(child_template, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1144:    (sample_project / "control.kicad_sch").write_text(child_template, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1146:    trace = await call_tool_text(server, "sch_trace_net", {"net_name": "VIN"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1160:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1163:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1190:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1194:    symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1203:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1206:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1224:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1228:    symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1238:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1241:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1267:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1272:    wires = await call_tool_text(server, "sch_get_wires", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1277:    result = await call_tool_text(server, "sch_delete_wire", {"wire_id": wire_id[:8]})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1278:    wires_after = await call_tool_text(server, "sch_get_wires", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1288:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1291:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1317:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1322:    result = await call_tool_text(server, "sch_delete_symbol", {"reference": "R1"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1323:    symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1324:    wires = await call_tool_text(server, "sch_get_wires", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1337:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1339:    listing = await call_tool_text(server, "sch_list_templates", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1341:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1346:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1367:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1373:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1393:    (symbols_dir / "LongPins.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1407:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1409:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1422:    boxes = await call_tool_text(server, "sch_get_bounding_boxes", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1433:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1436:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1473:    (symbols_dir / "STM32.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1478:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1480:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1520:    result = await call_tool_text(server, "sch_auto_place_functional", arguments)
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1540:    (symbols_dir / "STM32.kicad_sym").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1545:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1547:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1585:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1589:    await call_tool_text(server, "sch_set_sheet_size", {"paper": "A3"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1591:    result = await call_tool_text(server, "sch_auto_place_functional", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1605:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1607:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1618:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1620:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1636:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1638:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1648:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1650:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1660:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1662:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1672:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1674:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_tools.py:1701:    sch_file = next(Path(os.environ["KICAD_MCP_PROJECT_DIR"]).glob("*.kicad_sch"))
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:39:def _write_board(sample_project: Path, *footprints: str) -> None:
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:40:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:55:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:56:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:59:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:76:    fetched = await call_tool_text(server, "project_get_design_intent", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:97:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:128:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:129:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:131:    payload = await call_tool_payload(server, "project_get_design_spec", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:149:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:153:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:154:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:155:    await call_tool_text(server, "project_set_design_intent", {"connector_refs": ["J1"]})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:157:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:158:    score = await call_tool_text(server, "pcb_score_placement", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:172:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:177:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:178:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:180:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:185:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:197:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:201:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:202:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:204:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:213:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:225:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:257:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:258:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:260:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:274:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:275:    score = await call_tool_text(server, "pcb_score_placement", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:293:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:320:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:321:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:322:    await call_tool_text(server, "project_set_design_intent", {"critical_nets": ["USB_DP"]})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:324:    score = await call_tool_text(server, "pcb_score_placement", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:336:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:341:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:342:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:343:    await call_tool_text(server, "project_set_design_intent", {"thermal_hotspots": ["U1", "U2"]})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:345:    score = await call_tool_text(server, "pcb_score_placement", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:358:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:364:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:365:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:367:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:372:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:373:    score = await call_tool_text(server, "pcb_score_placement", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:386:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:391:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:392:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:394:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:399:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:411:    _write_board(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:413:        _footprint_block("U1", "AFE", 10.0, 10.0, name="Amplifier_Operational:MCP6002"),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:416:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:417:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:419:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_placement_quality_gate.py:424:    gate = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:94:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:95:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:98:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:110:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:122:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:127:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:132:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:143:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:148:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:153:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:161:    assert "Differential-pair skew analysis" in skew
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:167:    assert "Via stub analysis at 5.000 GHz" in via_stub
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:179:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:180:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:197:    materials = await call_tool_text(server, "si_list_dielectric_materials", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:199:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:204:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:211:    def fake_write_rule(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:220:    monkeypatch.setattr("kicad_mcp.tools.signal_integrity._write_nc_rule", fake_write_rule)
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:222:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_signal_integrity_tools.py:227:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:25:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:26:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:45:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:63:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:64:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:82:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:95:async def test_project_auto_fix_loop_applies_server_fix_and_reports_remaining_action(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:99:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:100:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:119:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:139:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:140:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:149:    await call_tool_text(server, "project_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:151:    trend = await call_tool_text(server, "project_gate_trend", {"gate_name": "Placement"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_validation_loop.py:152:    report = await call_tool_payload(server, "project_design_report", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:9:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:29:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:31:    text = await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:36:    info = await call_tool_text(server, "kicad_get_project_info", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:37:    scan = await call_tool_text(server, "kicad_scan_directory", {"path": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:38:    recent = await call_tool_text(server, "kicad_list_recent_projects", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:39:    version = await call_tool_text(server, "kicad_get_version", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:40:    help_text = await call_tool_text(server, "kicad_help", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:41:    categories = await call_tool_text(server, "kicad_list_tool_categories", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:43:        server, "kicad_get_tools_in_category", {"category": "project"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:46:        server, "kicad_get_tools_in_category", {"category": "library"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:49:        server, "kicad_get_tools_in_category", {"category": "routing"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:52:        server, "kicad_get_tools_in_category", {"category": "pcb_read"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:54:    pcb_write_tools = await call_tool_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:55:        server, "kicad_get_tools_in_category", {"category": "pcb_write"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:58:        server, "kicad_get_tools_in_category", {"category": "simulation"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:61:        server, "kicad_get_tools_in_category", {"category": "signal_integrity"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:64:        server, "kicad_get_tools_in_category", {"category": "power_integrity"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:66:    emc_tools = await call_tool_text(server, "kicad_get_tools_in_category", {"category": "emc"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:67:    dfm_tools = await call_tool_text(server, "kicad_get_tools_in_category", {"category": "dfm"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:69:        server, "kicad_get_tools_in_category", {"category": "version_control"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:72:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:80:    assert "KiCad MCP Pro Server" in version
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:87:    assert "analysis" in categories
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:94:    assert "pcb_auto_place_by_schematic" in pcb_write_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:95:    assert "pcb_set_stackup" in pcb_write_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:96:    assert "pcb_add_blind_via" in pcb_write_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:97:    assert "pcb_add_microvia" in pcb_write_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:98:    assert "pcb_set_keepout_zone" in pcb_write_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:99:    assert "pcb_add_teardrops" in pcb_write_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:117:    assert "dfm_load_manufacturer_profile" in dfm_tools
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:126:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:132:    project_resource = await read_resource_text(server, "kicad://project/info")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:133:    project_manifest_resource = await read_resource_text(server, "kicad://project/manifest")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:134:    project_spec_resource = await read_resource_text(server, "kicad://project/spec")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:136:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:139:    project_next_action_resource = await read_resource_text(server, "kicad://project/next_action")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:140:    board_summary = await read_resource_text(server, "kicad://board/summary")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:141:    board_netlist = await read_resource_text(server, "kicad://board/netlist")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:142:    quality_gate_resource = await read_resource_text(server, "kicad://project/quality_gate")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:143:    gate_history_resource = await read_resource_text(server, "kicad://project/gate_history")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:144:    fix_queue_resource = await read_resource_text(server, "kicad://project/fix_queue")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:145:    connectivity_resource = await read_resource_text(server, "kicad://schematic/connectivity")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:146:    layer_coverage_resource = await read_resource_text(server, "kicad://board/layer_coverage")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:147:    placement_resource = await read_resource_text(server, "kicad://board/placement_quality")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:148:    placement_gate_resource = await read_resource_text(server, "kicad://gate/placement")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:150:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:154:    schematic_to_pcb = await get_prompt_text(server, "schematic_to_pcb", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:155:    manufacturing = await get_prompt_text(server, "manufacturing_export", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:156:    design_review_loop = await get_prompt_text(server, "design_review_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:157:    fix_blocking_issues = await get_prompt_text(server, "fix_blocking_issues", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:158:    release_checklist = await get_prompt_text(server, "manufacturing_release_checklist", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:159:    high_speed_review = await get_prompt_text(server, "high_speed_review_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:160:    new_board = await get_prompt_text(server, "new_board_bringup", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:161:    dfm_polish = await get_prompt_text(server, "dfm_polish_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:162:    regression = await get_prompt_text(server, "regression_sweep", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:183:    assert "broader profile" in manufacturing
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:193:    assert "broader profile" in release_checklist
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:196:    assert "manufacturer profile" in dfm_polish.lower()
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:199:    design_spec = await call_tool_payload(server, "project_get_design_spec", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:200:    design_spec_validation = await call_tool_payload(server, "project_validate_design_spec", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:201:    next_action = await call_tool_payload(server, "project_get_next_action", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:202:    placement_report = await call_tool_payload(server, "pcb_placement_quality_report", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:203:    gate_report = await call_tool_payload(server, "project_quality_gate_report", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:217:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:306:    libraries = await call_tool_text(server, "lib_list_libraries", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:307:    symbols = await call_tool_text(server, "lib_search_symbols", {"query": "resistor"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:309:        server, "lib_get_symbol_info", {"library": "Device", "symbol_name": "R"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:311:    footprints = await call_tool_text(server, "lib_search_footprints", {"query": "0805"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:313:        server, "lib_list_footprints", {"library": "Resistor_SMD"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:315:    rebuild = await call_tool_text(server, "lib_rebuild_index", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:317:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:322:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:327:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:332:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:337:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:342:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:357:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:362:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:367:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:372:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:377:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:416:    server = build_server("library")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:417:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:422:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:441:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:443:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:445:    no_symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:446:    no_wires = await call_tool_text(server, "sch_get_wires", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:447:    no_labels = await call_tool_text(server, "sch_get_labels", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:448:    no_nets = await call_tool_text(server, "sch_get_net_names", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:457:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:471:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:476:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:481:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:486:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:491:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:495:        call_tool_text(server, "sch_add_no_connect", {"x_mm": 25.0, "y_mm": 25.0}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:501:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:506:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:510:    symbols = await call_tool_text(server, "sch_get_symbols", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:511:    wire_text = await call_tool_text(server, "sch_get_wires", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:512:    labels = await call_tool_text(server, "sch_get_labels", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:513:    nets = await call_tool_text(server, "sch_get_net_names", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:515:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:519:    power = await call_tool_text(server, "sch_check_power_flags", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:520:    annotated = await call_tool_text(server, "sch_annotate", {"start_number": 1, "order": "sheet"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:522:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_project_library_surface.py:542:    reload_text = await call_tool_text(server, "sch_reload", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:14:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:15:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:18:        server, "kicad_get_tools_in_category", {"category": "simulation"}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:21:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:34:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:44:    netlist.write_text("* deck\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:51:                analysis="operating-point",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:56:        def run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:69:                analysis="ac",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:78:        def run_transient_analysis(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:90:                analysis="transient",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:111:                analysis="dc",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:119:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:120:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:122:    op = await call_tool_text(server, "sim_run_operating_point", {"netlist_path": "custom.cir"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:124:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:125:        "sim_run_ac_analysis",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:135:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:145:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:157:    assert "Operating point analysis" in op
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:159:    assert "AC analysis" in ac
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:161:    assert "Transient analysis" in tran
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:163:    assert "DC sweep analysis" in sweep
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:170:    netlist.write_text("* deck\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:173:        def run_ac_analysis(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:186:                analysis="ac",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:205:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:206:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:209:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:233:        out_file.write_text("* exported\n.end\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:242:                analysis="operating-point",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:249:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:250:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:252:    text = await call_tool_text(server, "sim_run_operating_point", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_simulation_tools.py:254:    assert "Operating point analysis" in text
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:89:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:90:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:92:    libs = await call_tool_text(server, "lib_list_libraries", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:93:    symbols = await call_tool_text(server, "lib_search_symbols", {"query": "resistor"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:95:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:100:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:104:    footprints = await call_tool_text(server, "lib_search_footprints", {"query": "0805"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:106:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:111:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:116:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:121:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:126:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:131:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:136:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:141:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:146:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:151:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:162:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:167:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:197:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:198:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:225:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:230:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:235:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:240:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:244:    bom = await call_tool_text(server, "lib_get_bom_with_pricing", {"quantity": 3})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:245:    bad_qty = await call_tool_text(server, "lib_get_bom_with_pricing", {"quantity": 0})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:246:    stock = await call_tool_text(server, "lib_check_stock_availability", {"refs": ["U1", "D1"]})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:247:    no_refs = await call_tool_text(server, "lib_check_stock_availability", {"refs": []})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:249:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:254:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:259:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:264:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:296:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:297:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:311:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:323:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:332:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:337:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:342:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_library_tools_extended.py:352:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:8:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:18:    (sample_project / "demo.dsn").write_text(f"(pcb\n{nets}\n)\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:35:        ses_path.write_text("ses", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:40:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:41:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:44:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:64:async def test_routing_rule_tools_write_state_and_dru_files(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:68:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:69:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:81:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:92:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:97:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:102:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:107:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:111:    profile = await call_tool_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:112:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:113:        "route_create_tuning_profile",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:121:    profiles = await call_tool_text(server, "route_list_tuning_profiles", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:123:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:124:        "route_apply_tuning_profile",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:125:        {"net_pattern": "DATA*", "profile_name": "fast"},
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:127:    missing_profile = await call_tool_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:128:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:129:        "route_apply_tuning_profile",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:130:        {"net_pattern": "DATA*", "profile_name": "slow"},
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:133:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:144:    assert "saved" in profile
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:145:    assert '"fast"' in profiles
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_routing_tools.py:147:    assert "was not found" in missing_profile
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:13:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:130:            (output_path / "demo-F_Cu.gbr").write_text("gerber", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:134:            (output_path / "demo.drl").write_text("drill", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:138:            output_path.write_text("Ref,Value\nR1,10k\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:142:            output_path.write_text("(export netlist)", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:146:            output_path.write_text("pdf", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:150:            output_path.write_text("step", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:154:            output_path.write_text("png", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:158:            output_path.write_text("ref,x,y\nR1,1,2\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:162:            output_path.write_text("<ipc2581/>", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:166:            (output_path / "board.svg").write_text("<svg/>", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:170:            (output_path / "board.dxf").write_text("0\nSECTION\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:174:            output_path.write_text("Board size: 50 x 50 mm", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:178:            output_path.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:196:            output_path.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:222:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:223:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:224:    (sample_project / "demo.dsn").write_text("dsn", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:247:        ses_path.write_text("ses", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:255:    summary = await call_tool_text(server, "pcb_get_board_summary", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:256:    tracks = await call_tool_text(server, "pcb_get_tracks", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:257:    vias = await call_tool_text(server, "pcb_get_vias", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:258:    footprints = await call_tool_text(server, "pcb_get_footprints", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:259:    nets = await call_tool_text(server, "pcb_get_nets", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:260:    zones = await call_tool_text(server, "pcb_get_zones", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:261:    shapes = await call_tool_text(server, "pcb_get_shapes", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:262:    pads = await call_tool_text(server, "pcb_get_pads", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:263:    layers = await call_tool_text(server, "pcb_get_layers", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:264:    stackup = await call_tool_text(server, "pcb_get_stackup", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:265:    selection = await call_tool_text(server, "pcb_get_selection", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:266:    board_text = await call_tool_text(server, "pcb_get_board_as_string", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:267:    ratsnest = await call_tool_text(server, "pcb_get_ratsnest", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:268:    rules = await call_tool_text(server, "pcb_get_design_rules", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:287:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:300:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:305:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:310:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:315:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:320:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:325:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:330:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:334:        await call_tool_text(server, "pcb_delete_items", {"item_ids": ["abc-def"]}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:335:        await call_tool_text(server, "pcb_save", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:336:        await call_tool_text(server, "pcb_refill_zones", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:337:        await call_tool_text(server, "pcb_highlight_net", {"net_name": "NET1"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:339:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:344:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:349:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:354:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:359:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:374:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:379:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:388:        await call_tool_text(server, "route_import_ses", {"ses_path": "output/routing/board.ses"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:390:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:401:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:413:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:422:            server, "tune_track_length", {"net_name": "NET1", "target_length_mm": 5.0}
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:425:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:448:    server = build_server("pcb")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:449:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:452:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:457:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:462:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:509:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:510:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:513:        await call_tool_text(server, "export_gerber", {"output_subdir": "gerber", "layers": []}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:514:        await call_tool_text(server, "export_drill", {"output_subdir": "gerber"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:515:        await call_tool_text(server, "export_bom", {"format": "csv"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:516:        await call_tool_text(server, "export_netlist", {"format": "kicad"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:517:        await call_tool_text(server, "export_spice_netlist", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:518:        await call_tool_text(server, "export_pcb_pdf", {"layers": ["F.Cu"]}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:519:        await call_tool_text(server, "export_sch_pdf", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:520:        await call_tool_text(server, "export_step", {"output_path": ""}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:521:        await call_tool_text(server, "export_3d_step", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:523:            server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:527:        await call_tool_text(server, "export_pick_and_place", {"format": "csv"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:528:        await call_tool_text(server, "export_ipc2581", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:529:        await call_tool_text(server, "export_svg", {"layer": "F.Cu"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:530:        await call_tool_text(server, "export_dxf", {"layer": "Edge.Cuts"}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:531:        await call_tool_text(server, "get_board_stats", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:532:        await call_tool_text(server, "export_manufacturing_package", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:533:        await call_tool_text(server, "run_drc", {"save_report": True}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:534:        await call_tool_text(server, "run_erc", {"save_report": True}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:535:        await call_tool_text(server, "validate_design", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:536:        await call_tool_text(server, "schematic_quality_gate", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:537:        await call_tool_text(server, "schematic_connectivity_gate", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:538:        await call_tool_text(server, "pcb_quality_gate", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:539:        await call_tool_text(server, "pcb_placement_quality_gate", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:540:        await call_tool_text(server, "pcb_score_placement", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:541:        await call_tool_text(server, "manufacturing_quality_gate", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:542:        await call_tool_text(server, "project_quality_gate", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:543:        await call_tool_text(server, "check_design_for_manufacture", {"jlcpcb": True}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:544:        await call_tool_text(server, "check_design_for_manufacture", {"jlcpcb": False}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:545:        await call_tool_text(server, "get_unconnected_nets", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:546:        await call_tool_text(server, "get_courtyard_violations", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:547:        await call_tool_text(server, "get_silk_to_pad_violations", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_pcb_export_validation_surface.py:548:        await call_tool_text(server, "validate_footprints_vs_schematic", {}),
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:9:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:18:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:19:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:22:    missing = await call_tool_text(server, "mfg_panelize", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:23:    assert "KiKit is not installed" in missing
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:26:    invalid_layout = await call_tool_text(server, "mfg_panelize", {"layout": "radial"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:27:    invalid_size = await call_tool_text(server, "mfg_panelize", {"rows": 0, "cols": 2})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:38:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:39:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:49:    dry_run = await call_tool_text(server, "mfg_panelize", {"layout": "grid"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:51:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:56:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:61:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:79:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:91:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:102:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:103:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:105:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:116:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:127:    (output_dir / "demo-F_Cu.gbr").write_text("gerber", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:128:    (output_dir / "demo.drl").write_text("drill", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:129:    manifest = await call_tool_text(server, "mfg_generate_release_manifest", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:135:    cpl.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:140:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:145:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:161:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:162:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:171:    supported = await call_tool_text(server, "mfg_check_import_support", {"format": "allegro"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:172:    unknown = await call_tool_text(server, "mfg_check_import_support", {"format": "eagle"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:179:    allegro.write_text("legacy", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:187:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:198:    failed = await call_tool_text(server, "mfg_import_pads", {"pads_pcb_path": "legacy.brd"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_manufacturing_tools.py:199:    missing = await call_tool_text(server, "mfg_import_geda", {"geda_pcb_path": "missing.pcb"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:58:    top_file.write_text(updated, encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:67:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:68:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:71:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:97:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:102:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:107:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:112:    text = await call_tool_text(server, "schematic_connectivity_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:126:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:127:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:130:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:156:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:161:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:166:    text = await call_tool_text(server, "schematic_connectivity_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:180:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:181:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:183:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:189:    (sample_project / "power.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:194:    text = await call_tool_text(server, "schematic_connectivity_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:206:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:207:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:209:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:215:    (sample_project / "power.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:220:    text = await call_tool_text(server, "schematic_connectivity_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:278:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:279:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:282:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:308:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:313:    text = await call_tool_text(server, "project_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:325:    server = build_server("schematic")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:326:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_schematic_connectivity_gate.py:356:    text = await call_tool_text(server, "schematic_connectivity_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:9:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:21:        (out_dir / "demo-F_Cu.gbr").write_text("gerber", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:47:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:48:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:49:    text = await call_tool_text(server, "export_gerber", {"output_subdir": "gerber", "layers": []})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:76:        (out_dir / "demo-F_Cu.gbr").write_text("gerber", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:92:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:93:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:94:    text = await call_tool_text(server, "export_gerber", {"output_subdir": "gerber", "layers": []})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:117:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:118:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:120:    gerber = await call_tool_text(server, "export_gerber", {"output_subdir": "../escape"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:122:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:126:    render = await call_tool_text(server, "export_3d_render", {"output_file": "nested/render.png"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:128:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:173:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:174:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:176:    step = await call_tool_text(server, "export_step", {"output_path": "board.step"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:177:    render = await call_tool_text(server, "export_3d_render", {"output_file": "render.png"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:201:            out_file.write_text("pdf", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:205:            out_file.write_text("ref,value\nR1,10k\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:233:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:234:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:235:    await call_tool_text(server, "variant_create", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:236:    await call_tool_text(server, "variant_set_active", {"name": "lite"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:238:    pdf_result = await call_tool_text(server, "pcb_export_3d_pdf", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:239:    bom_result = await call_tool_text(server, "export_bom", {"format": "csv"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:255:            (out_dir / "demo-F_Cu.gbr").write_text("gerber", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:259:            (out_dir / "demo.drl").write_text("drill", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:262:            (output_path / "bom.csv").write_text("ref,value\nR1,10k\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:289:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:290:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:293:        server,
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:297:    drill = await call_tool_text(server, "export_drill", {"output_subdir": "gerber"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:298:    bom = await call_tool_text(server, "export_bom", {"format": "csv"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:310:    (sample_project / "second.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:333:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:334:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:336:    bom = await call_tool_text(server, "export_bom", {"format": "csv"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:349:        report_path.write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:384:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:385:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:386:    text = await call_tool_text(server, "run_drc", {"save_report": True})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:419:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:420:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:422:    text = await call_tool_text(server, "run_erc", {"save_report": True})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:508:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:509:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:511:    text = await call_tool_text(server, "project_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:544:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:545:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:547:    text = await call_tool_text(server, "export_manufacturing_package", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:560:    (sample_project / "demo.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:582:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:602:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:603:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:605:    text = await call_tool_text(server, "validate_footprints_vs_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:617:    (sample_project / "second.kicad_sch").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:621:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:646:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:647:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:649:    text = await call_tool_text(server, "validate_footprints_vs_schematic", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:658:    (sample_project / "demo.kicad_pcb").write_text(
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:686:    server = build_server("manufacturing")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:687:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:689:    text = await call_tool_text(server, "pcb_placement_quality_gate", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:727:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:728:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:730:    text = await call_tool_text(server, "export_pcb_pdf", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:755:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:756:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:758:    text = await call_tool_text(server, "export_pcb_pdf", {"layers": ["F.Cu", "Edge.Cuts"]})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:775:        out_path.write_text("(export (version D))\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:786:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:787:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:789:    text = await call_tool_text(server, "export_netlist", {"format": "kicad"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:807:        (out_dir / "board.svg").write_text("<svg />\n", encoding="utf-8")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:833:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:834:    await call_tool_text(server, "kicad_set_project", {"project_dir": str(sample_project)})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_export_tools.py:836:    text = await call_tool_text(server, "export_svg", {"layer": "Edge.Cuts"})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:7:from kicad_mcp.server import build_server
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:29:                summary="A DFM profile is not configured.",
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:30:                details=["Load a manufacturer profile before release."],
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:35:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:36:    await read_resource_text(server, "kicad://project/info")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:38:    queue = await read_resource_text(server, "kicad://project/fix_queue")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:41:    assert "1. [critical] Manufacturing: Load a manufacturer profile before release." in queue
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:49:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:51:    review = await get_prompt_text(server, "design_review_loop", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:52:    fix = await get_prompt_text(server, "fix_blocking_issues", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:53:    release = await get_prompt_text(server, "manufacturing_release_checklist", {})
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:81:    server = build_server("full")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:82:    await read_resource_text(server, "kicad://project/info")
03_TOOLS\repos\kicad-mcp-pro\tests\integration\test_health_surface.py:84:    queue = await read_resource_text(server, "kicad://project/fix_queue")
EXIT_CODE: 0
```

## Command

```powershell
rg -n "\[project\]|requires-python|dependencies|scripts|kicad-mcp-pro|health|doctor|server|profile" "03_TOOLS\repos\kicad-mcp-pro\pyproject.toml"
```

### Output

```text
5:[project]
6:name = "kicad-mcp-pro"
8:description = "A professional Model Context Protocol server for KiCad EDA."
38:requires-python = ">=3.12"
39:dependencies = [
52:[project.optional-dependencies]
83:[project.scripts]
84:kicad-mcp-pro = "kicad_mcp.server:main"
87:Homepage = "https://github.com/oaslananka/kicad-mcp-pro"
88:Documentation = "https://oaslananka.github.io/kicad-mcp-pro"
89:Repository = "https://github.com/oaslananka/kicad-mcp-pro"
90:"Bug Tracker" = "https://github.com/oaslananka/kicad-mcp-pro/issues"
91:Changelog = "https://github.com/oaslananka/kicad-mcp-pro/blob/main/CHANGELOG.md"
EXIT_CODE: 0
```

## Command

```powershell
rg -n "uvx|pip install|venv|health|doctor|KICAD_MCP|profile|stdio|server|mcpServers|command|args|env|codex|config.toml" "03_TOOLS\repos\kicad-mcp-pro\README.md" "03_TOOLS\repos\kicad-mcp-pro\docs\installation.md" "03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md" "03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md" "03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml" "03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-http-config.toml" "03_TOOLS\repos\kicad-mcp-pro\.env.example" "03_TOOLS\repos\kicad-mcp-pro\mcp.json" "03_TOOLS\repos\kicad-mcp-pro\server.json"
```

### Output

```text
03_TOOLS\repos\kicad-mcp-pro\server.json:2:  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
03_TOOLS\repos\kicad-mcp-pro\server.json:5:  "description": "A professional Model Context Protocol server for KiCad EDA.",
03_TOOLS\repos\kicad-mcp-pro\server.json:18:        "type": "stdio"
03_TOOLS\repos\kicad-mcp-pro\mcp.json:4:  "description": "Compatibility metadata for KiCad MCP Pro. Prefer server.json for official MCP Registry publication.",
03_TOOLS\repos\kicad-mcp-pro\mcp.json:11:    "stdio",
03_TOOLS\repos\kicad-mcp-pro\.env.example:1:# KiCad MCP Pro Server environment configuration
03_TOOLS\repos\kicad-mcp-pro\.env.example:4:# KICAD_MCP_KICAD_CLI=/usr/bin/kicad-cli
03_TOOLS\repos\kicad-mcp-pro\.env.example:6:# KICAD_MCP_FREEROUTING_JAR=/path/to/freerouting.jar
03_TOOLS\repos\kicad-mcp-pro\.env.example:7:# KICAD_MCP_FREEROUTING_IMAGE=ghcr.io/freerouting/freerouting:2.1.0
03_TOOLS\repos\kicad-mcp-pro\.env.example:8:# KICAD_MCP_FREEROUTING_TIMEOUT_SEC=900
03_TOOLS\repos\kicad-mcp-pro\.env.example:9:# KICAD_MCP_DOCKER_EXECUTABLE=docker
03_TOOLS\repos\kicad-mcp-pro\.env.example:10:# KICAD_MCP_JAVA_EXECUTABLE=java
03_TOOLS\repos\kicad-mcp-pro\.env.example:11:# KICAD_MCP_NGSPICE_CLI=/usr/bin/ngspice
03_TOOLS\repos\kicad-mcp-pro\.env.example:14:# KICAD_MCP_KICAD_SOCKET_PATH=/tmp/kicad.sock
03_TOOLS\repos\kicad-mcp-pro\.env.example:15:# KICAD_MCP_KICAD_TOKEN=replace-with-your-kicad-ipc-token
03_TOOLS\repos\kicad-mcp-pro\.env.example:19:# KICAD_MCP_WORKSPACE_ROOT=/path/to/allowed/workspace
03_TOOLS\repos\kicad-mcp-pro\.env.example:20:KICAD_MCP_PROJECT_DIR=/path/to/your/kicad/project
03_TOOLS\repos\kicad-mcp-pro\.env.example:21:# KICAD_MCP_PROJECT_FILE=/path/to/project.kicad_pro
03_TOOLS\repos\kicad-mcp-pro\.env.example:22:# KICAD_MCP_PCB_FILE=/path/to/board.kicad_pcb
03_TOOLS\repos\kicad-mcp-pro\.env.example:23:# KICAD_MCP_SCH_FILE=/path/to/schematic.kicad_sch
03_TOOLS\repos\kicad-mcp-pro\.env.example:24:# KICAD_MCP_OUTPUT_DIR=/path/to/output
03_TOOLS\repos\kicad-mcp-pro\.env.example:27:# KICAD_MCP_SYMBOL_LIBRARY_DIR=/path/to/kicad/symbols
03_TOOLS\repos\kicad-mcp-pro\.env.example:28:# KICAD_MCP_FOOTPRINT_LIBRARY_DIR=/path/to/kicad/footprints
03_TOOLS\repos\kicad-mcp-pro\.env.example:31:# KICAD_MCP_TRANSPORT=stdio
03_TOOLS\repos\kicad-mcp-pro\.env.example:32:# KICAD_MCP_HOST=127.0.0.1
03_TOOLS\repos\kicad-mcp-pro\.env.example:33:# KICAD_MCP_PORT=3334
03_TOOLS\repos\kicad-mcp-pro\.env.example:35:# KICAD_MCP_MOUNT_PATH=/mcp
03_TOOLS\repos\kicad-mcp-pro\.env.example:36:# KICAD_MCP_CORS_ORIGINS=https://app.example.com,http://127.0.0.1:3334
03_TOOLS\repos\kicad-mcp-pro\.env.example:37:# KICAD_MCP_AUTH_TOKEN=replace-with-a-local-bearer-token
03_TOOLS\repos\kicad-mcp-pro\.env.example:38:# KICAD_MCP_LEGACY_SSE=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:39:# KICAD_MCP_STATEFUL_HTTP=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:40:# KICAD_MCP_ENABLE_METRICS=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:41:# KICAD_MCP_STUDIO_WATCH_DIR=/path/to/projects
03_TOOLS\repos\kicad-mcp-pro\.env.example:42:# KICAD_MCP_PROFILE=full
03_TOOLS\repos\kicad-mcp-pro\.env.example:45:# KICAD_MCP_LOG_LEVEL=INFO
03_TOOLS\repos\kicad-mcp-pro\.env.example:46:# KICAD_MCP_LOG_FORMAT=console
03_TOOLS\repos\kicad-mcp-pro\.env.example:49:# KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:50:# KICAD_MCP_IPC_CONNECTION_TIMEOUT=10.0
03_TOOLS\repos\kicad-mcp-pro\.env.example:51:# KICAD_MCP_TIMEOUT_MS=10000
03_TOOLS\repos\kicad-mcp-pro\.env.example:52:# KICAD_MCP_RETRIES=2
03_TOOLS\repos\kicad-mcp-pro\.env.example:53:# KICAD_MCP_HEADLESS=false
03_TOOLS\repos\kicad-mcp-pro\.env.example:54:# KICAD_MCP_CLI_TIMEOUT=120.0
03_TOOLS\repos\kicad-mcp-pro\.env.example:55:# KICAD_MCP_MAX_ITEMS_PER_RESPONSE=200
03_TOOLS\repos\kicad-mcp-pro\.env.example:56:# KICAD_MCP_MAX_TEXT_RESPONSE_CHARS=50000
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-http-config.toml:1:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:1:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:2:command = "uvx"
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:3:args = ["kicad-mcp-pro"]
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:7:[mcp_servers.kicad.env]
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:8:KICAD_MCP_PROJECT_DIR = "/absolute/path/to/your/kicad-project"
03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml:9:KICAD_MCP_PROFILE = "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:7:3. `.env`
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:8:4. `~/.config/kicad-mcp-pro/config.toml`
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:16:kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:17:kicad-mcp-pro doctor --json
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:21:`health --json` is a fast install/configuration check and does not require a
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:22:running KiCad IPC server. `doctor --json` adds deeper KiCad CLI and IPC probes
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:28:Existing `KICAD_MCP_*` variables continue to work. The server also accepts these
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:35:| `KICAD_MCP_TIMEOUT_MS` | IPC timeout in milliseconds |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:36:| `KICAD_MCP_RETRIES` | IPC connection retries |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:37:| `KICAD_MCP_HEADLESS` | Headless preference |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:38:| `KICAD_MCP_WORKSPACE_ROOT` | Workspace root for path safety |
03_TOOLS\repos\kicad-mcp-pro\docs\configuration.md:45:When `KICAD_MCP_WORKSPACE_ROOT` is set, project artifact reads and writes must
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:5:uvx kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:10:pip install kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:15:pip install "kicad-mcp-pro[http]"
03_TOOLS\repos\kicad-mcp-pro\docs\installation.md:18:After installation, add the server to your MCP client. See
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:3:KiCad MCP Pro works with MCP clients that can start a local `stdio` server or connect to a
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:4:Streamable HTTP endpoint. The most portable setup is local `stdio` with `uvx`.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:7:omit `KICAD_MCP_PROJECT_DIR` and call `kicad_set_project()` from the client instead, but
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:12:Use this command in clients that ask for a command and arguments:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:15:command: uvx
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:16:args: ["kicad-mcp-pro"]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:19:Recommended environment:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:22:KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:23:KICAD_MCP_PROFILE=pcb_only
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:26:Use `KICAD_MCP_PROFILE=full` if you want every tool category. Preferred focused profiles are
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:33:VS Code uses `.vscode/mcp.json` for workspace-level configuration and a user profile MCP
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:34:configuration for global setup. GitHub Copilot in VS Code uses the same MCP server setup.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:40:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:42:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:43:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:44:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:45:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:46:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:47:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:54:Use an absolute KiCad project path for `KICAD_MCP_PROJECT_DIR`. Some VS Code MCP setups do
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:55:not expand `${workspaceFolder}` and may fail at server startup.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:59:Codex stores MCP servers in `~/.codex/config.toml` or a trusted project-scoped
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:60:`.codex/config.toml`.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:65:codex mcp add kicad \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:66:  --env KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:67:  --env KICAD_MCP_PROFILE=pcb_only \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:68:  -- uvx kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:71:`~/.codex/config.toml`:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:74:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:75:command = "uvx"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:76:args = ["kicad-mcp-pro"]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:80:[mcp_servers.kicad.env]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:81:KICAD_MCP_PROJECT_DIR = "/absolute/path/to/your/kicad-project"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:82:KICAD_MCP_PROFILE = "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:87:Add the server to `claude_desktop_config.json`:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:91:  "mcpServers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:93:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:94:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:95:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:96:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:97:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:106:Use KiCad MCP Pro 3.0.2 or newer for Claude Code `stdio` setups. That release defers
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:108:on slower WSL or cold KiCad environments.
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:114:  "mcpServers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:116:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:117:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:118:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:119:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:120:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:132:  --env KICAD_MCP_PROJECT_DIR=/absolute/path/to/your/kicad-project \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:133:  --env KICAD_MCP_PROFILE=pcb_only \
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:134:  -- uvx kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:144:  "mcpServers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:146:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:147:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:148:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:149:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:150:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:151:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:160:Add the server to `~/.gemini/settings.json`:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:164:  "mcpServers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:166:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:167:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:168:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:169:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:170:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:180:If your client accepts the common `mcpServers` JSON shape, use this as the starting point:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:184:  "mcpServers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:186:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:187:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:188:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:189:      "env": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:190:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:191:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:198:Client-specific behavior can vary. If the client supports only HTTP servers, use the HTTP
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:203:Start KiCad MCP Pro as an HTTP server:
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:219:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:231:[mcp_servers.kicad]
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:240:  "mcpServers": {
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:251:- VS Code MCP configuration: https://code.visualstudio.com/docs/copilot/customization/mcp-servers
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:252:- Codex MCP configuration: https://developers.openai.com/codex/mcp
03_TOOLS\repos\kicad-mcp-pro\docs\client-configuration.md:256:- Gemini CLI MCP setup notes: https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md
03_TOOLS\repos\kicad-mcp-pro\README.md:12:KiCad MCP Pro is a production-focused Model Context Protocol server for KiCad PCB and schematic workflows. It gives agents project setup, schematic editing, PCB inspection and edits, validation gates, DFM checks, SI/PI helpers, simulation helpers, and release-gated manufacturing export.
03_TOOLS\repos\kicad-mcp-pro\README.md:18:Install and run with `uvx`:
03_TOOLS\repos\kicad-mcp-pro\README.md:21:uvx kicad-mcp-pro --help
03_TOOLS\repos\kicad-mcp-pro\README.md:22:uvx kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\README.md:23:uvx kicad-mcp-pro doctor --json
03_TOOLS\repos\kicad-mcp-pro\README.md:24:uvx kicad-mcp-pro serve
03_TOOLS\repos\kicad-mcp-pro\README.md:30:pip install kicad-mcp-pro
03_TOOLS\repos\kicad-mcp-pro\README.md:32:kicad-mcp-pro health --json
03_TOOLS\repos\kicad-mcp-pro\README.md:36:The default no-subcommand invocation still starts the stdio MCP server for
03_TOOLS\repos\kicad-mcp-pro\README.md:37:backward compatibility. `health --json` is safe to run when KiCad is not
03_TOOLS\repos\kicad-mcp-pro\README.md:38:running; it reports KiCad IPC as deferred instead of crashing. `doctor --json`
03_TOOLS\repos\kicad-mcp-pro\README.md:47:  "servers": {
03_TOOLS\repos\kicad-mcp-pro\README.md:49:      "type": "stdio",
03_TOOLS\repos\kicad-mcp-pro\README.md:50:      "command": "uvx",
03_TOOLS\repos\kicad-mcp-pro\README.md:51:      "args": ["kicad-mcp-pro"],
03_TOOLS\repos\kicad-mcp-pro\README.md:52:      "env": {
03_TOOLS\repos\kicad-mcp-pro\README.md:53:        "KICAD_MCP_PROJECT_DIR": "/absolute/path/to/your/kicad-project",
03_TOOLS\repos\kicad-mcp-pro\README.md:54:        "KICAD_MCP_WORKSPACE_ROOT": "/absolute/path/to/your/workspace",
03_TOOLS\repos\kicad-mcp-pro\README.md:55:        "KICAD_MCP_PROFILE": "pcb_only"
03_TOOLS\repos\kicad-mcp-pro\README.md:79:- Server profiles such as `minimal`, `pcb_only`, `schematic_only`, `manufacturing`, `analysis`, and `agent_full`.
03_TOOLS\repos\kicad-mcp-pro\README.md:113:guarded behind explicit repository checks and protected environments.
EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\docs\examples\clients\codex-config.toml" -Raw
```

### Output

```text
[mcp_servers.kicad]
command = "uvx"
args = ["kicad-mcp-pro"]
startup_timeout_sec = 20
tool_timeout_sec = 120

[mcp_servers.kicad.env]
KICAD_MCP_PROJECT_DIR = "/absolute/path/to/your/kicad-project"
KICAD_MCP_PROFILE = "pcb_only"

EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\.env.example" -Raw
```

### Output

```text
# KiCad MCP Pro Server environment configuration

# Path to kicad-cli (auto-detected if omitted)
# KICAD_MCP_KICAD_CLI=/usr/bin/kicad-cli
# KICAD_CLI_PATH=/usr/bin/kicad-cli
# KICAD_MCP_FREEROUTING_JAR=/path/to/freerouting.jar
# KICAD_MCP_FREEROUTING_IMAGE=ghcr.io/freerouting/freerouting:2.1.0
# KICAD_MCP_FREEROUTING_TIMEOUT_SEC=900
# KICAD_MCP_DOCKER_EXECUTABLE=docker
# KICAD_MCP_JAVA_EXECUTABLE=java
# KICAD_MCP_NGSPICE_CLI=/usr/bin/ngspice

# Optional KiCad IPC credentials
# KICAD_MCP_KICAD_SOCKET_PATH=/tmp/kicad.sock
# KICAD_MCP_KICAD_TOKEN=replace-with-your-kicad-ipc-token
# KICAD_API_TOKEN=replace-with-your-kicad-ipc-token

# Active project
# KICAD_MCP_WORKSPACE_ROOT=/path/to/allowed/workspace
KICAD_MCP_PROJECT_DIR=/path/to/your/kicad/project
# KICAD_MCP_PROJECT_FILE=/path/to/project.kicad_pro
# KICAD_MCP_PCB_FILE=/path/to/board.kicad_pcb
# KICAD_MCP_SCH_FILE=/path/to/schematic.kicad_sch
# KICAD_MCP_OUTPUT_DIR=/path/to/output

# Library overrides
# KICAD_MCP_SYMBOL_LIBRARY_DIR=/path/to/kicad/symbols
# KICAD_MCP_FOOTPRINT_LIBRARY_DIR=/path/to/kicad/footprints

# Server
# KICAD_MCP_TRANSPORT=stdio
# KICAD_MCP_HOST=127.0.0.1
# KICAD_MCP_PORT=3334
# Use 27185 instead if you want a dedicated local KiCad Studio bridge port.
# KICAD_MCP_MOUNT_PATH=/mcp
# KICAD_MCP_CORS_ORIGINS=https://app.example.com,http://127.0.0.1:3334
# KICAD_MCP_AUTH_TOKEN=replace-with-a-local-bearer-token
# KICAD_MCP_LEGACY_SSE=false
# KICAD_MCP_STATEFUL_HTTP=false
# KICAD_MCP_ENABLE_METRICS=false
# KICAD_MCP_STUDIO_WATCH_DIR=/path/to/projects
# KICAD_MCP_PROFILE=full

# Logging
# KICAD_MCP_LOG_LEVEL=INFO
# KICAD_MCP_LOG_FORMAT=console

# Advanced
# KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false
# KICAD_MCP_IPC_CONNECTION_TIMEOUT=10.0
# KICAD_MCP_TIMEOUT_MS=10000
# KICAD_MCP_RETRIES=2
# KICAD_MCP_HEADLESS=false
# KICAD_MCP_CLI_TIMEOUT=120.0
# KICAD_MCP_MAX_ITEMS_PER_RESPONSE=200
# KICAD_MCP_MAX_TEXT_RESPONSE_CHARS=50000

EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "03_TOOLS\repos\kicad-mcp-pro\server.json" -Raw
```

### Output

```text
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.oaslananka/kicad-mcp-pro",
  "title": "KiCad MCP Pro Server",
  "description": "A professional Model Context Protocol server for KiCad EDA.",
  "version": "3.1.8",
  "repository": {
    "url": "https://github.com/oaslananka/kicad-mcp-pro",
    "source": "github"
  },
  "websiteUrl": "https://oaslananka.github.io/kicad-mcp-pro",
  "packages": [
    {
      "registryType": "pypi",
      "identifier": "kicad-mcp-pro",
      "version": "3.1.8",
      "transport": {
        "type": "stdio"
      }
    }
  ],
  "capabilities": {
    "tools": true,
    "resources": true,
    "prompts": true
  },
  "license": "MIT"
}

EXIT_CODE: 0
```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\repos\kicad-mcp-pro"
```

### Output

```text
True
EXIT_CODE: 0
```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro"
```

### Output

```text
False
EXIT_CODE: 0
```

## Command

```powershell
py -3.12 -m venv "03_TOOLS\python_envs\kicad-mcp-pro"
```

### Output

```text
(no output)
EXIT_CODE: 0
```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe"
```

### Output

```text
True
EXIT_CODE: 0
```

## Command

```powershell
Get-Process | Where-Object { $_.ProcessName -like "python*" -or $_.ProcessName -like "pip*" } | Select-Object ProcessName,Id,Path
```

### Output

```text
(no output)
EXIT_CODE: 0
```

## Command

```powershell
Get-Content -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md" -Tail 80
```

### Output

```text
```

### Output

```text
True

EXIT_CODE: 0

```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro"
```

### Output

```text
False

EXIT_CODE: 0

```

## Command

```powershell
py -3.12 -m venv "03_TOOLS\python_envs\kicad-mcp-pro"
```

### Output

```text
(no output)

EXIT_CODE: 0

```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe"
```

### Output

```text
True

EXIT_CODE: 0

```

## Command

```powershell
Get-Process | Where-Object { $_.ProcessName -like "python*" -or $_.ProcessName -like "pip*" } | Select-Object ProcessName,Id,Path
```

### Output

```text
(no output)

EXIT_CODE: 0

```

## Command

```powershell
Get-Content -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md" -Tail 80
```

### Output

```text
EXIT_CODE: 0
```


## Clean Install And Test Transcript

# kicad-mcp-pro Install Commands - Working Append

This append log records commands after the venv creation with clean UTF-8 output.


## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe" --version
```

### Output

```text
Python 3.12.10
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe" -m pip --version
```

### Output

```text
pip 25.0.1 from C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Lib\site-packages\pip (python 3.12)

EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe" -m pip install "03_TOOLS\repos\kicad-mcp-pro"
```

### Output

```text
Processing c:\users\lj\kicad_engine\03_tools\repos\kicad-mcp-pro
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting anyio>=4.4.0 (from kicad-mcp-pro==3.1.8)
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting authlib>=1.6.11 (from kicad-mcp-pro==3.1.8)
  Downloading authlib-1.7.0-py2.py3-none-any.whl.metadata (10.0 kB)
Collecting kicad-python<0.8,>=0.6 (from kicad-mcp-pro==3.1.8)
  Downloading kicad_python-0.7.1-py3-none-any.whl.metadata (8.7 kB)
Collecting kicad-sch-api<0.6,>=0.5.0 (from kicad-mcp-pro==3.1.8)
  Downloading kicad_sch_api-0.5.6-py3-none-any.whl.metadata (22 kB)
Collecting mcp>=1.23.0 (from mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading mcp-1.27.0-py3-none-any.whl.metadata (8.2 kB)
Collecting pydantic-settings>=2.3.0 (from kicad-mcp-pro==3.1.8)
  Downloading pydantic_settings-2.14.0-py3-none-any.whl.metadata (3.4 kB)
Collecting pydantic>=2.7.0 (from kicad-mcp-pro==3.1.8)
  Downloading pydantic-2.13.3-py3-none-any.whl.metadata (108 kB)
Collecting rich>=13.7.0 (from kicad-mcp-pro==3.1.8)
  Using cached rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Collecting structlog>=24.2.0 (from kicad-mcp-pro==3.1.8)
  Downloading structlog-25.5.0-py3-none-any.whl.metadata (9.5 kB)
Collecting typer>=0.12.0 (from kicad-mcp-pro==3.1.8)
  Downloading typer-0.25.1-py3-none-any.whl.metadata (15 kB)
Collecting idna>=2.8 (from anyio>=4.4.0->kicad-mcp-pro==3.1.8)
  Using cached idna-3.13-py3-none-any.whl.metadata (8.0 kB)
Collecting typing_extensions>=4.5 (from anyio>=4.4.0->kicad-mcp-pro==3.1.8)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting cryptography (from authlib>=1.6.11->kicad-mcp-pro==3.1.8)
  Downloading cryptography-47.0.0-cp311-abi3-win_amd64.whl.metadata (4.5 kB)
Collecting joserfc>=1.6.0 (from authlib>=1.6.11->kicad-mcp-pro==3.1.8)
  Downloading joserfc-1.6.4-py3-none-any.whl.metadata (3.2 kB)
Collecting jsonschema<5,>=4.23.0 (from kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting protobuf<6,>=5.29 (from kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading protobuf-5.29.6-cp310-abi3-win_amd64.whl.metadata (592 bytes)
Collecting pynng<0.10.0,>=0.9.0 (from kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading pynng-0.9.0-cp312-cp312-win_amd64.whl.metadata (7.1 kB)
Collecting sexpdata>=0.0.3 (from kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached sexpdata-1.0.2-py3-none-any.whl.metadata (3.6 kB)
Collecting fastmcp>=0.2.0 (from kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading fastmcp-3.2.4-py3-none-any.whl.metadata (8.1 kB)
Collecting jinja2>=3.0.0 (from kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting httpx-sse>=0.4 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading httpx_sse-0.4.3-py3-none-any.whl.metadata (9.7 kB)
Collecting httpx>=0.27.1 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting pyjwt>=2.10.1 (from pyjwt[crypto]>=2.10.1->mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Using cached pyjwt-2.12.1-py3-none-any.whl.metadata (4.1 kB)
Collecting python-multipart>=0.0.9 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading python_multipart-0.0.27-py3-none-any.whl.metadata (2.1 kB)
Collecting pywin32>=310 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Using cached pywin32-311-cp312-cp312-win_amd64.whl.metadata (10 kB)
Collecting sse-starlette>=1.6.1 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading sse_starlette-3.4.1-py3-none-any.whl.metadata (15 kB)
Collecting starlette>=0.27 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading starlette-1.0.0-py3-none-any.whl.metadata (6.3 kB)
Collecting typing-inspection>=0.4.1 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting uvicorn>=0.31.1 (from mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading uvicorn-0.46.0-py3-none-any.whl.metadata (6.7 kB)
Collecting python-dotenv>=1.0.0 (from mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Using cached python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->kicad-mcp-pro==3.1.8)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.46.3 (from pydantic>=2.7.0->kicad-mcp-pro==3.1.8)
  Downloading pydantic_core-2.46.3-cp312-cp312-win_amd64.whl.metadata (6.7 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=13.7.0->kicad-mcp-pro==3.1.8)
  Using cached markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich>=13.7.0->kicad-mcp-pro==3.1.8)
  Using cached pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting click>=8.2.1 (from typer>=0.12.0->kicad-mcp-pro==3.1.8)
  Downloading click-8.3.3-py3-none-any.whl.metadata (2.6 kB)
Collecting shellingham>=1.3.0 (from typer>=0.12.0->kicad-mcp-pro==3.1.8)
  Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting annotated-doc>=0.0.2 (from typer>=0.12.0->kicad-mcp-pro==3.1.8)
  Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting colorama (from click>=8.2.1->typer>=0.12.0->kicad-mcp-pro==3.1.8)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting cyclopts>=4.0.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached cyclopts-4.11.0-py3-none-any.whl.metadata (12 kB)
Collecting exceptiongroup>=1.2.2 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading exceptiongroup-1.3.1-py3-none-any.whl.metadata (6.7 kB)
Collecting griffelib>=2.0.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading griffelib-2.0.2-py3-none-any.whl.metadata (1.3 kB)
Collecting jsonref>=1.1.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading jsonref-1.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting jsonschema-path>=0.3.4 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading jsonschema_path-0.4.6-py3-none-any.whl.metadata (5.9 kB)
Collecting openapi-pydantic>=0.5.1 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading openapi_pydantic-0.5.1-py3-none-any.whl.metadata (10 kB)
Collecting opentelemetry-api>=1.20.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading opentelemetry_api-1.41.1-py3-none-any.whl.metadata (1.5 kB)
Collecting packaging>=24.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
Collecting platformdirs>=4.0.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached platformdirs-4.9.6-py3-none-any.whl.metadata (4.7 kB)
Collecting py-key-value-aio<0.5.0,>=0.4.4 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading py_key_value_aio-0.4.4-py3-none-any.whl.metadata (15 kB)
Collecting pyperclip>=1.9.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading pyperclip-1.11.0-py3-none-any.whl.metadata (2.4 kB)
Collecting pyyaml<7.0,>=6.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached pyyaml-6.0.3-cp312-cp312-win_amd64.whl.metadata (2.4 kB)
Collecting uncalled-for>=0.2.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading uncalled_for-0.3.1-py3-none-any.whl.metadata (2.9 kB)
Collecting watchfiles>=1.0.0 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading watchfiles-1.1.1-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
Collecting websockets>=15.0.1 (from fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading websockets-16.0-cp312-cp312-win_amd64.whl.metadata (7.0 kB)
Collecting certifi (from httpx>=0.27.1->mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Using cached certifi-2026.4.22-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx>=0.27.1->mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.27.1->mcp>=1.23.0->mcp[cli]>=1.23.0->kicad-mcp-pro==3.1.8)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.0.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading markupsafe-3.0.3-cp312-cp312-win_amd64.whl.metadata (2.8 kB)
Collecting cffi>=2.0.0 (from cryptography->authlib>=1.6.11->kicad-mcp-pro==3.1.8)
  Using cached cffi-2.0.0-cp312-cp312-win_amd64.whl.metadata (2.6 kB)
Collecting attrs>=22.2.0 (from jsonschema<5,>=4.23.0->kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema<5,>=4.23.0->kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema<5,>=4.23.0->kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema<5,>=4.23.0->kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading rpds_py-0.30.0-cp312-cp312-win_amd64.whl.metadata (4.2 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=13.7.0->kicad-mcp-pro==3.1.8)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting sniffio (from pynng<0.10.0,>=0.9.0->kicad-python<0.8,>=0.6->kicad-mcp-pro==3.1.8)
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting pycparser (from cffi>=2.0.0->cryptography->authlib>=1.6.11->kicad-mcp-pro==3.1.8)
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting docstring-parser<4.0,>=0.15 (from cyclopts>=4.0.0->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached docstring_parser-0.18.0-py3-none-any.whl.metadata (3.5 kB)
Collecting rich-rst<2.0.0,>=1.3.1 (from cyclopts>=4.0.0->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached rich_rst-1.3.2-py3-none-any.whl.metadata (6.1 kB)
Collecting pathable<0.6.0,>=0.5.0 (from jsonschema-path>=0.3.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading pathable-0.5.0-py3-none-any.whl.metadata (5.9 kB)
Collecting importlib-metadata<8.8.0,>=6.0 (from opentelemetry-api>=1.20.0->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading importlib_metadata-8.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting beartype>=0.20.0 (from py-key-value-aio<0.5.0,>=0.4.4->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading beartype-0.22.9-py3-none-any.whl.metadata (37 kB)
Collecting aiofile>=3.5.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading aiofile-3.9.0-py3-none-any.whl.metadata (14 kB)
Collecting keyring>=25.6.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
Collecting cachetools>=5.0.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading cachetools-7.0.6-py3-none-any.whl.metadata (5.9 kB)
Collecting email-validator>=2.0.0 (from pydantic[email]>=2.11.7->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading email_validator-2.3.0-py3-none-any.whl.metadata (26 kB)
Collecting caio<0.10.0,>=0.9.0 (from aiofile>=3.5.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading caio-0.9.25-py3-none-any.whl.metadata (3.4 kB)
Collecting dnspython>=2.0.0 (from email-validator>=2.0.0->pydantic[email]>=2.11.7->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting zipp>=3.20 (from importlib-metadata<8.8.0,>=6.0->opentelemetry-api>=1.20.0->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading zipp-3.23.1-py3-none-any.whl.metadata (3.6 kB)
Collecting pywin32-ctypes>=0.2.0 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
Collecting jaraco.classes (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting jaraco.functools (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading jaraco_functools-4.4.0-py3-none-any.whl.metadata (3.0 kB)
Collecting jaraco.context (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
Collecting docutils (from rich-rst<2.0.0,>=1.3.1->cyclopts>=4.0.0->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached docutils-0.22.4-py3-none-any.whl.metadata (15 kB)
Collecting more-itertools (from jaraco.classes->keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.2.0->kicad-sch-api<0.6,>=0.5.0->kicad-mcp-pro==3.1.8)
  Using cached more_itertools-11.0.2-py3-none-any.whl.metadata (41 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
Downloading authlib-1.7.0-py2.py3-none-any.whl (258 kB)
Downloading kicad_python-0.7.1-py3-none-any.whl (214 kB)
Downloading kicad_sch_api-0.5.6-py3-none-any.whl (329 kB)
Downloading mcp-1.27.0-py3-none-any.whl (215 kB)
Downloading pydantic-2.13.3-py3-none-any.whl (471 kB)
Downloading pydantic_core-2.46.3-cp312-cp312-win_amd64.whl (2.1 MB)
   ---------------------------------------- 2.1/2.1 MB 38.5 MB/s eta 0:00:00
Downloading pydantic_settings-2.14.0-py3-none-any.whl (60 kB)
Using cached rich-15.0.0-py3-none-any.whl (310 kB)
Downloading structlog-25.5.0-py3-none-any.whl (72 kB)
Downloading typer-0.25.1-py3-none-any.whl (58 kB)
Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading click-8.3.3-py3-none-any.whl (110 kB)
Downloading fastmcp-3.2.4-py3-none-any.whl (728 kB)
   --------------------------------------- 728.6/728.6 kB 29.2 MB/s eta 0:00:00
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading httpx_sse-0.4.3-py3-none-any.whl (9.0 kB)
Using cached idna-3.13-py3-none-any.whl (68 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading joserfc-1.6.4-py3-none-any.whl (70 kB)
Downloading cryptography-47.0.0-cp311-abi3-win_amd64.whl (3.8 MB)
   ---------------------------------------- 3.8/3.8 MB 74.7 MB/s eta 0:00:00
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Downloading protobuf-5.29.6-cp310-abi3-win_amd64.whl (435 kB)
Using cached pygments-2.20.0-py3-none-any.whl (1.2 MB)
Using cached pyjwt-2.12.1-py3-none-any.whl (29 kB)
Downloading pynng-0.9.0-cp312-cp312-win_amd64.whl (542 kB)
   ---------------------------------------- 542.6/542.6 kB ? eta 0:00:00
Using cached python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading python_multipart-0.0.27-py3-none-any.whl (29 kB)
Using cached pywin32-311-cp312-cp312-win_amd64.whl (9.5 MB)
Using cached sexpdata-1.0.2-py3-none-any.whl (10 kB)
Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Downloading sse_starlette-3.4.1-py3-none-any.whl (16 kB)
Downloading starlette-1.0.0-py3-none-any.whl (72 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading uvicorn-0.46.0-py3-none-any.whl (70 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached cffi-2.0.0-cp312-cp312-win_amd64.whl (183 kB)
Using cached cyclopts-4.11.0-py3-none-any.whl (208 kB)
Downloading exceptiongroup-1.3.1-py3-none-any.whl (16 kB)
Downloading griffelib-2.0.2-py3-none-any.whl (142 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading jsonref-1.1.0-py3-none-any.whl (9.4 kB)
Downloading jsonschema_path-0.4.6-py3-none-any.whl (19 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading markupsafe-3.0.3-cp312-cp312-win_amd64.whl (15 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading openapi_pydantic-0.5.1-py3-none-any.whl (96 kB)
Downloading opentelemetry_api-1.41.1-py3-none-any.whl (69 kB)
Using cached packaging-26.2-py3-none-any.whl (100 kB)
Using cached platformdirs-4.9.6-py3-none-any.whl (21 kB)
Downloading py_key_value_aio-0.4.4-py3-none-any.whl (152 kB)
Downloading pyperclip-1.11.0-py3-none-any.whl (11 kB)
Using cached pyyaml-6.0.3-cp312-cp312-win_amd64.whl (154 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-0.30.0-cp312-cp312-win_amd64.whl (240 kB)
Downloading uncalled_for-0.3.1-py3-none-any.whl (11 kB)
Downloading watchfiles-1.1.1-cp312-cp312-win_amd64.whl (288 kB)
Downloading websockets-16.0-cp312-cp312-win_amd64.whl (178 kB)
Using cached certifi-2026.4.22-py3-none-any.whl (135 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading aiofile-3.9.0-py3-none-any.whl (19 kB)
Downloading beartype-0.22.9-py3-none-any.whl (1.3 MB)
   ---------------------------------------- 1.3/1.3 MB 71.4 MB/s eta 0:00:00
Downloading cachetools-7.0.6-py3-none-any.whl (13 kB)
Using cached docstring_parser-0.18.0-py3-none-any.whl (22 kB)
Downloading email_validator-2.3.0-py3-none-any.whl (35 kB)
Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
Downloading pathable-0.5.0-py3-none-any.whl (16 kB)
Using cached rich_rst-1.3.2-py3-none-any.whl (12 kB)
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Downloading caio-0.9.25-py3-none-any.whl (19 kB)
Downloading dnspython-2.8.0-py3-none-any.whl (331 kB)
Using cached pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
Downloading zipp-3.23.1-py3-none-any.whl (10 kB)
Using cached docutils-0.22.4-py3-none-any.whl (633 kB)
Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
Downloading jaraco_functools-4.4.0-py3-none-any.whl (10 kB)
Using cached more_itertools-11.0.2-py3-none-any.whl (71 kB)
Building wheels for collected packages: kicad-mcp-pro
  Building wheel for kicad-mcp-pro (pyproject.toml): started
  Building wheel for kicad-mcp-pro (pyproject.toml): finished with status 'done'
  Created wheel for kicad-mcp-pro: filename=kicad_mcp_pro-3.1.8-py3-none-any.whl size=299043 sha256=f17a64f73acf0eb50264f8f4a63fdc32bb460dfc1fdf5049a972dcc091f7351d
  Stored in directory: c:\users\lj\appdata\local\pip\cache\wheels\ce\55\3d\86d001d9c49d030310eec5d49167b972f2faa72f5f69c2dc15
Successfully built kicad-mcp-pro
Installing collected packages: pywin32, pyperclip, zipp, websockets, uncalled-for, typing_extensions, structlog, sniffio, shellingham, sexpdata, rpds-py, pyyaml, pywin32-ctypes, python-multipart, python-dotenv, pyjwt, pygments, pycparser, protobuf, platformdirs, pathable, packaging, more-itertools, mdurl, MarkupSafe, jsonref, jaraco.context, idna, httpx-sse, h11, griffelib, docutils, docstring-parser, dnspython, colorama, certifi, caio, cachetools, beartype, attrs, annotated-types, annotated-doc, typing-inspection, referencing, pydantic-core, py-key-value-aio, markdown-it-py, jinja2, jaraco.functools, jaraco.classes, importlib-metadata, httpcore, exceptiongroup, email-validator, click, cffi, anyio, aiofile, watchfiles, uvicorn, starlette, rich, pynng, pydantic, opentelemetry-api, keyring, jsonschema-specifications, jsonschema-path, httpx, cryptography, typer, sse-starlette, rich-rst, pydantic-settings, openapi-pydantic, jsonschema, joserfc, mcp, kicad-python, cyclopts, authlib, fastmcp, kicad-sch-api, kicad-mcp-pro
Successfully installed MarkupSafe-3.0.3 aiofile-3.9.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.13.0 attrs-26.1.0 authlib-1.7.0 beartype-0.22.9 cachetools-7.0.6 caio-0.9.25 certifi-2026.4.22 cffi-2.0.0 click-8.3.3 colorama-0.4.6 cryptography-47.0.0 cyclopts-4.11.0 dnspython-2.8.0 docstring-parser-0.18.0 docutils-0.22.4 email-validator-2.3.0 exceptiongroup-1.3.1 fastmcp-3.2.4 griffelib-2.0.2 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 httpx-sse-0.4.3 idna-3.13 importlib-metadata-8.7.1 jaraco.classes-3.4.0 jaraco.context-6.1.2 jaraco.functools-4.4.0 jinja2-3.1.6 joserfc-1.6.4 jsonref-1.1.0 jsonschema-4.26.0 jsonschema-path-0.4.6 jsonschema-specifications-2025.9.1 keyring-25.7.0 kicad-mcp-pro-3.1.8 kicad-python-0.7.1 kicad-sch-api-0.5.6 markdown-it-py-4.0.0 mcp-1.27.0 mdurl-0.1.2 more-itertools-11.0.2 openapi-pydantic-0.5.1 opentelemetry-api-1.41.1 packaging-26.2 pathable-0.5.0 platformdirs-4.9.6 protobuf-5.29.6 py-key-value-aio-0.4.4 pycparser-3.0 pydantic-2.13.3 pydantic-core-2.46.3 pydantic-settings-2.14.0 pygments-2.20.0 pyjwt-2.12.1 pynng-0.9.0 pyperclip-1.11.0 python-dotenv-1.2.2 python-multipart-0.0.27 pywin32-311 pywin32-ctypes-0.2.3 pyyaml-6.0.3 referencing-0.37.0 rich-15.0.0 rich-rst-1.3.2 rpds-py-0.30.0 sexpdata-1.0.2 shellingham-1.5.4 sniffio-1.3.1 sse-starlette-3.4.1 starlette-1.0.0 structlog-25.5.0 typer-0.25.1 typing-inspection-0.4.2 typing_extensions-4.15.0 uncalled-for-0.3.1 uvicorn-0.46.0 watchfiles-1.1.1 websockets-16.0 zipp-3.23.1
System.Management.Automation.RemoteException
[notice] A new release of pip is available: 25.0.1 -> 26.1
[notice] To update, run: C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe -m pip install --upgrade pip
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe" -m pip show kicad-mcp-pro
```

### Output

```text
Name: kicad-mcp-pro
Version: 3.1.8
Summary: A professional Model Context Protocol server for KiCad EDA.
Home-page: https://github.com/oaslananka/kicad-mcp-pro
Author: Osman Aslan
Author-email: 
License: MIT
Location: C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Lib\site-packages
Requires: anyio, authlib, kicad-python, kicad-sch-api, mcp, pydantic, pydantic-settings, rich, structlog, typer
Required-by: 
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe" -m pip freeze
```

### Output

```text
aiofile==3.9.0
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.13.0
attrs==26.1.0
Authlib==1.7.0
beartype==0.22.9
cachetools==7.0.6
caio==0.9.25
certifi==2026.4.22
cffi==2.0.0
click==8.3.3
colorama==0.4.6
cryptography==47.0.0
cyclopts==4.11.0
dnspython==2.8.0
docstring_parser==0.18.0
docutils==0.22.4
email-validator==2.3.0
exceptiongroup==1.3.1
fastmcp==3.2.4
griffelib==2.0.2
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
httpx-sse==0.4.3
idna==3.13
importlib_metadata==8.7.1
jaraco.classes==3.4.0
jaraco.context==6.1.2
jaraco.functools==4.4.0
Jinja2==3.1.6
joserfc==1.6.4
jsonref==1.1.0
jsonschema==4.26.0
jsonschema-path==0.4.6
jsonschema-specifications==2025.9.1
keyring==25.7.0
kicad-mcp-pro @ file:///C:/Users/LJ/KICAD_ENGINE/03_TOOLS/repos/kicad-mcp-pro
kicad-python==0.7.1
kicad-sch-api==0.5.6
markdown-it-py==4.0.0
MarkupSafe==3.0.3
mcp==1.27.0
mdurl==0.1.2
more-itertools==11.0.2
openapi-pydantic==0.5.1
opentelemetry-api==1.41.1
packaging==26.2
pathable==0.5.0
platformdirs==4.9.6
protobuf==5.29.6
py-key-value-aio==0.4.4
pycparser==3.0
pydantic==2.13.3
pydantic-settings==2.14.0
pydantic_core==2.46.3
Pygments==2.20.0
PyJWT==2.12.1
pynng==0.9.0
pyperclip==1.11.0
python-dotenv==1.2.2
python-multipart==0.0.27
pywin32==311
pywin32-ctypes==0.2.3
PyYAML==6.0.3
referencing==0.37.0
rich==15.0.0
rich-rst==1.3.2
rpds-py==0.30.0
sexpdata==1.0.2
shellingham==1.5.4
sniffio==1.3.1
sse-starlette==3.4.1
starlette==1.0.0
structlog==25.5.0
typer==0.25.1
typing-inspection==0.4.2
typing_extensions==4.15.0
uncalled-for==0.3.1
uvicorn==0.46.0
watchfiles==1.1.1
websockets==16.0
zipp==3.23.1
EXIT_CODE: 0
```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe"
```

### Output

```text
True
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" --help
```

### Output

```text
                                                                               
 Usage: kicad-mcp-pro [OPTIONS] COMMAND [ARGS]...                              
                                                                               
 KiCad MCP Pro server for PCB and schematic workflows.                         
                                                                               
+- Options -------------------------------------------------------------------+
| --transport                                  TEXT     Transport: stdio,     |
|                                                       http, sse,            |
|                                                       streamable-http       |
| --host                                       TEXT     HTTP bind host        |
| --port                                       INTEGER  HTTP bind port        |
| --project-dir                                TEXT     Active KiCad project  |
|                                                       directory             |
| --log-level                                  TEXT     Log level             |
| --log-format                                 TEXT     Log format: console   |
|                                                       or json               |
| --profile                                    TEXT     Server profile: full, |
|                                                       minimal,              |
|                                                       schematic_only,       |
|                                                       pcb_only,             |
|                                                       manufacturing,        |
|                                                       builder, critic,      |
|                                                       release_manager,      |
|                                                       high_speed, power,    |
|                                                       simulation, analysis, |
|                                                       agent_full, pcb,      |
|                                                       schematic             |
| --experimental          --no-experimental             Enable experimental   |
|                                                       tools                 |
| --install-completion                                  Install completion    |
|                                                       for the current       |
|                                                       shell.                |
| --show-completion                                     Show completion for   |
|                                                       the current shell, to |
|                                                       copy it or customize  |
|                                                       the installation.     |
| --help                                                Show this message and |
|                                                       exit.                 |
+-----------------------------------------------------------------------------+
+- Commands ------------------------------------------------------------------+
| serve    Start the MCP server explicitly.                                   |
| health   Report fast package and configuration health without requiring     |
|          KiCad IPC.                                                         |
| doctor   Run deeper diagnostics without treating unavailable KiCad as       |
|          fatal.                                                             |
| version  Print package version information.                                 |
+-----------------------------------------------------------------------------+

EXIT_CODE: 0
```

## Command

```powershell
$env:KICAD_MCP_PROFILE="analysis"; $env:KICAD_MCP_WORKSPACE_ROOT="C:\Users\LJ\KICAD_ENGINE"; $env:KICAD_MCP_KICAD_CLI="C:\Program Files\KiCad\9.0\bin\kicad-cli.exe"; & "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" health --json
```

### Output

```text
{
  "ok": true,
  "status": "ok",
  "package": {
    "name": "kicad-mcp-pro",
    "version": "3.1.8"
  },
  "python": {
    "version": "3.12.10",
    "executable": "C:\\Users\\LJ\\KICAD_ENGINE\\03_TOOLS\\python_envs\\kicad-mcp-pro\\Scripts\\python.exe"
  },
  "mcp": {
    "transport_default": "stdio",
    "profile": "analysis"
  },
  "kicad": {
    "cli_path": "C:\\Program Files\\KiCad\\9.0\\bin\\kicad-cli.exe",
    "cli_found": true,
    "version": null,
    "ipc_reachable": false,
    "headless": false
  },
  "config": {
    "workspace_root": "C:\\Users\\LJ\\KICAD_ENGINE",
    "project_dir": null,
    "output_dir": null,
    "timeout_ms": 10000,
    "retries": 2,
    "headless": false,
    "log_level": "INFO",
    "log_format": "console",
    "transport": "stdio",
    "auth_token": {
      "configured": false
    },
    "kicad_token": {
      "configured": false
    }
  },
  "checks": [
    {
      "name": "kicad_cli",
      "status": "ok",
      "message": "kicad-cli found at C:\\Program Files\\KiCad\\9.0\\bin\\kicad-cli.exe",
      "hint": ""
    },
    {
      "name": "kicad_ipc",
      "status": "skipped",
      "message": "KiCad IPC probe deferred for fast health check.",
      "hint": "Run doctor --json for a deeper probe."
    }
  ]
}
EXIT_CODE: 0
```

## Command

```powershell
$env:KICAD_MCP_PROFILE="analysis"; $env:KICAD_MCP_WORKSPACE_ROOT="C:\Users\LJ\KICAD_ENGINE"; $env:KICAD_MCP_KICAD_CLI="C:\Program Files\KiCad\9.0\bin\kicad-cli.exe"; & "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" doctor --json
```

### Output

```text
{
  "ok": true,
  "status": "degraded",
  "package": {
    "name": "kicad-mcp-pro",
    "version": "3.1.8"
  },
  "python": {
    "version": "3.12.10",
    "executable": "C:\\Users\\LJ\\KICAD_ENGINE\\03_TOOLS\\python_envs\\kicad-mcp-pro\\Scripts\\python.exe"
  },
  "mcp": {
    "transport_default": "stdio",
    "profile": "analysis"
  },
  "kicad": {
    "cli_path": "C:\\Program Files\\KiCad\\9.0\\bin\\kicad-cli.exe",
    "cli_found": true,
    "version": "9.0.7",
    "ipc_reachable": false,
    "headless": false
  },
  "config": {
    "workspace_root": "C:\\Users\\LJ\\KICAD_ENGINE",
    "project_dir": null,
    "output_dir": null,
    "timeout_ms": 10000,
    "retries": 2,
    "headless": false,
    "log_level": "INFO",
    "log_format": "console",
    "transport": "stdio",
    "auth_token": {
      "configured": false
    },
    "kicad_token": {
      "configured": false
    }
  },
  "checks": [
    {
      "name": "kicad_cli",
      "status": "ok",
      "message": "kicad-cli found at C:\\Program Files\\KiCad\\9.0\\bin\\kicad-cli.exe",
      "hint": ""
    },
    {
      "name": "kicad_cli_version",
      "status": "ok",
      "message": "9.0.7",
      "hint": ""
    },
    {
      "name": "kicad_ipc",
      "status": "warn",
      "message": "KiCad IPC is reachable, but no PCB is open in the active KiCad session.",
      "hint": "Start KiCad, enable the IPC API server, and open a board."
    }
  ]
}
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" version
```

### Output

```text
3.1.8
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" serve --help
```

### Output

```text
                                                                               
 Usage: kicad-mcp-pro serve [OPTIONS]                                          
                                                                               
 Start the MCP server explicitly.                                              
                                                                               
+- Options -------------------------------------------------------------------+
| --transport                            TEXT     Transport: stdio, http,     |
|                                                 sse, streamable-http        |
| --host                                 TEXT     HTTP bind host              |
| --port                                 INTEGER  HTTP bind port              |
| --project-dir                          TEXT     Active KiCad project        |
|                                                 directory                   |
| --log-level                            TEXT     Log level                   |
| --log-format                           TEXT     Log format: console or json |
| --profile                              TEXT     Server profile: full,       |
|                                                 minimal, schematic_only,    |
|                                                 pcb_only, manufacturing,    |
|                                                 builder, critic,            |
|                                                 release_manager,            |
|                                                 high_speed, power,          |
|                                                 simulation, analysis,       |
|                                                 agent_full, pcb, schematic  |
| --experimental    --no-experimental             Enable experimental tools   |
| --help                                          Show this message and exit. |
+-----------------------------------------------------------------------------+

EXIT_CODE: 0
```

## Command

```powershell
Get-Command "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" | Select-Object Source
```

### Output

```text

EXIT_CODE: 0
```

## Command

```powershell
Resolve-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe"
```

### Output

```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe
EXIT_CODE: 0
```

## Command

```powershell
Resolve-Path -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe"
```

### Output

```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\python.exe
EXIT_CODE: 0
```

## Command

```powershell
git -C "03_TOOLS\repos\kicad-mcp-pro" status --short --branch
```

### Output

```text
## main...origin/main
EXIT_CODE: 0
```

## Command

```powershell
Get-ChildItem -LiteralPath "03_TOOLS\python_envs\kicad-mcp-pro\Scripts" -Filter "kicad-mcp-pro*" | Select-Object Name,FullName
```

### Output

```text

EXIT_CODE: 0
```


## Log Finalization

The command log was normalized to UTF-8 by removing NUL characters introduced by an early mixed-encoding append. This changed only this command log file.

## Command

```powershell
$rawMain = Get-Content -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md" -Raw; $rawAppend = Get-Content -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS_WORKING_APPEND.md" -Raw; Set-Content -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md" -Value (($rawMain -replace "`0", "") + ($rawAppend -replace "`0", "")) -Encoding UTF8; Remove-Item -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS_WORKING_APPEND.md" -Force
```

### Output

```text
Normalized command log to UTF-8 and removed temporary append log.
Final log: C:\Users\LJ\KICAD_ENGINE\02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md
EXIT_CODE: 0
```

## Command

```powershell
Test-Path -LiteralPath "03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml"; Test-Path -LiteralPath "02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md"; Test-Path -LiteralPath "02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md"
```

### Output

```text
True
True
True
EXIT_CODE: 0
```

## Command

```powershell
rg -n "INSTALLED_ISOLATED|MCP startup command|KICAD_MCP_PROFILE|KICAD_MCP_PROJECT_DIR|status: degraded|DRAFT_ONLY_NOT_APPLIED" "00_CODEX_START\TOOL_INDEX.md" "03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml" "02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md"
```

### Output

```text
03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml:3:# Status: DRAFT_ONLY_NOT_APPLIED
03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml:9:# KICAD_MCP_PROJECT_DIR is intentionally omitted while CURRENT_PROJECT is NONE.
03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml:19:KICAD_MCP_PROFILE = "analysis"
03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml:28:# KICAD_MCP_PROJECT_DIR = "C:\\Users\\LJ\\KICAD_ENGINE\\04_KICAD_PROJECTS\\active\\PROJECT_NAME"
00_CODEX_START\TOOL_INDEX.md:71:- Status: INSTALLED_ISOLATED_VENV_ANALYSIS_TESTED_NOT_CONFIGURED
00_CODEX_START\TOOL_INDEX.md:82:- Safe tests run: `--help`, `version`, `health --json`, and `doctor --json` with `KICAD_MCP_PROFILE=analysis`.
00_CODEX_START\TOOL_INDEX.md:83:- Test result: installed and healthy; `doctor --json` reported `status: degraded` only because no active KiCad board/project was open. KiCad CLI was found through explicit path `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` and reported version 9.0.7.
00_CODEX_START\TOOL_INDEX.md:84:- MCP startup command: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe serve --transport stdio --profile analysis`.
00_CODEX_START\TOOL_INDEX.md:89:- Notes: MCP config was not applied globally or project-locally. Do not add `KICAD_MCP_PROJECT_DIR` until an active project is explicitly selected and backed up.
02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md:26:- `kicad-mcp-pro doctor --json`: passed with `status: degraded` because no active KiCad board/project was open.
02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md:40:- `KICAD_MCP_PROFILE=analysis`
02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md:48:`KICAD_MCP_PROJECT_DIR` is intentionally omitted while `CURRENT_PROJECT` is `NONE`.
EXIT_CODE: 0
```

## Command

```powershell
git -C "03_TOOLS\repos\kicad-mcp-pro" status --short --branch
```

### Output

```text
## main...origin/main
EXIT_CODE: 0
```

## Command

```powershell
& "03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe" version
```

### Output

```text
3.1.8
EXIT_CODE: 0
```
