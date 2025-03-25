# 📸 OpenCV Face Detection Project 🕵️‍♀️

## 🌟 Project Overview
This is a comprehensive OpenCV-based face detection project that demonstrates various computer vision techniques using Python and OpenCV. The project includes multiple scripts showcasing image processing, video capture, edge detection, and real-time face detection.

![demo](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/demo.gif)

## 🚀 Features
- 📷 Image Loading and Display
- 🎥 Live Video Capture
- 🖌️ Drawing Shapes and Annotations
- 🌚 Grayscale and Image Blurring
- 🔍 Edge Detection
- 👤 Real-time Face Detection

## 📋 Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- NumPy

## 🛠️ Installation

### Clone the Repository
```bash
git clone https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade.git
cd Face-Detection-Using-OpenCV-Haarcascade
```

### Install Dependencies
```bash
pip install opencv-python numpy
```

## 📂 Project Structure
- `1image_basics.py`: Basic image loading and display
- `2video_basics.py`: Live video capture
- `3draw_image.py`: Drawing shapes on images
- `4gray_scale.py`: Image grayscale and blurring
- `5live_edge.py`: Real-time edge detection
- `face_detection.py`: Haar Cascade face detection
- `mirror.py`: Fun mirror effect video manipulation

## 🎯 Usage

### Image Basics
```bash
python 1image_basics.py
```
Loads and displays a sample image.

![hide the name you wan to give ](https://github.com/user-attachments/assets/7d9f8521-66f0-47b6-ab42-04ce8634e36a)


### Live Video Capture
```bash
python 2video_basics.py
```
Opens webcam and captures live video. Press 'q' to quit.

![demo](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/demo2.gif)


### Draw shapes on images
```bash
python 3draw_image.py
```
Loads and displays a sample image with shapes drawn.

![hide the name you wan to give ](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/img5.png)


### Image grayscale and blurring
```bash
python 4gray_scale.py
```
Loads and displays three images- sample image,grayscale of the sample and the blurred image of the sample.

![hide the name you wan to give ](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/img6.png)


### Real-time edge detection
```bash
python 5live_edge.py
```
Detects and highlights edges in real-time. Press 'q' to exit.

![hide the name you wan to give ](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/img7.png)

### Face Detection
```bash
python face_detection.py
```
Detects and highlights faces in real-time. Press 'q' to exit.

![demo](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/demo.gif)

### Mirror 
```bash
python mirror.py
```
Realtime Creates mirror effect of the image . Press 'q' to exit.
In the line frame = cv2.flip(frame, 1), the parameters represent:
~First parameter: The image/frame to be flipped
~Second parameter (1 or 0): The flipping code
The flipping codes in OpenCV have specific meanings:
~0: Flip vertically (around the x-axis)
~1: Flip horizontally (around the y-axis)
~-1: Flip both vertically and horizontally
In this specific mirror.py script, cv2.flip(frame, 1) is used to horizontally flip the entire frame. This creates a mirror-like effect where the image appears as if reflected in a mirror, preventing the natural "inverted" look of a webcam view.

[when both are 1 in line 10 and 14 of the mirror.py👇]

![hide the name you wan to give ](https://github.com/user-attachments/assets/6a13fd60-2466-4287-8fd0-2c248d77d95d)



[when both are 0 in line 10 and 14 of the mirror.py👇]

![hide the name you wan to give ](https://github.com/user-attachments/assets/4965c0cc-377c-4187-a760-02d74832f5dc)

[when 0 in line 10 and 1 in line 14 of the mirror.py👇]

![hide the name you wan to give ](https://github.com/user-attachments/assets/cd259424-9568-4c64-9fb7-94ac9ea8797e)

[when 1 in line 10 and 0 in line 14 of the mirror.py👇]

![hide the name you wan to give ](https://github.com/user-attachments/assets/1b197b51-4a44-4167-8fa9-350cbaa7d839)


## 🔬 Techniques Used
- Haar Cascade Classifier
- Image Transformation
- Video Capture
- Edge Detection
- Image Blurring

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See [LICENSE](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade/blob/main/LICENSE) for more information.

## 🙌 Acknowledgments
- OpenCV
- Python Community
- Haar Cascade Developers

## 📞 Contact
Ammu N Raj - [ammunraj18@gmail.com](mailto:ammunraj18@gmail.com)

Project Link: [https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade](https://github.com/AMMU-N-RAJ/Face-Detection-Using-OpenCV-Haarcascade)
