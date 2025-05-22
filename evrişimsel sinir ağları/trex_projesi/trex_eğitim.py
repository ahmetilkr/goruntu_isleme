import glob  #klasörlere erişim sağlar
import os    #klasörlere erişim sağlar
import numpy as np   #matematiksel işlemler
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D  #derin öğrenme ile ilgili kavramlar
from PIL import Image
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns  #basit görselleştirme işlemi
from tensorflow.python.layers.pooling import max_pooling2d
from tensorflow.python.ops.gen_special_math_ops import Dawsn

imgs=glob.glob("./img/*.png")
width=125
height=50
X=[]
Y=[]
for img in imgs:
    filename=os.path.basename(img) #down_04165f39-e48c-4b80-aa30-d58689f7f68e_113.png mesela bunu gidip filename değişkenine atıyor
    label=filename.split("_")[0] #down_04165f39-e48c-4b80-aa30-d58689f7f68e_113.png mesela bu _ kısımlarından ayırıyor
                                 #['down','04165f39-e48c-4b80-aa30-d58689f7f68e','113.png'] bu şekilde yapar [0} ile downu alır labela atarız
    im=np.array(Image.open(img).convert("L").resize((width,height)))
    im=im/255  #resimler 0 ile 255 arasında pikseller  alır normalize etmek için 255 e bölünür 0 ile 1 arasında değerler alır
    X.append(im)
    Y.append(label)

X=np.array(X) #array yaptık çünkü train_test_split ile split yapıcaz ve train_test_split içine array kabul eden bir method
X=X.reshape(X.shape[0],width,height,1) #X.shape[0] kaç tane resim olduğunu verir width her resme ait genişlik height yükseklik
t=sns.countplot(Y)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np


def one_hotlabels(values):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoder = OneHotEncoder(sparse_output=False)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

    return onehot_encoded


Y=one_hotlabels(Y)
train_X,test_X,train_y,test_y=train_test_split(X,Y,test_size=0.25,random_state=2)
model=Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(width, height, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation="relu"))
model.add(Dropout(0.4))
model.add(Dense(3,activation="softmax"))
if os.path.exists("./trex_weight.h5"):
    model.load_weights("trex_weight.h5")
    print("weights yüklendi")

model.compile(loss="categorical_crossentropy",optimizer="Adam",metrics=["accuracy"])
model.fit(train_X,train_y,epochs=35,batch_size=64)
score_train=model.evaluate(train_X,train_y)
print("eğitim doğruluğu:%",score_train[1]*100)
score_test=model.evaluate(test_X,test_y)
print("test doğruluğu:%",score_test[1]*100)

open("model_new.json","w").write(model.to_json())
model.save_weights("trex_weight_new.weights.h5")















