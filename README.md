# Real-Time Object Detection and Tracking using YOLOv8

Welcome to the **Real-Time Object Detection and Tracking** project, developed using the state-of-the-art YOLOv8 (You Only Look Once) algorithm. This project focuses on identifying and tracking multiple objects in high-definition videos with exceptional accuracy and real-time performance.

---

## 🚀 Features
- **High Accuracy:** Leveraging YOLOv8 for precise object detection.
- **Real-Time Processing:** Capable of processing frames dynamically at high speeds.
- **Multi-Object Detection:** Detects multiple objects like people, vehicles, and more with confidence scores.
- **Annotated Video Output:** Generates a video with labeled and bounded detected objects.

---

## 📋 Objectives
1. Implement real-time object detection in video streams using YOLOv8.
2. Evaluate performance via frames per second (FPS) and detection accuracy.
3. Produce annotated output videos with identified objects.

---

## 📂 Project Structure
### Code Components:
1. **Model Loading:** YOLOv8 loads to process each video frame.
2. **Video Setup:** Using OpenCV, input videos are loaded, and FPS is computed.
3. **Object Detection and Tracking:** YOLOv8 detects objects in frames, adding bounding boxes and labels.
4. **Output Generation:** Annotated frames are compiled into a new video.

---

## 💻 Technology Stack
- **Framework:** YOLOv8
- **Programming Language:** Python
- **Libraries:** OpenCV, Ultralytics

---

## 📸 Results
Below is a live detection snapshot showcasing the project's capability:
![Screenshot 2024-11-26 000201](https://github.com/user-attachments/assets/dd730bf1-b602-4878-ae9f-d82ef0ec41d8)

This image demonstrates YOLOv8 detecting objects such as a person, a phone, and a remote with associated confidence scores.
![image](https://github.com/user-attachments/assets/002e8263-94b5-4692-8a99-c1bd9e685ed6)


2. Urban Street Detection Example
Input Video (Urban Street)
This is the raw input video of an urban street scene used for testing the YOLOv8 model.



Output Video (Annotated Urban Street)
This is the output video where YOLOv8 has detected multiple objects with bounding boxes and confidence scores.
![image](https://github.com/user-attachments/assets/473ad266-43df-425d-b860-d76ac720b11e)

---
## 🎥 Workflow Overview
1. Input a high-definition video (e.g., an urban street scene).
2. YOLOv8 processes each frame for object detection.
3. The system overlays bounding boxes and labels on detected objects.
4. Outputs an annotated video for real-world use cases like surveillance or traffic monitoring.

---

## 📊 Performance Evaluation
- **Frames Per Second (FPS):** Evaluates real-time processing efficiency.
- **Strengths:**
  - High detection accuracy.
  - Real-time multi-object detection.
- **Limitations:**
  - Resource-intensive (requires a robust system).
  - Performance affected by challenging lighting and complex backgrounds.

---

## ⚡ Future Scope
1. Optimize the model for edge devices.
2. Expand object classes for improved versatility.
3. Integrate advanced tracking algorithms for maintaining object IDs across frames.

---

## 🛠️ Installation
### Prerequisites:
- Python 3.9+
- Required Python libraries: `ultralytics`, `opencv-python`

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/delanie-06/real-time-object-detection.git
   ```
2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python
   ```
3. Run the code:
   ```bash
   python your_script_name.py
   ```



