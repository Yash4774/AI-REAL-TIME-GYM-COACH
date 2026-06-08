# 🏋️ AI Real-Time Gym Assistant

<p align="center">
  <a href="https://ai-realtime-gym-assist.netlify.app/">
    <img src="https://img.shields.io/badge/🌐_Live_Documentation-Visit_Now-success?style=for-the-badge" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-00BFA5?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/WebRTC-333333?style=for-the-badge&logo=webrtc&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=groq&logoColor=white" />
</p>

<p align="center">
  <h3 align="center">🤖 AI-Powered Real-Time Fitness Assistant</h3>
  <p align="center">
    Intelligent exercise tracking, pose analysis, voice Assistanting, and workout monitoring using Computer Vision and AI.
  </p>
</p>

---

## 🌐 Documentation & Project Website

### https://ai-realtime-gym-assist.netlify.app/

Explore the complete project documentation, features, architecture, workflow, and implementation details.

---

## 🚀 Overview

AI Real-Time Gym Assistant V2 is an intelligent fitness assistant that leverages **Computer Vision**, **MediaPipe Pose Detection**, **Artificial Intelligence**, and **Voice Assistanting** to provide real-time exercise guidance.

The system analyzes body posture through a webcam, counts repetitions automatically, evaluates exercise form, tracks workout performance, and delivers live AI-generated Assistanting feedback.

---

## ✨ Key Features

### 🎯 Real-Time Pose Detection
Track body landmarks and joint movements using MediaPipe.

### 🔢 Automatic Rep Counting
Accurately count repetitions without manual input.

### 📊 Smart Workout Tracking
Monitor reps, sets, workout duration, and exercise progress.

### 🎙️ AI Voice Assistant
Receive real-time spoken feedback and exercise guidance.

### 🤖 LLM-Powered Assistanting
Generate contextual Assistanting and motivation using AI.

### ⚡ Form Correction
Detect incorrect posture and provide corrective feedback.

### 📷 Live Webcam Analysis
Analyze body movements directly from the webcam feed.

### 💾 Workout History Storage
Store workout data using SQLite.

### 🌐 Streamlit Deployment
Accessible from anywhere through a browser.

---

## 🧠 Tech Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Computer Vision | OpenCV |
| Pose Detection | MediaPipe |
| Database | SQLite |
| Real-Time Streaming | WebRTC |
| AI Assistanting | Groq LLM |
| Text-to-Speech | gTTS |
| Deployment | Streamlit Cloud |

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Webcam Stream
 │
 ▼
MediaPipe Pose Detection
 │
 ▼
Exercise Analysis Engine
 │
 ├── Rep Counting
 ├── Form Detection
 ├── Angle Calculation
 ├── Metrics Tracking
 │
 ▼
AI Assistant Engine
 │
 ├── Groq LLM
 ├── Voice Feedback
 └── Motivation System
 │
 ▼
Streamlit Dashboard
 │
 ▼
SQLite Database
```

---

## 🏋️ Supported Exercises

### Upper Body

- Shoulder Press
- Push-Ups
- Biceps Curls

### Lower Body

- Squats
- Lunges

---

## 📊 Performance Metrics

The system continuously tracks:

- Total Repetitions
- Current Set Reps
- Sets Completed
- Elbow Angles
- Knee Angles
- Hip Angles
- Back Alignment
- Exercise Form Quality
- Workout Duration
- Posture Accuracy

---

## 🎙️ AI Assistanting Capabilities

The AI Assistant can:

- Welcome users at workout start
- Correct exercise form
- Detect posture mistakes
- Motivate users during workouts
- Announce set completion
- Announce workout completion
- Detect missing body pose
- Provide contextual Assistanting feedback

---

## 💾 Database Features

SQLite is used to store:

- Workout Sessions
- Exercise Records
- Rep Counts
- Set Statistics
- User Progress Data
- Workout History

---

## 📁 Project Structure

```bash
AI-REALTIME-GYM-Assistant-V2/
│
├── services/
│   ├── Assistanting/
│   ├── tracking/
│   ├── persistence/
│   ├── auth/
│   └── config/
│
├── vision/
├── ui/
├── state/
├── static/
│
├── main.py
├── requirements.txt
├── runtime.txt
├── README.md
│
└── database/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-REALTIME-GYM-Assistant-V2.git
cd AI-REALTIME-GYM-Assistant-V2
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run main.py
```

---

## 🔥 Highlights

- Real-Time Exercise Tracking
- AI Fitness Assistant
- Live Voice Guidance
- Automatic Rep Counting
- Pose-Based Form Analysis
- MediaPipe Integration
- OpenCV Processing
- SQLite Storage
- Streamlit Interface
- Groq LLM Assistanting

---

## 👨‍💻 Developer

### Yash Kumar

**AI • Computer Vision • Fitness Technology**

Building intelligent systems that combine AI, Human Motion Analysis, and Real-Time Feedback.

---

## ⭐ Support The Project

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🚀 Share it with others

---

## 📜 License

This project is developed for educational, research, and learning purposes.
