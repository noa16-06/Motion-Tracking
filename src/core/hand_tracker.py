# src/core/hand_tracker.py
from cvzone.HandTrackingModule import HandDetector

class HandTracker:
    def __init__(self, max_hands=1, detectionCon=0.6):
        # Parameter müssen exakt so heißen wie hier
        self.detector = HandDetector(maxHands=max_hands, detectionCon=detectionCon)

    def find_hands(self, img):
        hands, img = self.detector.findHands(img)
        return hands, img

    def fingers_up(self, hand):
        return self.detector.fingersUp(hand)

    def finger_pos(self, hand, finger_id):
        lmList = hand["lmList"]
        return lmList[finger_id*4][0], lmList[finger_id*4][1]

    def hand_center(self, hand):
        return hand["center"]
