# 🏋️ AI Real-Time Gym Coach V2

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-00BFA5?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/WebRTC-333333?style=for-the-badge&logo=webrtc&logoColor=white" />
</p>

<p align="center">
  <b>AI-Powered Real-Time Fitness Coaching using Computer Vision, Pose Detection, and Voice Feedback</b>
</p>

---

## 🚀 Overview

AI Real-Time Gym Coach V2 is a smart fitness assistant that analyzes exercises in real time using MediaPipe Pose Detection and Computer Vision.

The system tracks body movements, counts repetitions, evaluates exercise form, provides AI-generated coaching feedback, and delivers real-time voice guidance while users perform workouts.

---

## ✨ Features

- 🎯 Real-Time Pose Detection
- 🤖 AI Fitness Coach
- 🎙️ Voice Feedback System
- 🔢 Automatic Rep Counting
- 📊 Set & Workout Tracking
- 🏋️ Multiple Exercise Support
- 📈 Performance Analytics
- 💾 SQLite Database Storage
- 📷 Live Webcam Processing
- ⚡ Form Correction Feedback
- 🌐 Streamlit Cloud Deployment

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Application |
| Streamlit | Frontend & Dashboard |
| MediaPipe | Human Pose Detection |
| OpenCV | Video Processing |
| SQLite | Workout Data Storage |
| WebRTC | Real-Time Camera Streaming |
| gTTS | Text-To-Speech |
| Groq LLM | AI Coaching Feedback |

---

## 🏗️ System Architecture


---

## 🎯 Supported Exercises

### Upper Body
- Shoulder Press
- Push-Ups
- Biceps Curls

### Lower Body
- Squats
- Lunges

---

## 📊 Real-Time Metrics

The coach tracks:

- Total Repetitions
- Current Set Progress
- Sets Completed
- Elbow Angle
- Knee Angle
- Hip Angle
- Back Alignment
- Exercise Form
- Workout Duration

---

## 🎙️ AI Voice Coaching

The AI Coach can:

- Welcome Users
- Correct Form Mistakes
- Give Live Feedback
- Announce Set Completion
- Announce Workout Completion
- Detect Missing Pose
- Motivate During Training

---

## 💾 Database

SQLite stores:

- Workout Sessions
- Exercise History
- Rep Counts
- Set Statistics
- User Performance Records

---

## 📂 Project Structure

```bash
AI-REALTIME-GYM-COACH-V2/
│
├── services/
│   ├── coaching/
│   ├── tracking/
│   ├── vision/
│   ├── persistence/
│   └── auth/
│
├── state/
├── ui/
├── static/
│
├── main.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---


```

---

## 🌐 Live Demo & Documentation👇:


https://ai-realtime-gym-assist.netlify.app/


---

## 📸 Core Components

### MediaPipe Pose Detection
Tracks body landmarks in real time for exercise analysis.

### OpenCV Processing
Handles frame processing and visual overlays.

### AI Coaching Engine
Generates intelligent exercise feedback using LLMs.

### Voice Guidance System
Converts coaching feedback into speech using gTTS.

### SQLite Database
Stores workout performance and session history.

---
## 👨‍💻 Developer

**Yash Kumar**

AI • Computer Vision • Fitness Technology

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational and research purposes.
