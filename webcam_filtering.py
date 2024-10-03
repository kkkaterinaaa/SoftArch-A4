import cv2

import filters
import filters as filters


class Pipeline:
    def __init__(self):
        self.filters: [filters.Filter] = []

    def add(self, filter_: filters.Filter):
        self.filters.append(filter_)
        print(f"Added filter: {filter_.__class__.__name__}")

    def process(self, frame_):
        for filter in self.filters:
            frame_ = filter.process(frame_)
        return frame_

    def remove(self, filter_: filters.Filter):
        self.filters.remove(filter_)
        print(f"Removed filter: {filter_.__class__.__name__}")


class WebcamSource:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def read(self):
        return self.cap.read()[1]

    def release(self):
        self.cap.release()


if __name__ == "__main__":
    source = WebcamSource()

    pipe = Pipeline()

    hsv_filter = filters.HsvFilter()
    pixel_filter = filters.PixelationFilter(pixel_size=4)
    cartoon_filter = filters.CartoonFilter()
    edge_filter = filters.EdgeDetectionFilter()

    while True:
        frame = source.read()
        if frame is None:
            break

        processed_frame = pipe.process(frame)

        cv2.imshow("Filtering Webcam frames", processed_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('1'):
            if hsv_filter in pipe.filters:
                pipe.remove(hsv_filter)
            else:
                pipe.add(hsv_filter)
        elif key == ord('2'):
            if pixel_filter in pipe.filters:
                pipe.remove(pixel_filter)
            else:
                pipe.add(pixel_filter)
        elif key == ord('3'):
            if cartoon_filter in pipe.filters:
                pipe.remove(cartoon_filter)
            else:
                pipe.add(cartoon_filter)
        elif key == ord('4'):
            if edge_filter in pipe.filters:
                pipe.remove(edge_filter)
            else:
                pipe.add(edge_filter)

    source.release()
    cv2.destroyAllWindows()
