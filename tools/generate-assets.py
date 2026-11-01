#!/usr/bin/env python3
"""Vẽ lại asset placeholder cho Diêm La Điện bằng PIL, không dùng ảnh gốc.
Chạy: python3 tools/generate-assets.py
"""
from PIL import Image, ImageDraw
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

def hall():
    W,H=1080,1920
    img=Image.new("RGB",(W,H),(10,5,5)); d=ImageDraw.Draw(img,"RGBA")
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)], fill=(int(10+30*t),int(5+10*t),int(5+8*t)))
    for x in (90, 940):
        d.rectangle([x,300,x+50,1500], fill=(40,15,10,255))
    d.polygon([(300,1150),(780,1150),(860,1250),(220,1250)], fill=(60,20,12,255))
    d.polygon([(450,1150),(630,1150),(600,950),(480,950)], fill=(30,30,35,255))
    d.ellipse([505,880,575,960], fill=(255,210,170,255))
    d.polygon([(505,900),(575,900),(560,860),(520,860)], fill=(20,20,25,255))
    d.polygon([(500,890),(470,850),(505,875)], fill=(220,200,160,255))
    d.polygon([(580,890),(610,850),(575,875)], fill=(220,200,160,255))
    for x in range(0,1080,90):
        d.polygon([(x,1920),(x+45,1750),(x+90,1920)], fill=(200,60,10,255))
        d.polygon([(x+20,1920),(x+45,1820),(x+70,1920)], fill=(255,150,20,255))
    img.save(OUT/"hall.jpg", quality=85); print("hall.jpg")

def soul(name, robe, horns=False, hat=False):
    im=Image.new("RGBA",(195,260),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.polygon([(55,260),(140,260),(120,110),(75,110)], fill=robe+(255,))
    d.ellipse([78,55,117,110], fill=(255,210,170,255))
    if horns:
        d.polygon([(78,70),(60,40),(82,60)], fill=(220,200,160,255))
        d.polygon([(117,70),(135,40),(113,60)], fill=(220,200,160,255))
    if hat:
        d.polygon([(70,60),(125,60),(115,30),(80,30)], fill=(20,20,25,255))
    im.save(OUT/name); print(name)

def anim(name, fw, robe):
    strip=Image.new("RGBA",(fw*8,300),(0,0,0,0)); d=ImageDraw.Draw(strip)
    for f in range(8):
        x0=f*fw
        if f<4: top=40+f*10; h=230
        else: top=70+(f-4)*8; h=200-(f-4)*5
        d.polygon([(x0+55,top+h),(x0+fw-55,top+h),(x0+fw-65,top),(x0+65,top)], fill=robe+(255,))
        d.ellipse([x0+fw//2-20,top-45,x0+fw//2+20,top-5], fill=(255,210,170,255))
    strip.save(OUT/name); print(name)

def fx(name, draw):
    im=Image.new("RGBA",(240,220),(0,0,0,0)); d=ImageDraw.Draw(im); draw(d); im.save(OUT/name); print(name)

if __name__=="__main__":
    hall()
    soul("c_man.png",(90,20,20),horns=True); soul("c_woman.png",(60,20,60))
    soul("c_granny.png",(40,40,40),horns=True); soul("c_monk.png",(20,20,25),hat=True)
    soul("c_nun.png",(70,20,70)); soul("c_child.png",(100,60,20),horns=True)
    anim("anim_man.png",212,(90,20,20)); anim("anim_woman.png",212,(60,20,60)); anim("anim_granny.png",195,(40,40,40))
    fx("fx_lotus.png", lambda d: d.ellipse([60,40,180,180], fill=(255,80,10,255)))
    fx("fx_halo.png", lambda d: d.ellipse([30,10,210,210], outline=(255,120,20,255), width=12))
    fx("fx_bell.png", lambda d: d.ellipse([70,60,170,160], fill=(120,60,20,255)))
    fx("fx_incense.png", lambda d: d.rectangle([110,20,130,200], fill=(150,150,150,180)))
    fx("fx_petal.png", lambda d: d.ellipse([80,80,160,140], fill=(255,120,20,255)))
    fx("fx_mo.png", lambda d: d.ellipse([50,70,190,150], fill=(140,40,20,255)))
    fx("fx_banner.png", lambda d: d.rectangle([20,60,220,160], fill=(120,20,10,255)))
    fx("fx_scroll.png", lambda d: d.rectangle([30,40,210,180], fill=(220,200,150,255)))
