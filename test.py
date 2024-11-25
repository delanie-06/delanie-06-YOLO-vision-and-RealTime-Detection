from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("yolov8x.pt")

# Path to the input video
input_video_path = "C:/Users/Delisha Rodrigues/OneDrive/ドキュメント/ipcv\854100-hd_1920_1080_25fps.mp4"

# Set up the VideoCapture and VideoWriter: gets frames per second 
cap = cv2.VideoCapture(input_video_path)
fps = cap.get(cv2.CAP_PROP_FPS)  # Get frames per second
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object to save the output 
output_video_path = "C:/Users/Delisha Rodrigues/OneDrive/ドキュメント/ipcv/final_output.mp4" #tells where to store o/po video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec: encodes the video 
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Process each frame and save it with detections
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  

    # Run predictions on the frame
    results = model.predict(frame, stream=True)

    # Overlay results on the frame
    for result in results:
        frame_with_detections = result.plot()  

    out.write(frame_with_detections)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved as: {output_video_path}")
