import cv2
from object_detector import *
import numpy as np

# Loading Aruco detector
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

# Loading Object Detector
detector = HomogeneousBgDetector()

# Loading Image
img = cv2.imread("phone.jpg")

# Getting Aruco marker corners
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict)

# Drawing polygon around the marker
int_corners = np.int0(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

# Calculating Aruco perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)

# Calculating Pixel to cm ratio
pixel_cm_ratio = aruco_perimeter / 20

# Detecting objects using the Homogeneous Background Detector
contours = detector.detect_objects(img)

# Drawing boundaries around detected objects
for cnt in contours:
    # Getting rectangle parameters
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Calculating Width and Height of the Objects using the pixel to cm ratio
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio

    # Displaying rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

# Displaying the final annotated image
cv2.imshow("Image", img)
cv2.waitKey(0)