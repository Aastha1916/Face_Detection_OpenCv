#This line imports the OpenCV library, which is used for computer vision tasks such as image and video processing.
import cv2

# Here, a cascade classifier is loaded with the Haar cascade XML file specifically designed for frontal face
# detection. This classifier will be used to detect faces in the video frames.
face_classifier = cv2.CascadeClassifier("D:\\face_mask_detection\\haarcascade_frontalface_default.xml")

# A second cascade classifier is loaded, this time with a Haar cascade XML file for smile detection. This 
# classifier will be used to detect smiles within the detected face regions.
smile_classifier = cv2.CascadeClassifier("D:\\face_mask_detection\\haarcascade_smile.xml")

# This line initializes a video capture object (cap) to capture video from the default camera (camera index 0).
# This object will be used to read frames from the video stream.
cap = cv2.VideoCapture(0)

# A while loop is used to continuously process frames from the video capture.
while True:

    # This line reads a frame from the video capture and stores it in the frame variable. 
    # The ret variable indicates whether the frame was read successfully.
    ret, frame = cap.read()

    # The captured frame (frame) is converted to grayscale using the cv2.cvtColor function. Grayscale is often
    # used for face detection as it simplifies processing and reduces computational load.
    convert_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # The detectMultiScale function of the face_classifier cascade classifier is used to detect faces in the 
    # grayscale frame. It returns a list of rectangles representing the detected face regions.
    faces = face_classifier.detectMultiScale(convert_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # This initiates a loop to iterate through each detected face region.
    for (x, y, w, h) in faces:

        # Two regions of interest (ROIs) are defined: roi_gray is a region of the grayscale frame corresponding 
        # to the detected face, and roi_color is the corresponding region in the original (color) frame.
        roi_gray = convert_gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # The detectMultiScale function of the smile_classifier cascade classifier is used to detect smiles 
        # within the roi_gray region. It returns a list of rectangles representing the detected smile regions.
        smiles = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=30, minSize=(15, 15))

        # This loop iterates through each detected smile region within the face region. It draws a blue
        # rectangle around the detected smile (cv2.rectangle) and adds a text label "Mask not Detected"
        # at specific coordinates (cv2.putText) on the color frame.
        for (sx, sy, sw, sh) in smiles:
            if (sx, sy, sw, sh):
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
                cv2.putText(frame, "Mask not Detected", (200, 450),cv2.FONT_HERSHEY_PLAIN, 2.3, (255, 255, 0), 2)
        
        # Outside the smile detection loop, a text label "Mask Detection" is added at the top-left corner of 
        # the frame to indicate the general process of mask detection.
        cv2.putText(frame, "Mask Detection", (10, 25),cv2.FONT_HERSHEY_PLAIN, 1.0, (150, 150, 0), 2)

    # The current frame with annotations is displayed in a window titled "My video" using cv2.imshow.  
    cv2.imshow("My video", frame)

    # This waits for a key press for 1 millisecond (cv2.waitKey(1)) and checks if the pressed key is "q" 
    # (ASCII value). If "q" is pressed, the loop is exited using break.
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# After the loop ends, the video capture object is released to free up system resources.
cap.release()
cap.deleteAllWindows()

# Finally, all OpenCV windows are closed.