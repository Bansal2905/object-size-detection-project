import cv2
import numpy as np

class HomogeneousBgDetector():
    def __init__(self):
        pass

    def detect_objects(self, frame):
        # Converting the input frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Applying Gaussian blur to the grayscale image
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        #edges = cv2.Canny(blurred, 50, 150)
        #kernel = np.ones((5, 5), np.uint8)
        #closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # Creating a binary mask using adaptive thresholding
        mask = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

        # Finding contours in the binary mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        objects_contours = []

        # Iterating through contours and filtering based on area
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 2000:
                objects_contours.append(cnt)

        return objects_contours
