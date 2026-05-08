import cv2
from src.core.hand_tracker import HandTracker
from src.features.drawing import MotionDrawing
from src.features.slider import MotionSlider
from src.features.mouse import VirtualMouse
from src.features.aimbot import aimbot
import pyautogui

print("")
print("Option 1: Motion Drawing")
print("Optin 2: Motion Slider")
print("Option 3: Virtuall Mouse")
print("Option 4: Aimbot")
print("")
choice = input("What do you want to do?: ")

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

hand_tracker = HandTracker(max_hands=1, detectionCon=0.6)
screen_w, screen_h = pyautogui.size()

feature = None
if choice == "1":
    feature = MotionDrawing() 
elif choice == "2":
    feature = MotionSlider(min_val=0, max_val=100, pos=(50, 200))
elif choice == "3":
    feature = VirtualMouse(screen_w, screen_h)
elif choice == "4":
    feature = aimbot()

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = hand_tracker.find_hands(img)

    if hands and feature:
        feature.update(hands[0], hand_tracker)

    if feature and hasattr(feature, "canvas"):
        img = cv2.addWeighted(img, 1, feature.canvas, 1, 0)

    cv2.imshow("Motion Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()