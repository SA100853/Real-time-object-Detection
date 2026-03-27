# Real-time-object-Detection
This project performs real-time face recognition using a trained model from Google Teachable Machine and controls an Arduino device (like LED) based on detection.
# 🎯 Real-Time Face Recognition with Arduino Control

This project performs **real-time face recognition** using a trained model from Google Teachable Machine and controls an Arduino device (like LED) based on detection.

---

## 🚀 Features

* Real-time webcam face detection
* Custom trained model (`keras_model.h5`)
* Arduino integration via serial communication
* Automatic action (LED ON/OFF) based on recognized person

---

## 🧠 Tech Stack

* Python
* OpenCV
* TensorFlow / Keras
* NumPy
* PySerial
* Arduino

---

## 📂 Project Structure

```
├── main.py
├── keras_model.h5
├── labels.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/face-recognition-arduino.git
cd face-recognition-arduino
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Connect Arduino

* Connect Arduino via USB
* Update COM port in `main.py`:

```python
arduino = serial.Serial('COM4', 9600)
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 🔌 Arduino Logic

* Sends `'1'` → LED ON (if Sarfaraj detected)
* Sends `'0'` → LED OFF (otherwise)

---

## 📸 How It Works

1. Webcam captures live video
2. Image is resized to 224x224
3. Model predicts class
4. If target person detected → Arduino triggered

---

## 🏆 Use Case

* Smart security system
* Attendance system
* Personalized automation

---

## 👨‍💻 Author

**Sarfaraj Alam**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
