import cv2
import numpy as np
from tensorflow.keras.models import load_model
import serial
import time

model = load_model("keras_model.h5", compile=False)

class_names = []
with open("labels.txt", "r") as f:
    for line in f:
        class_names.append(line.strip().split(' ')[1])

arduino = serial.Serial('COM4', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    image = cv2.resize(frame, (224, 224))
    image = np.asarray(image, dtype=np.float32)
    image = (image / 127.5) - 1
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence = prediction[0][index]

    print(f"Detected: {class_name} ({confidence:.2f})")

    if "Sarfaraj" in class_name:
        arduino.write(b'1')
    else:
        arduino.write(b'0')

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()