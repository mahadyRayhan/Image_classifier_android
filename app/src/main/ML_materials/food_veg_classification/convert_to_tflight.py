import tensorflow as tf

saved_model_dir = "./output/food.model"

model = tf.keras.models.load_model(saved_model_dir)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("./output/food.tflite", "wb").write(tflite_model)