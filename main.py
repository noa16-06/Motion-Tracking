import cv2
from src.core.hand_tracker import HandTracker
from src.features.drawing import MotionDrawing

print("")
print("Option 1: Motion Drawing")
print("Optin 2: Motion Slider")
print("")
choice = input("What do you want to do?: ")

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

hand_tracker = HandTracker(max_hands=1, detectionCon=0.6)

drawing = None
if choice == "1":
    drawing = MotionDrawing() 

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = hand_tracker.find_hands(img)

    if hands and drawing:
        drawing.update(hands[0], hand_tracker)

    if drawing:
        img = cv2.addWeighted(img, 1, drawing.canvas, 1, 0)

    cv2.imshow("Motion Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()