import json
from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.basePen import BasePen
from fontTools.svgLib.path import parse_path
from shapely.geometry import LineString
from shapely.geometry.polygon import orient
from shapely.ops import unary_union
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).parent;g=json.loads((p/'thin-glyphs.json').read_text())
class Flatten(BasePen):
 def __init__(self):super().__init__(None);self.lines=[];self.cur=[]
 def _moveTo(self,pt):self.finish();self.cur=[pt]
 def _lineTo(self,pt):self.cur.append(pt)
 def _qCurveToOne(self,c,b):
  a=self.cur[-1]
  for i in range(1,25):
   t=i/24;self.cur.append(tuple((1-t)**2*a[k]+2*(1-t)*t*c[k]+t*t*b[k] for k in range(2)))
 def _closePath(self):self.cur.append(self.cur[0]);self.finish()
 def _endPath(self):self.finish()
 def finish(self):
  if len(self.cur)>1:self.lines.append(self.cur)
  self.cur=[]
fb=FontBuilder(1000,isTTF=True);order=['.notdef','space']+list(g);fb.setupGlyphOrder(order);fb.setupCharacterMap({32:'space',**{ord(c):c for c in g}});out={};metrics={}
for c in order:
 pen=TTGlyphPen(None)
 if c in g:
  flat=Flatten();parse_path(g[c][0],flat);flat.finish();shape=unary_union([LineString(ln).buffer(4.5,cap_style='flat',join_style='round',quad_segs=12) for ln in flat.lines])
  for poly in (list(shape.geoms) if shape.geom_type=='MultiPolygon' else [shape]):
   poly=orient(poly,sign=1)
   for ring in [poly.exterior,*poly.interiors]:
    pts=list(ring.coords)[:-1];pen.moveTo((pts[0][0]*7+40,700-pts[0][1]*7))
    for x,y in pts[1:]:pen.lineTo((x*7+40,700-y*7))
    pen.closePath()
 out[c]=pen.glyph();metrics[c]=(g[c][1]*7+80,40) if c in g else (300,0)
fb.setupGlyf(out);fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=850,descent=-150);fb.setupNameTable({'familyName':'Shade Thin Draft','styleName':'Regular','uniqueFontIdentifier':'ShadeThinDraft-0.001','fullName':'Shade Thin Draft Regular','psName':'ShadeThinDraft-Regular','version':'Version 0.001'});fb.setupOS2(sTypoAscender=850,sTypoDescender=-150,usWinAscent=900,usWinDescent=150);fb.setupPost();fb.setupMaxp();fb.save(p/'ShadeThinDraft.ttf')
im=Image.new('RGB',(1600,980),'#f7f7f3');d=ImageDraw.Draw(im);body='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';label=ImageFont.truetype(body,24)
d.text((50,30),'SHADE / TWO RELATED DISPLAY DIRECTIONS',font=label,fill='#111111')
for x,name,fn in [(50,'HEAVY / DEMO-derived','ShadeDisplayDraft.ttf'),(850,'THIN / EARLY ACCESS-derived','ShadeThinDraft.ttf')]:
 d.text((x,100),name,font=label,fill='#555555')
 for i,w in enumerate(['PLAY','STUDIO','UPDATES','CREDITS']):d.text((x,150+i*120),w,font=ImageFont.truetype(str(p/fn),85),fill='black')
 d.text((x,670),'36 px / menu-scale check',font=label,fill='#555555')
 for i,w in enumerate(['PLAY','STUDIO','UPDATES','CREDITS']):d.text((x,720+i*42),w,font=ImageFont.truetype(str(p/fn),36),fill='black')
d.text((50,935),'Both are draft fonts rendered as text. Neither is deployed or artist-approved.',font=label,fill='#555555');im.save(p/'two-faces-proof.png')
