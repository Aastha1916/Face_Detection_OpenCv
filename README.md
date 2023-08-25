
# Face Mask Detection Using OpenCV

Face Mask Detection is software to performs the live detection of faces and differentiate whether the person is wearing a Mask or not. This software is designed for the situations where we need to take such preventions to avoid the spread of diseases like COVID.

## Working

This code essentially captures video frames, detects faces within the frames, and then attempts to detect smiles within the detected face regions. Detected smiles are marked with blue rectangles, and a text label indicating "Mask not Detected" is added. The original and annotated frames are displayed in a window, and the loop continues until the user presses "q".
## Installation

1. Clone this repository to your local machine using:
```
git clone https://github.com/yourusername/face-mask-detection.git
```
2. Navigate to the project directory:
```
cd face-mask-detection
```
3. Make the necessary Installations :

```bash
  pip install python
```

```bash
  pip install opencv-python
```

```bash
  pip install face detection
```
4. Make sure to download the following Haarcascade XML files and place them in the project directory :

- frontal face detection harcasscade xml file
- smile detection harcasscade xml file


    