import glob  #klasörlere erişim sağlar genelde belirli bir uzantıya sahip dosyaları bulmak amacıyla kullanılır
import os    #klasörlere erişim sağlar dosya oluşturma silme taşıma yapabilir
import numpy as np   #matematiksel işlemler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D  #derin öğrenme ile ilgili kavramlar
from PIL import Image
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns  #basit görselleştirme işlemi


imgs=glob.glob("./img/*.png") #glob fonksiyonu img dosyanın içindeki tüm dosya yollarını dizi içinde imgs aktarır
width=125
height=50
X=[]
Y=[]
for img in imgs:
    filename=os.path.basename(img) #img nin içinde şu an dosyanın yolu var ospathbasename() fonksiyonu dosyanın ismini filename a atar
    label=filename.split("_")[0] #down_04165f39-e48c-4b80-aa30-d58689f7f68e_113.png mesela bu _ kısımlarından ayırıyor
                             #['down','04165f39-e48c-4b80-aa30-d58689f7f68e','113.png'] bu şekilde yapar [0] ile downu alır labela atarız
    im=np.array(Image.open(img).convert("L").resize((width,height)))   #Image.open(img) imgin içinde belirtilen yola göre dosyayı açar
    #.convert içinde bulunan parametre l griye çevirir .resize belirtilen parametreye göre yeniden boyutlandırır
    #np.array işlenmiş olan görüntüyü bir numpy dizisine dönüştürür 0 ile 255 arası değerler oluşturur

    im=im/255  #görüntü verileri 0 ile 255 arası değerler alır bunu 255 e bölerek 0 ile 1 arasına çekiyoruz ?
    X.append(im)
    Y.append(label)

X=np.array(X) #x dizisi  içinde numpy kütüphanesinden arrayler tutuyor ama kendisi python dizisi
#bunu yaparak x i de bir numpy dizisine çeviriyoruz çünkü keras kütüphanesi direk numpy dizisi istiyor
#diğer amacı ise reshape gibi fonksiyonları kullanabilmek
X=X.reshape(X.shape[0],width,height,1) #X.shape[0] kaç tane resim olduğunu verir width her resme ait genişlik height yükseklik 4d diziye çeviriyoruz
#reshape yeniden boyutlandırma shape ise matrisin boyutunu verir


def one_hotlabels(values):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values) #gelen dizideki değerleri 0 1 2 gibi sayılara dönüştürür
    #mesela [cat,dog,bird,dog,cat] fit transform yapınca [0,1,2,1,0] olur
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1) #üstte örnek verdiğim diziyi 2 boyutlu yapar ve alt alta yazar
    #yani 5 sütun 1 satır şeklinde olur
    onehot_encoder = OneHotEncoder(sparse_output=False)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded) #en son yaptıüımız mesela 5 stun bir satır vardı
    #burda mesela up down right var bunu  [[1,0,0]
                                          #[0,1,0]
                                          #[0,0,1] haline dönüştürür

    return onehot_encoded

Y=one_hotlabels(Y)
train_X,test_X,train_y,test_y=train_test_split(X,Y,test_size=0.25,random_state=2)
model=Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(width, height, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2))) #piksel azaltarak hız arttırma işlemi yapıyoruz
model.add(Dropout(0.25)) #her epochda yüzde 25 lik düğümü at amaç kalan nöronların daha iyi öğrenmesini sağlamak

model.add(Flatten()) #düzleştirme yaptık matrisleri

model.add(Dense(128,activation="relu")) #dense ile araya 128lik bir düğüm koyduk
model.add(Dropout(0.4))
model.add(Dense(3,activation="softmax"))
#conv2d katmanı mesela kenarları köşeleri algılarken dense katmanı bunları birleştirir ve olasılıkları çıkarır en yüksek ihtimali çıktı verir
if os.path.exists("./trex_weight.h5"):
    model.load_weights("trex_weight.h5")
    print("weights yüklendi")

model.compile(loss="categorical_crossentropy",optimizer="Adam",metrics=["accuracy"]) #modelin özellik belirleme kısmı
model.fit(train_X,train_y,epochs=35,batch_size=64) #modelin eğitim sürecini başlatır
score_train=model.evaluate(train_X,train_y)
print("eğitim doğruluğu:%",score_train[1]*100)
score_test=model.evaluate(test_X,test_y)
print("test doğruluğu:%",score_test[1]*100)

open("model_new.json","w").write(model.to_json())
model.save_weights("trex_weight_new.weights.h5")












