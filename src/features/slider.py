# src/features/slider.py
import cv2
import numpy as np

class MotionSlider:
    def __init__(self, width=50, height=300, min_val=0, max_val=100, pos=(50, 200)):
        self.width = width
        self.height = height
        self.min_val = min_val
        self.max_val = max_val
        self.pos = pos
        self.value = min_val
        self.active = False
        self.canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

    def update(self, hand, tracker):
        fingers = tracker.fingers_up(hand)

        # Slider nur aktiv, wenn nur der Zeigefinger oben ist
        self.active = fingers[1] == 1 and sum(fingers) == 1

        if self.active:
            # Y-Position des Zeigefingers
            _, y = tracker.finger_pos(hand, 1)
            # Clamp auf Sliderbereich
            y = max(self.pos[1], min(self.pos[1]+self.height, y))
            # Sliderwert berechnen
            self.value = self.max_val - ((y - self.pos[1]) / self.height) * (self.max_val - self.min_val)

        # Visualisierung
        self.canvas[:] = 0
        cv2.rectangle(self.canvas, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height), (200,200,200), 2)
        fill_y = int(self.pos[1] + self.height - (self.value - self.min_val) / (self.max_val - self.min_val) * self.height)
        cv2.rectangle(self.canvas, (self.pos[0], fill_y), (self.pos[0]+self.width, self.pos[1]+self.height), (0,0,255), -1)
        cv2.putText(self.canvas, f"{int(self.value)}", (self.pos[0]+60, fill_y+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
