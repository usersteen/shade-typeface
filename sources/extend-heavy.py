import json,unicodedata
from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).parent
g=json.loads((p/'menu-glyphs.json').read_text())
# Genuine lowercase: x-height 40, ascender 58, descender 15 source units.
lc={
'a':['M3 21Q11 17 21 18Q38 18 38 34L40 58H29L27 54Q23 59 15 59Q1 59 1 46Q1 32 26 33Q26 27 20 27Q12 27 5 31Z M26 41Q12 39 12 46Q12 51 18 51Q27 51 26 41Z',40],
'b':['M0 0H12L15 22Q20 17 27 18Q42 18 43 37Q45 59 27 59Q20 59 16 54L15 58H6Z M16 32L18 45Q21 50 26 49Q33 49 31 37Q30 27 24 28Q19 28 16 32Z',44],
'c':['M34 21L31 31Q24 26 19 28Q11 29 13 40Q14 50 21 49Q28 49 33 45L30 57Q26 59 19 59Q2 59 1 41Q-1 20 17 18Q28 17 34 21Z',35],
'd':['M29 0H41L37 58H26L25 54Q20 59 13 59Q0 59 0 40Q0 18 17 18Q23 18 28 22Z M27 32Q23 27 18 28Q11 29 12 40Q12 50 18 49Q23 49 26 44Z',41],
'e':['M12 41Q13 51 22 50Q29 50 35 46L32 56Q25 59 19 59Q1 59 0 40Q-1 18 20 18Q38 18 36 41Z M12 33H25Q24 26 19 26Q14 26 12 33Z',37],
'f':['M10 58L8 29H1L0 19H8V13Q8 0 22 0H31L28 10H23Q19 10 20 19H30L28 29H21L23 58Z',31],
'g':['M29 19H40L37 56Q36 74 17 74Q9 74 3 71L5 61Q12 65 18 64Q26 64 26 55Q21 59 14 58Q0 58 0 40Q0 18 16 18Q24 18 28 23Z M27 32Q23 28 19 28Q11 28 12 39Q12 49 18 49Q23 49 26 44Z',40],
'h':['M0 0H12L15 23Q20 18 27 18Q39 18 40 32L42 58H30L28 35Q28 28 23 28Q18 28 16 34L18 58H6Z',42],
'i':['M2 19H14L18 58H6Z M0 0H13L14 11H1Z',18],
'j':['M10 19H22L20 59Q20 74 7 74H0L2 63H5Q8 63 8 57Z M11 0H24L23 11H10Z',24],
'k':['M0 0H12L16 32L28 19H43L25 37L43 58H27L17 44L18 58H6Z',43],
'l':['M0 0H12L18 58H6Z',18],
'm':['M0 19H11L13 24Q18 18 25 18Q32 18 36 24Q42 18 49 18Q61 18 62 33L64 58H52L50 35Q50 28 46 28Q42 28 40 34L42 58H30L28 35Q28 28 24 28Q20 28 16 34L18 58H6Z',64],
'n':['M0 19H11L13 24Q19 18 26 18Q39 18 40 33L42 58H30L28 35Q28 28 23 28Q18 28 16 34L18 58H6Z',42],
'o':['M18 18Q36 18 38 37Q41 59 21 59Q2 59 1 40Q-1 18 18 18Z M19 28Q11 28 13 40Q14 50 21 49Q29 49 27 38Q26 28 19 28Z',39],
'p':['M0 19H11L13 23Q19 18 26 18Q42 18 43 38Q44 59 27 59Q21 59 17 55L19 74H7Z M15 32L17 45Q21 50 26 49Q33 49 31 38Q30 28 24 28Q19 28 15 32Z',44],
'q':['M28 19H40L36 74H24L25 55Q20 59 14 59Q0 59 0 40Q0 18 17 18Q24 18 28 23Z M27 32Q23 28 18 28Q11 28 12 40Q12 50 18 49Q23 49 26 44Z',40],
'r':['M0 19H11L13 25Q19 18 29 18L27 30Q19 28 16 35L18 58H6Z',29],
's':['M33 20L30 30Q24 27 17 27Q11 27 13 31L26 37Q37 41 33 51Q30 59 17 59Q8 59 2 56L0 46Q8 51 17 50Q24 50 22 46L9 40Q0 36 2 27Q4 17 19 18Q28 18 33 20Z',35],
't':['M7 8H19L20 19H30L28 29H21L23 44Q23 50 29 48L27 58Q13 62 11 47L9 29H2L0 19H8Z',30],
'u':['M0 19H12L15 43Q15 49 21 49Q27 49 28 42L30 19H42L39 58H28L27 54Q22 59 15 59Q4 59 3 45Z',42],
'v':['M0 19H13L23 46L30 19H43L29 58H17Z',43],
'w':['M0 19H12L20 46L24 19H36L43 46L49 19H61L50 58H37L31 37L27 58H14Z',61],
'x':['M0 19H14L22 31L30 19H44L29 38L45 58H31L22 45L14 58H0L15 38Z',45],
'y':['M0 19H13L23 44L30 19H43L28 61Q23 74 11 74H4L5 64H10Q16 64 17 58Z',43],
'z':['M0 19H36L34 28L16 48H35L32 58H0L1 49L20 29H3Z',36]}
(p/'heavy-lowercase-paths.json').write_text(json.dumps(lc,indent=2));g.update(lc)
punct={',':['M1 46H14L10 64H2L4 58H0Z',14],':':['M0 19H12L13 30H1Z M2 47H14L15 58H3Z',15],';':['M0 19H12L13 30H1Z M2 47H15L11 65H3L5 58H1Z',15],'-':['M0 31H28L26 40H2Z',28],'!':['M0 0H15L12 40H5Z M3 47H15L16 58H4Z',16],'?':['M0 4Q9 0 20 0Q38 0 36 17Q35 25 25 30L21 40H10L12 26Q25 21 24 14Q24 7 7 14Z M9 47H22L21 58H8Z',37],"'":['M0 0H12L8 18H1Z',12],'(' :['M19 0L15 12Q4 31 17 57L21 66H10Q-1 31 8 0Z',21],')':['M0 0H11Q22 31 13 66H2L6 54Q17 31 4 9Z',22],'—':['M0 31H54L52 40H2Z',54],'–':['M0 31H40L38 40H2Z',40]}
punct.update({
'/':['M29 0H40L11 58H0Z',40],
'[':['M0 0H24V10H12V56H24V66H0Z',24],
']':['M0 0H24V66H0V56H12V10H0Z',24],
'‘':['M4 0H13L10 7H14L15 18H2L0 10Z',15],
'’':['M0 0H13L15 9L10 18H1L5 11H1Z',15],
'“':['M4 0H13L10 7H14L15 18H2L0 10Z M23 0H32L29 7H33L34 18H21L19 10Z',34],
'”':['M0 0H13L15 9L10 18H1L5 11H1Z M19 0H32L34 9L29 18H20L24 11H20Z',34],
'&':['M38 58L32 52Q24 60 14 59Q0 58 0 44Q0 33 12 27Q4 20 6 12Q8 0 22 0Q36 0 36 13Q36 22 25 28L32 36L36 28H48L40 44L52 58Z M20 19Q27 16 25 11Q23 7 19 10Q15 13 20 19Z M18 36Q10 40 12 46Q15 52 25 44Z',52]
})
g.update(punct)
g['ß']=['M0 58V17Q0 0 18 0Q36 0 35 15Q35 24 27 29Q41 35 40 46Q39 59 23 59H17V49H22Q29 49 28 44Q27 39 17 35V26Q25 21 24 15Q24 10 18 10Q12 10 12 19V58Z',41]

