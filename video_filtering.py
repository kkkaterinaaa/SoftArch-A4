import cv2

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


class VideoSource:
    def __init__(self, video_path_):
        self.cap = cv2.VideoCapture(video_path_)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def read(self):
        ret, frame_ = self.cap.read()
        if not ret:
            return None
        return frame_

    def release(self):
        self.cap.release()


if __name__ == "__main__":
    video_path = 'input.mp4'
    source = VideoSource(video_path)

    pipe = Pipeline()

    hsv_filter = filters.HsvFilter()
    pixel_filter = filters.PixelationFilter(pixel_size=8)
    cartoon_filter = filters.CartoonFilter()
    edge_filter = filters.EdgeDetectionFilter()

    while True:
        frame = source.read()
        if frame is None:
            print("End of the video.")
            break

        processed_frame = pipe.process(frame)

        cv2.imshow("Filtering Video frames", processed_frame)

        wait_time = int(1000 / source.fps)

        key = cv2.waitKey(wait_time) & 0xFF

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
