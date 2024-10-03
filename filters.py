from abc import ABC, abstractmethod
import cv2


class Filter(ABC):
    @abstractmethod
    def process(self, frame):
        raise NotImplementedError("Process must be implemented correctly for each filter!")


class HsvFilter(Filter):
    def process(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv[..., 0] = (hsv[..., 0] + 60) % 180
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


class EdgeDetectionFilter(Filter):
    def process(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return edges_colored


class CartoonFilter(Filter):
    def process(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon


class PixelationFilter(Filter):
    def __init__(self, pixel_size: int = 4):
        self.pixel_size = pixel_size

    def process(self, frame):
        height, width = frame.shape[:2]
        temp = cv2.resize(frame, (width // self.pixel_size, height // self.pixel_size), interpolation=cv2.INTER_LINEAR)
        return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
