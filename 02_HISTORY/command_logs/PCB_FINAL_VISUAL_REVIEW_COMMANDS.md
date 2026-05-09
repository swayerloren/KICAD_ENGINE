# PCB Final Visual Review Commands

Date: `2026-05-09`

Commands executed or rerun for evidence capture during this review:

```powershell
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_ROUTING_COMPLETION_REPORT.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_DRC_REPORT.md
git status --short
git diff --name-only -- "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/*.kicad_sch"
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb drc --format json --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_VISUAL_REVIEW_LIVE_DRC.json' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb'
@'
import math, pathlib, re, json
pcb = pathlib.Path(r'04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb').read_text(encoding='utf-8')
segment_re = re.compile(r'\(segment\s+\(start\s+([\d\.-]+)\s+([\d\.-]+)\)\s+\(end\s+([\d\.-]+)\s+([\d\.-]+)\).*?\(layer\s+"([^"]+)"\).*?\(net\s+(\d+)\)', re.S)
net_re = {int(n): name for n, name in re.findall(r'\(net\s+(\d+)\s+"([^"]+)"\)', pcb)}
segments = []
for x1, y1, x2, y2, layer, net in segment_re.findall(pcb):
    x1=float(x1); y1=float(y1); x2=float(x2); y2=float(y2); net=int(net)
    ang = abs(math.degrees(math.atan2(y2-y1, x2-x1))) % 180
    length = math.hypot(x2-x1, y2-y1)
    segments.append({"net": net_re.get(net, str(net)), "layer": layer, "start": [x1,y1], "end": [x2,y2], "length": round(length,3), "angle": round(ang,2)})
from collections import defaultdict
pts=defaultdict(list)
for s in segments:
    if s['start']!=s['end']:
        pts[(tuple(s['start']), s['net'], s['layer'])].append(s)
        pts[(tuple(s['end']), s['net'], s['layer'])].append({**s, 'start': s['end'], 'end': s['start']})
right_angles=[]
for (pt, net, layer), segs in pts.items():
    if len(segs) < 2:
        continue
    dirs=[]
    for s in segs:
        dx=s['end'][0]-s['start'][0]; dy=s['end'][1]-s['start'][1]
        ang=abs(math.degrees(math.atan2(dy,dx)))%180
        dirs.append((ang,s))
    for i in range(len(dirs)):
        for j in range(i+1,len(dirs)):
            a=dirs[i][0]; b=dirs[j][0]
            diff=abs(a-b); diff=min(diff,180-diff)
            if abs(diff-90) < 0.1:
                right_angles.append({"net": net, "layer": layer, "point": list(pt)})
                break
        else:
            continue
        break
by_net=defaultdict(list)
for s in segments:
    by_net[(s['net'], s['layer'])].append(s)
loops=[]
for (net, layer), segs in by_net.items():
    xs=[p for s in segs for p in (s['start'][0], s['end'][0])]
    ys=[p for s in segs for p in (s['start'][1], s['end'][1])]
    orth=sum(s['length'] for s in segs if s['angle'] in (0.0,90.0))
    if len(segs) >= 4 and orth > 35 and (max(xs)-min(xs)) > 5 and (max(ys)-min(ys)) > 5:
        loops.append({"net": net, "layer": layer, "bbox": [round(min(xs),3), round(min(ys),3), round(max(xs),3), round(max(ys),3)], "orth_total": round(orth,3)})
long_diagonals=[s for s in segments if s['length'] > 5 and s['angle'] not in (0.0,45.0,90.0,135.0)]
out={"right_angle_count": len(right_angles), "right_angles": right_angles, "loop_like_nets": loops, "long_non_45_diagonals": long_diagonals}
out_path = pathlib.Path(r'04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_FINAL_VISUAL_REVIEW_GEOMETRY.json')
out_path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps({"right_angle_count": len(right_angles), "loop_like_count": len(loops), "long_non_45_diagonal_count": len(long_diagonals)}, indent=2))
'@ | python -
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_VISUAL_REVIEW_GEOMETRY.json
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_VISUAL_REVIEW_LIVE_DRC.json
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROMPT_COUNTER.md
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "pcb final visual review" --apply
git diff --name-only -- "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/*.kicad_sch"
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROMPT_COUNTER.md
```

Observed results summary:
- `git diff --name-only` for `*.kicad_sch` returned no files.
- Live DRC returned `0` violations and `13` unconnected items.
- Geometry scan found `33` right-angle junctions, `3` loop-like orthogonal route groups, and `3` long non-45 diagonal segments.
- Prompt counter was incremented from `4` to `5`; project status is now `MAINTENANCE_DUE`.
- No live PCB edit command was run in this review.
