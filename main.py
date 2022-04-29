from PIL import Image , ImageDraw , ImageFont
from random_word import RandomWords
import bcrypt

r = RandomWords()

new = Image.new('RGB',(200,200),color=(0,0,0))
new2 = Image.new('RGB',(200,200),color=(0,0,0))
msg1 =r.get_random_word(maxLength=5)
msg2 = r.get_random_word(maxLength=5)
d = ImageDraw.Draw(new)
fnt = ImageFont.truetype("python/F1.ttf", 140)
W,H = new.size
w,h = d.textsize(msg1,font=fnt)
d.text(((W-w)/2,(H-h)/2), msg1, font=fnt, fill=(255,255,255))
new = new.resize((200,600))
d = ImageDraw.Draw(new)
for i in range(0,int(new.size[1]/20)):
    d.line((0,new.size[1]/3+i*100)+(new.size[0],i*100-new.size[1]/3),fill=(255,255,255),width=2)
    d.line((0,i*100-new.size[1]/3)+(new.size[0],new.size[1]/3+i*100),fill=(255,255,255),width=2)

d = ImageDraw.Draw(new2)
fnt = ImageFont.truetype("python\OpenSans-VariableFont_wdth,wght.ttf", 27)
W,H = new2.size
w,h = d.textsize(msg2,font=fnt)
for i in range(0,int(new.size[1]/20)):
    d.line((0,new.size[1]/3+i*100)+(new.size[0],i*100-new.size[1]/3),fill=(255,255,255),width=2)
    d.line((0,i*100-new.size[1]/3)+(new.size[0],new.size[1]/3+i*100),fill=(255,255,255),width=2)
d.text(((W-w)/2,(H-h)/2), msg2, font=fnt, fill=(255,255,255))
# new.show()
new2 = new2.resize((50,300))
new.save('python/new1.png')
new2.save('python/new2.png')


newmsg1 = msg1.encode('utf-8')
newmsg2 = msg2.encode('utf-8')

print(msg1+","+msg2)
# print(str(bcrypt.hashpw(newmsg1,bcrypt.gensalt(10)).decode("utf-8")),",",str(bcrypt.hashpw(newmsg2,bcrypt.gensalt(10)).decode("utf-8")))
# p1 = bcrypt.hashpw(newmsg1,bcrypt.gensalt(10))
# p2 = bcrypt.hashpw(newmsg1,bcrypt.gensalt(10))
# print(p1)
# print(p2)
# print(bcrypt.checkpw(newmsg1,p1))
# print(bcrypt.checkpw(newmsg1,p2))
