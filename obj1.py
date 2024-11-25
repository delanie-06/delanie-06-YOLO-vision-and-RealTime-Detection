from ultralytics import YOLO
from enum import Enum
import cv2

# Enum for specifying model types
class ModelType(Enum):
    YOLOV8n = 'yolov8n.pt'
    YOLOV8s = 'yolov8s.pt'
    YOLOV8x = 'yolov8x.pt'

# Enum for specifying camera sources
class Camera(Enum):
    LAPTOP = '0'       # Laptop’s internal camera
    EXTERNAL_1 = '1'   # External camera on port 1
    EXTERNAL_2 = '2'   # Another external camera, adjust if needed

def liveObjDetection(model_type: ModelType = ModelType.YOLOV8n, camera: Camera = Camera.LAPTOP):
    try:
        # Load YOLO model based on the specified type
        model = YOLO(model_type.value)
        
        # Open video capture with the specified camera
        cap = cv2.VideoCapture(int(camera.value))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform prediction
            results = model.predict(source=frame, save=False, show=False, stream=True)

            # Display detections on the frame
            for result in results:
                annotated_frame = result.plot()
                cv2.imshow("YOLOv8 Real-Time Human Detection", annotated_frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Run object detection with YOLOv8n model and laptop camera
    liveObjDetection(ModelType.YOLOV8x, Camera.LAPTOP)
