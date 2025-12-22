# 🚗 Smart AI-Powered Car Parking System

The **Smart AI-Powered Car Parking System** is an AI-driven computer vision solution that detects, classifies, and counts parking slots in real time using video input.  
It visually highlights **occupied and free parking spaces** and displays live availability statistics.

## 🎯 Features

- 🎥 Works on **video footage** (CCTV / drone / static camera)
- 🧠 **AI & Deep Learning–based vehicle detection**
- 🟥 Occupied parking slots marked in **Red**
- 🟩 Free parking slots marked in **Green**
- 🔢 Live counter showing **FREE / TOTAL slots**
- 📸 Real-time bounding boxes and overlays
- ⚡ Fully automated & scalable solution


## 🖼️ Output Preview

The system produces results like:

- Parking slot detection using bounding boxes  
- Color-coded slot classification  
- Real-time availability display (e.g., `FREE 15 / 69`)  

> 🟩 Green → Free Slot  
> 🟥 Red → Occupied Slot  

(See images Below for sample output)

<img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/3099468c-ce77-4129-84c4-88584423f0d6" /><img width="50%" height="50%" alt="image" src="https://github.com/user-attachments/assets/209437bf-d6b5-48ba-b05e-229c9c81c139" />

## 🛠️ Tech Stack

- Python
- OpenCV
- Deep Learning (CNN-based Object Detection)
- NumPy
- Video Processing

## 🔍 How It Works

1. Load parking lot **video**
2. Process frames sequentially
3. Detect vehicles using AI model
4. Map detections to parking slots
5. Classify slots as free or occupied
6. Display results on video frames

## ⚙️ Setup & Installation
## Clone the repository
```bash
git clone https://github.com/Mkaify/Smart-CarParking-System.git
cd Smart-CarParking-System
```

## Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run App
```bash
python main.py
```

## 🚀 Applications

- Smart city parking systems
- Shopping malls & plazas
- Office buildings
- Universities & campuses
- Automated parking surveillance




## 📈 Future Improvements

- License plate recognition
- Mobile application integration
- Cloud-based dashboard
- IoT sensor fusion
- Parking reservation system

---

## 👨‍💻 Author

**Muhammad Kaif ur Rehman**  
AI & Computer Vision Enthusiast
