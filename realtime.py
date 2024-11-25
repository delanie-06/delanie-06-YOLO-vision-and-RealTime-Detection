from ultralytics import YOLO
from enum import Enum
import cv2

class ModelType(Enum):
    YOLOV8n = 'yolov8n.pt'
    YOLOV8s = 'yolov8s.pt'
    YOLOV8x = 'yolov8x.pt'

class Camera(Enum):
    LAPTOP = '0'  # Using index 0, as this is the available camera

def liveObjDetection(modelType: ModelType, camera_index: str):
    model = YOLO(modelType.value)
    model.predict(source=camera_index, show=True)

if __name__ == '__main__':
    liveObjDetection(ModelType.YOLOV8x, Camera.LAPTOP.value)
