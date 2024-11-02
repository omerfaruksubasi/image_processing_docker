from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
video_path = 'people.mmp4'
cap = cv2.VideoCapture(video_path)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20.0,(frame_width,frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results[0].boxes:
        x1,y1,x2,y2 = map(int, result.xyxy[0])
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

out.write(frame)
cap.release()
out.release()
cv2.destroyAllWindows()
