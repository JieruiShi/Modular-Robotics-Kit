import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
builder = tfds.folder_dataset.ImageFolder('flowers-split/')
print(builder.info)

raw_train = builder.as_dataset(split='train', shuffle_files=True)
raw_test = builder.as_dataset(split='test', shuffle_files=True)
raw_valid = builder.as_dataset(split='valid', shuffle_files=True)

IMG_SIZE = 160 # All images will be resized to 160x160

def format_example(pair):
  image, index = pair['image'], pair['label']
  image = tf.cast(image, tf.float32)
  image = (image/127.5) - 1
  image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
  if index == tf.constant(0,dtype = tf.int64):
    label = tf.constant([1,0,0,0,0])
  elif index == tf.constant(1,dtype = tf.int64):
    label = tf.constant([0,1,0,0,0])
  elif index == tf.constant(2,dtype = tf.int64):
    label = tf.constant([0,0,1,0,0])
  elif index == tf.constant(3,dtype = tf.int64):
    label = tf.constant([0,0,0,1,0])
  else:
    label = tf.constant([0,0,0,0,1])    
  return image, label
  
train = raw_train.map(format_example)
validation = raw_valid.map(format_example)
test = raw_test.map(format_example)

BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000

train_batches = train.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
validation_batches = validation.batch(BATCH_SIZE)
test_batches = test.batch(BATCH_SIZE)

IMG_SHAPE = (IMG_SIZE,IMG_SIZE,3)

base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')
base_model.trainable = False                                               
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(5, activation = 'softmax')

for image_batch, label_batch in validation_batches.take(1):
   pass


model = tf.keras.Sequential([
  base_model,
  global_average_layer,
  prediction_layer
])
model.compile(optimizer = 'Adam', loss = 'categorical_crossentropy', metrics=['categorical_accuracy'])
print(model.summary())

model.fit(image_batch, label_batch, epochs = 10)
model.save('flower_classification')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open('flower_classification.tflite','wb') as f:
    f.write(tflite_model)



