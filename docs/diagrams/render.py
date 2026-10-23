"""Render the editable diagram JSON files to standalone SVG with Python stdlib."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent
COLORS = {
    'actor': ('#eaf6f4', '#127568'),
    'system': ('#e7eefc', '#285ca1'),
    'module': ('#eff8f5', '#20806b'),
    'external': ('#fff2e4', '#b46a20'),
    'usecase': ('#f7f8fb', '#506b83'),
    'uml_actor': ('#ffffff', '#274c65'),
}
for source in sorted(ROOT.glob('*.json')):
    name = source.stem
    data = json.loads(source.read_text())
    width, height = data['width'], data['height']
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(data["title"])}">',
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#60798d"/></marker></defs>',
           f'<rect width="{width}" height="{height}" fill="#f8fafc"/>',
           f'<text x="48" y="66" font-size="32" font-weight="700" fill="#193348" font-family="Arial">{escape(data["title"])}</text>']
    if data.get('boundary'):
        b=data['boundary']
        out.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" fill="#ffffff" stroke="#8ba3b5" stroke-width="3"/>')
        out.append(f'<text x="{b["x"]+20}" y="{b["y"]+34}" font-family="Arial" font-size="20" font-weight="700" fill="#385268">{escape(b["label"])}</text>')
    for edge in data['edges']:
        x1,y1,x2,y2 = (edge[k] for k in ('x1','y1','x2','y2'))
        marker='' if edge.get('type')=='association' else ' marker-end="url(#arrow)"'
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#60798d" stroke-width="2.5"{marker}/>')
        if edge.get('label'):
            x,y=(x1+x2)/2,(y1+y2)/2-11
            out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial" font-size="17" fill="#365369" stroke="#f8fafc" stroke-width="5" paint-order="stroke">{escape(edge["label"])}</text>')
    for node in data['nodes']:
        x,y,w,h=(node[k] for k in ('x','y','w','h'))
        fill,stroke=COLORS[node['kind']]
        if node['kind']=='usecase':
            out.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
        elif node['kind']=='uml_actor':
            cx=x+w/2; top=y+5
            out.append(f'<circle cx="{cx}" cy="{top+12}" r="12" fill="none" stroke="{stroke}" stroke-width="3"/>')
            out.append(f'<path d="M {cx} {top+24} L {cx} {top+55} M {cx-23} {top+35} L {cx+23} {top+35} M {cx} {top+55} L {cx-20} {top+78} M {cx} {top+55} L {cx+20} {top+78}" fill="none" stroke="{stroke}" stroke-width="3"/>')
        else:
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(26,h//3)}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
        lines=node['text'].split('\n')
        top=(y+h+28 if node['kind']=='uml_actor' else y+h/2-(len(lines)-1)*14)
        for i,line in enumerate(lines):
            size=21 if i==0 else 17
            weight='700' if i==0 else '400'
            out.append(f'<text x="{x+w/2}" y="{top+i*28}" text-anchor="middle" font-family="Arial" font-size="{size}" font-weight="{weight}" fill="#193348">{escape(line)}</text>')
    note_y=height-145
    out.append(f'<rect x="40" y="{note_y-35}" width="{width-80}" height="135" rx="14" fill="#eef2f7"/>')
    for i,note in enumerate(data['notes']):
        out.append(f'<text x="65" y="{note_y+i*35}" font-family="Arial" font-size="17" fill="#385268">• {escape(note)}</text>')
    out.append('</svg>')
    (ROOT / f'{name}.svg').write_text('\n'.join(out)+'\n')
