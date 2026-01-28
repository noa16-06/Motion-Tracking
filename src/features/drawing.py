import cv2
import numpy as np

class MotionDrawing:
    def __init__(self, width=1280, height=720):
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)
        self.prev_x = 0
        self.prev_y = 0

    def update(self, hand, detector):
        lmList = hand["lmList"]
        fingers = detector.fingers_up(hand)

        x, y = lmList[8][0], lmList[8][1]

        # ✏️ Drawing (nur Zeigefinger)
        if fingers == [0, 1, 0, 0, 0]:
            if self.prev_x == 0 and self.prev_y == 0:
                self.prev_x, self.prev_y = x, y

            cv2.line(
                self.canvas,
                (self.prev_x, self.prev_y),
                (x, y),
                (0, 0, 255),
                5
            )
            self.prev_x, self.prev_y = x, y

        # 🧼 Delete everything (alle Finger)
        elif fingers == [1, 1, 1, 1, 1]:
            self.clear()

        else:
            self.prev_x, self.prev_y = 0, 0

    def clear(self):
        self.canvas[:] = 0
        self.prev_x, self.prev_y = 0, 0
