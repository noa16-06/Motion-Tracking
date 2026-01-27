import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.6, maxHands=1)

canvas = np.zeros((720, 1280, 3), dtype=np.uint8)
prev_x, prev_y = 0, 0

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)

        x, y = lmList[8][0], lmList[8][1]  # Zeigefinger-Spitze

        # ✏️ Zeichnen (nur Zeigefinger)
        if fingers == [0, 1, 0, 0, 0]:
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 0, 255), 5)
            prev_x, prev_y = x, y

        # 🧼 Löschen (alle Finger)
        elif fingers == [1, 1, 1, 1, 1]:
            canvas = np.zeros((720, 1280, 3), dtype=np.uint8)
            prev_x, prev_y = 0, 0

        else:
            prev_x, prev_y = 0, 0

    img = cv2.addWeighted(img, 1, canvas, 1, 0)
    cv2.imshow("In-Air Drawing", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