# Extended-name glyphs are intentional base-plus-mark constructions, not aliases.
g['ç']=[g['c'][0]+' M16 57H23L19 63Q29 63 25 70Q21 76 10 72L12 66Q18 69 19 67L13 65Z',g['c'][1]]
g['Ç']=[g['C'][0]+' M20 57H27L23 63Q33 63 29 70Q25 76 14 72L16 66Q22 69 23 67L17 65Z',g['C'][1]]
g['ø']=[g['o'][0]+' M29 15H37L10 62H2Z',g['o'][1]]
g['Ø']=[g['O'][0]+' M33 -3H42L9 61H0Z',g['O'][1]]
g['ł']=[g['l'][0]+' M0 34L21 22L22 31L1 43Z',23]
g['Ł']=[g['L'][0]+' M0 32L29 18L31 28L1 42Z',g['L'][1]]

# Purpose-drawn matching accent outlines. Anchor height tracks cap vs x-height.
marks={'\u0301':'M-7 -7L1 -18H13L2 -7Z','\u0300':'M7 -7L-1 -18H-13L-2 -7Z','\u0302':'M-16 -7L-5 -18H5L16 -7H5L0 -12L-5 -7Z','\u0308':'M-15 -17H-5V-7H-15Z M5 -17H15V-7H5Z','\u0303':'M-17 -8Q-12 -22 0 -15Q8 -10 11 -18H18Q15 -3 2 -10Q-7 -16 -10 -8Z','\u030a':'M0 -23Q12 -23 12 -14Q12 -5 0 -5Q-12 -5 -12 -14Q-12 -23 0 -23Z M0 -18Q-5 -18 -5 -14Q-5 -10 0 -10Q5 -10 5 -14Q5 -18 0 -18Z'}
accents={}
for c in 'ÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÝŸÑàáâãäåèéêëìíîïòóôõöùúûüýÿñ':
 base,mark=unicodedata.normalize('NFD',c);accents[c]=(base,mark)
