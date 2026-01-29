# Motion Tracking

A simple Python project for **real-time hand motion tracking** using your webcam.  
You can **draw in the air with your index finger** by tracking hand gestures through computer vision. ✋✍️

---

## 🧠 Features

- 🎨 Draw on the screen using hand gestures
- ☝️ Index finger tracking for drawing
- 🖐️ Open hand gesture to clear the canvas
- 📹 Real-time webcam tracking
- ⚡ Easy setup and quick start

---

## ⚙️ Requirements

Make sure you have the following installed:

- Python **3.8+**
- A working webcam
- Required Python packages:

```bash
pip install -r requirements.txt
````

1. **Clone the repository**

```bash
git clone https://github.com/Milchjunge16/Motion-Tracking.git
cd Motion-Tracking
```

2. **Install dependencis**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python main.py
```

## 🎯 How It Works

This project uses MediaPipe and OpenCV to detect hand landmarks and track finger movement.

The index finger tip position is tracked to draw on a virtual canvas.

A full open hand gesture clears the canvas.

Real-time video processing ensures smooth drawing experience.
