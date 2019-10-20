import os
import pandas as pd
import numpy as np
from PIL import Image

fer_path = './fer2013.csv'
training_path = "./Training"
publicTest_path = "./PublicTest"
privateTest_path = "./PrivateTest"

paths = [training_path,publicTest_path,privateTest_path]
for path in paths:
    if not os.path.exists(path):
        for i in range (7):
            os.makedirs(os.path.join(path,str(i)))
    
#if not os.path.exists(publicTest_path):
#    for i in range (7):
#        os.makedirs(os.path.join(publicTest_path,str(i)))
#if not os.path.exists(privateTest_path):
#    for i in range (7):
#        os.makedirs(os.path.join(privateTest_path,str(i)))


width, height = 48, 48

data = pd.read_csv(fer_path)

emotion = data['emotion'].tolist()
emotion = [str(i) for i in emotion]
pixels = data['pixels'].tolist()
usage = data['Usage'].tolist()

for i in range(len(data)):    
    image_string = pixels[i].split(' ')
    image_data = np.asarray(image_string, dtype=np.uint8).reshape(48,48)
    im = Image.fromarray(image_data)
    path_to_save = os.path.join(usage[i],emotion[i],str(i).zfill(5))+".jpeg"
    im.save(path_to_save)
    print(i)
    

    