from pathlib import Path
import html
ROOT = Path(__file__).resolve().parent
TEXT = "HI, I'M KUNAL!"
LAVENDER = "#B49AD9"
BLUE = "#A8CFF0"
GREEN = "#68AD86"
PIXEL_SIZE = 4
ICON_GAP = 18
GLYPHS = {'H': ['10001', '10001', '10001', '11111', '10001', '10001', '10001'], 'I': ['111', '010', '010', '010', '010', '010', '111'], 'M': ['10001', '11011', '10101', '10101', '10001', '10001', '10001'], 'K': ['10001', '10010', '10100', '11000', '10100', '10010', '10001'], 'U': ['10001', '10001', '10001', '10001', '10001', '10001', '01110'], 'N': ['10001', '11001', '11001', '10101', '10011', '10011', '10001'], 'A': ['01110', '10001', '10001', '11111', '10001', '10001', '10001'], 'L': ['10000', '10000', '10000', '10000', '10000', '10000', '11111'], ',': ['0', '0', '0', '0', '0', '1', '1'], "'": ['1', '1', '0', '0', '0', '0', '0'], ' ': ['000', '000', '000', '000', '000', '000', '000'], '!': ['1', '1', '1', '1', '1', '0', '1']}
ICONS = {'dna': '<path d="M5 2h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3V8H8V5H5zM17 2h3v3h-3v3h-3v3h-3v3H8v3H5v-3h3v-3h3V8h3V5h3z"/><path opacity=".5" d="M8 3h9v2H8zM8 14h9v2H8z"/>', 'sprout': '<path d="M11 11h3v11h-3zM2 5h6v3h3v6H5v-3H2zM14 5h3V2h6v6h-3v3h-6z"/>', 'terminal': '<path d="M2 3h20v18H2z" fill="none" stroke="currentColor" stroke-width="2"/><path d="m6 8 4 4-4 4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13 15h5v2h-5z"/>', 'flask': '<path d="M8 2h8v3h-2v6l7 10H3l7-10V5H8z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 15h8l3 5H5z"/>', 'yarn': '<path d="M7 3h10v3h3v12h-3v3H7v-3H4V6h3z" fill="none" stroke="currentColor" stroke-width="2"/><path d="m7 5 11 12M5 10l10 11M10 3l10 11M8 20l9-16M19 19h4v4" fill="none" stroke="currentColor" stroke-width="1.5"/>'}

scale=PIXEL_SIZE
text_width=sum((len(GLYPHS[c][0])+1)*scale for c in TEXT)-scale
cluster_width=3*28+2*10
width=text_width+ICON_GAP+cluster_width+8
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="60" viewBox="0 0 {width} 60" role="img"><title>{html.escape(TEXT)}</title>']
x=4
for c in TEXT:
 for y,row in enumerate(GLYPHS[c]):
  for col,v in enumerate(row):
   if v=='1': parts.append(f'<rect x="{x+col*scale}" y="{16+y*scale}" width="{scale}" height="{scale}" fill="{LAVENDER}"/>')
 x+=(len(GLYPHS[c][0])+1)*scale
x=4+text_width+ICON_GAP
for i,(name,color) in enumerate([('dna',BLUE),('sprout',GREEN),('terminal',LAVENDER)]):
 parts.append(f'<g transform="translate({x+i*38},17)" style="color:{color}" fill="{color}">{ICONS[name]}</g>')
parts.append('</svg>')
(ROOT/'assets/header.svg').write_text(''.join(parts))
for name,label,color in [('linkedin','LinkedIn',BLUE),('email','Email','#D2EADB')]:
 (ROOT/f'assets/{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="110" height="32" viewBox="0 0 110 32"><path fill="{color}" d="M4 0h102v4h4v24h-4v4H4v-4H0V4h4z"/><text x="55" y="21" text-anchor="middle" font-family="Verdana,Arial,sans-serif" font-size="12" font-weight="600" fill="#343744">{label}</text></svg>')
