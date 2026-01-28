import cv2
from cvzone.HandTrackingModule import HandDetector
from src.features.drawing import MotionDrawing

print("")
print("Option 1: Motion Drawing")
print("Optin 2: Motion Slider")
print("")
choice = input("What do you want to do?: ")

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.6, maxHands=1)

drawing = None
if choice == "1":
    drawing = MotionDrawing()

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    if hands and drawing:
        drawing.update(hands[0], detector)

    if drawing:
        img = cv2.addWeighted(img, 1, drawing.canvas, 1, 0)

    cv2.imshow("Motion Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()