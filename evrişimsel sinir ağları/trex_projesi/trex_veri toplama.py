import keyboard
import uuid
import time
from PIL import Image
from mss import mss
"""
https://www.trex-game.skipser.com/
"""
import os

# img klasörü yoksa oluştur
if not os.path.exists("img"):  #dosya var mı kontrol oluşturur
    os.makedirs("img")  #dosyayı oluşturur
mon={"top":368,"left":735,"width":250,"height":100}
sct=mss() #mss kütüphanesindeki mss fonksiyonu ile nesne oluşturduk
i=0
def record_screen(record_id,key):
    global i
    i=i+1
    print("{}: {}".format(key,i)) #key klavyede bastığımız tuş i kaç kere bastığımız
    img=sct.grab(mon) #sct.grab belirlediğimiz piksellleri matrisler aracılığıyla tut her pikselin ayrı değeri var
    im=Image.frombytes("RGB",img.size,img.rgb)   #tutulan matrisleri amaç direk bir fotoğrafa dönüştürüp imin içine atmak
    im.save("./img/{}_{}_{}.png".format(key,record_id,i)) #fotoğrafı kaydetmek
is_exit=False
def exit ():
    global is_exit
    is_exit=True
keyboard.add_hotkey("esc",exit) #hotkey fonksiyonu parametre olarak girilen fonksiyona basıldığında exit() fonksiyonunu çağırır
record_id=uuid.uuid4()  #her seferinde farklı bir record_id üretir
while True:
    if is_exit:
        break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id,"up")
            time.sleep(0.1)
        elif  keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.1)
    except RuntimeError:continue






