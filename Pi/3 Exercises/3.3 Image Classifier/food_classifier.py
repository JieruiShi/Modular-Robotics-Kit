from tflite_runtime.interpreter import Interpreter
from PIL import Image
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--imagePath', help='Path to input image', required=True)
args = parser.parse_args()

labelmap = []
with open('labelmap.txt', 'rb') as f:
    for line in f.readlines():
        try:
            labelmap.append(line.decode('ascii'))
        except:
            labelmap.append('???')
            

img = Image.open(args.imagePath)

imgArray = np.array(img.resize((192,192)))
print(imgArray.shape)

interpreter = Interpreter(model_path = 'food_classifier.tflite')

interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.set_tensor(input_details[0]['index'], np.array([imgArray]))
interpreter.invoke()
res = np.argmax(interpreter.get_tensor(output_details[0]['index'])[0])

print('input:',input_details,'output:',output_details)
print(labelmap[res])