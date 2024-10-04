# Import YOLO from ultralytics
from ultralytics import YOLO

model = YOLO('yolov8x')

result = model.track('inputs/tennis_video.mp4', save=True)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)