fb=FontBuilder(1000,isTTF=True);order=['.notdef','space']+list(g)+list(accents);fb.setupGlyphOrder(order);fb.setupCharacterMap({**{ord(c):c for c in g|accents},32:'space'})
out={};metrics={}
for c in order:
 pen=TTGlyphPen(None)
 if c=='.notdef':parse_path('M0 0H32V58H0Z M6 6V52H26V6Z',TransformPen(pen,(16.95,0,0,-12.07,50,700)));width=652
 elif c=='space':width=400
 else:
  base=accents[c][0] if c in accents else c;path,w=g[base]
  if c in accents and base=='i':path='M2 19H14L18 58H6Z'
  parse_path(path,TransformPen(pen,(16.95,0,0,-12.07,50,700)));width=round(w*16.95+110)
  if c in accents:
   dy=18 if base.islower() else 0
   parse_path(marks[accents[c][1]],TransformPen(pen,(11.0 if base in "iI" else 16.95,0,0,-12.07,50+w*16.95/2,700-dy*12.07)))
 out[c]=pen.glyph();metrics[c]=(width,50 if c!='space' else 0)
fb.setupGlyf(out);fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=1000,descent=-220);fb.setupNameTable({'familyName':'Shade Heavy Study','styleName':'Regular','uniqueFontIdentifier':'ShadeHeavyStudy-0.006','fullName':'Shade Heavy Study Regular','psName':'ShadeHeavyStudy-Regular','version':'Version 0.006'});fb.setupOS2(sTypoAscender=1000,sTypoDescender=-220,usWinAscent=1000,usWinDescent=220,sxHeight=483,sCapHeight=700);fb.setupPost(keepGlyphNames=False);fb.setupMaxp();addOpenTypeFeaturesFromString(fb.font,'feature kern { pos L A -100; pos A Y -85; pos A T -60; pos T U -30; pos T E -40; pos D A -30; pos P L -20; pos R E -20; pos r a -20; pos r e -20; pos r o -20; pos T a -65; pos T o -65; pos T e -65; pos V a -55; pos V o -55; pos W a -35; pos Y o -70; } kern;');fb.save(p/'ShadeHeavyStudy.ttf')
(p/'heavy-punctuation-paths.json').write_text(json.dumps(punct,indent=2));(p/'heavy-accent-paths.json').write_text(json.dumps(marks,indent=2))
im=Image.new('RGB',(1800,1500),'#f7f7f3');d=ImageDraw.Draw(im);small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',24)
d.text((55,35),'SHADE HEAVY / LOWERCASE AND NAME COVERAGE STUDY 06',font=small,fill='black')
for y,s,size in [(95,'abcdefghijklmnopqrstuvwxyz',52),(220,'Shade  Pore  Studio',80),(370,'minimum  rhythm  photograph',55),(490,'Álvaro  Élodie  Zoë  Björn',55),(610,'François  Søren  Łukasz',55),(730,'Åsa  Núria  João  Iñaki',55),(850,'Straße & ‘Shade’ / [Pore]',65),(990,'Hamburgefontsiv',65),(1120,'bdpq  ilj  rn m  ae  O0',55)]:
 d.text((55,y),s,font=ImageFont.truetype(str(p/'ShadeHeavyStudy.ttf'),size),fill='black')
d.text((55,1290),'Author-drawn lowercase, not scaled capitals. Extended names now include cedilla, slashed O and barred L.',font=small,fill='black');d.text((55,1330),'NFC accents only in this study; full combining marks, extended Latin and spacing remain unfinished.',font=small,fill='black');d.text((55,1370),'Not an accepted font or game integration. Experimental study; optical and game review remain unfinished.',font=small,fill='black');im.save(p/'lowercase-study-06.png')
