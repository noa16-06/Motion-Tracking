import math
import pyautogui
import numpy as np

class VirtualMouse:
    def __init__(self, screen_width, screen_height, max_distance=40):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.max_distance = max_distance
        self.prev_click = False

    def update(self, hand, tracker):
        fingers = tracker.fingers_up(hand)

        # Mausbewegung: nur Zeigefinger oben
        if fingers[1] == 1 and fingers[0] == 0:
            x, y = tracker.finger_pos(hand, 1)  # Zeigefinger
            screen_x = np.interp(x, [0, 1280], [0, self.screen_width])
            screen_y = np.interp(y, [0, 720], [0, self.screen_height])
            pyautogui.moveTo(screen_x, screen_y)

        # Klick: Daumen + Zeigefinger berühren
        if fingers[0] == 1 and fingers[1] == 1:
            x1, y1 = tracker.finger_pos(hand, 0)
            x2, y2 = tracker.finger_pos(hand, 1)
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist < self.max_distance and not self.prev_click:
                pyautogui.click()
                self.prev_click = True
        else:
            self.prev_click = False
