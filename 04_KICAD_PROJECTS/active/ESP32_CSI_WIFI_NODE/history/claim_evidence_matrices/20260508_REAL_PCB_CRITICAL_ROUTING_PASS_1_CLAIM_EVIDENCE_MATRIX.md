# Claim Evidence Matrix - REAL PCB Critical Routing Pass 1

| Claim | Evidence |
| --- | --- |
| The live PCB changed | hash before `1944B6DD...` vs hash after `D147FD1F...` |
| The accepted live pass holds `0` DRC violations | `reports\REAL_PCB_CRITICAL_ROUTING_PASS_1_DRC.json` |
| `+3V3` is now fully connected | live DRC unconnected summary shows `+3V3` count `0` |
| GND improved but is still incomplete | live DRC GND count `17`, prior count `26` |
| `/BOOT0` and `/ESP_EN` were deferred for real reasons | copied-board rehearsal folders and accepted report/trace audit |
