# 🤖 Hand Gesture Controlled Arduino Interface

This project uses **OpenCV**, **MediaPipe**, and **PySerial** to detect hand gestures via a webcam and send commands to an **Arduino** over serial communication.  
The Arduino can then perform actions such as displaying text on an LCD, turning on LEDs, or triggering any other connected hardware.

---

## 🚀 Features
- Real-time **hand detection** using [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)  
- Detects **left**, **right**, and **both** hands  
- Sends gesture-based messages to Arduino automatically  
- Uses **OpenCV** for live video capture and display  
- Easy to extend for hardware interaction (LEDs, Servos, LCDs, etc.)

---

## 🧠 How It Works
1. The webcam captures live video frames using **OpenCV**.  
2. **MediaPipe** detects hand landmarks and determines whether the left or right hand is visible.  
3. Depending on which hands are raised:
   - ✋ Left hand → sends `"Left Hand Raised"`  
   - 🤚 Right hand → sends `"Right Hand Raised"`  
   - 🙌 Both hands → sends `"Both Hands Raised"`  
4. The **Arduino** receives the message through serial communication and performs a predefined action.

---

## 🛠️ Requirements

### 🧩 Python Libraries
Install the necessary libraries with:

```bash
pip install opencv-python mediapipe pyserial

<p align="center">
  <img src="images/demo.jpg" alt="Hand Detection" width="500"/>
</p>

