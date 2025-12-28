import cv2
import pickle
import cvzone
import numpy as np
import streamlit as st
import time  # <--- Added this library

# 1. Load the parking positions
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

# 2. Setup the parking space checker function
def checkParkingSpace(img, imgPro):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        # Crop logic based on your repository dimensions
        imgCrop = imgPro[y:y + 33, x:x + 79]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + 79, pos[1] + 33), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + 33 - 3), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0,200,0))
    return img

# 3. Streamlit Web Interface
st.set_page_config(page_title="Smart Parking", layout="wide")
st.title("🚗 Smart Car Parking System")

# Sidebar for controls
st.sidebar.header("Settings")
# Add a frame rate limit control to fix the error
fps_limit = st.sidebar.slider("Frame Rate Limit (FPS)", 1, 30, 10) 

video_source = st.sidebar.radio("Select Video Source", ("Default Video", "Upload Your Own"))

if video_source == "Default Video":
    cap = cv2.VideoCapture('carPark.mp4') 
else:
    uploaded_file = st.sidebar.file_uploader("Upload a video...", type=["mp4", "avi"])
    if uploaded_file is not None:
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())
        cap = cv2.VideoCapture("temp_video.mp4")
    else:
        cap = None

if cap:
    st_frame = st.empty() # Placeholder
    
    while True:
        # Calculate time delay to match target FPS
        start_time = time.time()
        
        success, img = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # Loop video
            continue

        # Image Preprocessing
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        # Process the frame
        img = checkParkingSpace(img, imgDilate)

        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Display the frame
        st_frame.image(img, channels="RGB")
        
        # --- CRITICAL FIX: Control the speed ---
        # This prevents the "Missing file" error by giving the browser time to render
        time.sleep(1 / fps_limit)