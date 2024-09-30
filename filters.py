import cv2
import numpy as np

def hsv_filter(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[..., 0] = (hsv[..., 0] + 60) % 180
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


def edge_detection_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)


def cartoon_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


def pixelation_filter(frame, pixel_size=8):
    height, width = frame.shape[:2]
    temp = cv2.resize(frame, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)