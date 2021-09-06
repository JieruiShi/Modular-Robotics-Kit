from tflite_runtime.interpreter import Interpreter

interpreter = Interpreter(model_path='Sample_TFLite_model/detect.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print('input: ',input_details, '\noutput:',output_details)