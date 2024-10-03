# Video Stream Processing with Filters
## Description
This project implements the Pipes-and-Filters Pattern, applying real-time video stream processing from either a video file or a webcam. Frames are processed through four different filters, which can be enabled, disabled, and reordered dynamically via key presses.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Filter Types](#filter-types)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kkkaterinaaa/SoftArch-A4-Team12.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running with Video File
To apply filters on a video file frame by frame, use:

```bash
python video_filtering.py path/to/video/file.mp4
```

### Running with Webcam
To apply filters on real-time video from your webcam, use:

```bash
python webcam_filtering.py
```

### Controls for Filter Application
During execution, you can toggle or reorder the following filters by pressing the respective keys:

- `1` - Toggle HSV Filter
- `2` - Toggle Pixelation Filter
- `3` - Toggle Cartoon Filter
- `4` - Toggle Edge Detection Filter

You can mix and match the filters in any order, and each filter can be turned on or off as needed.

## Filter Types

1. **Color Transformation (HsvFilter)**  
   Converts the frame from BGR to HSV (Hue, Saturation, Value) color space, then shifts the hue to create a color transformation effect.

2. **Pixelation (PixelationFilter)**  
   Reduces the resolution of the frame, producing a pixelated, blocky appearance. Useful for obscuring information or creating a retro visual effect.

3. **Artistic Effect (CartoonFilter)**  
   Simplifies the image by reducing noise, detecting edges, and applying a bilateral filter to smooth colors. The result resembles a hand-drawn or cartoon-like image.

4. **Edge Detection (EdgeDetectionFilter)**  
   Highlights the edges of objects in the frame by converting it to grayscale and applying the Canny edge detection algorithm, creating a sketch-like outline.

## Features

- **Real-Time Video Processing**: Handles both webcam streams and video files, processing each frame on-the-fly.
- **Dynamic Filter Control**: Filters can be turned on/off or reordered during runtime through keyboard inputs.
- **Frame Synchronization**: For video files, the application adjusts the `wait_time` to sync with the video framerate.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch:

   ```bash
   git checkout -b feature-branch
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add new feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature-branch
   ```

5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This version is formatted with Markdown conventions used in Git repositories, including headers, code blocks, and proper markdown formatting for the README. Let me know if any further modifications are needed!
