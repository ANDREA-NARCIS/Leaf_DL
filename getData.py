import cv2
import numpy as np
import os
img='C:\\Users\ANDREA NARCIS\Desktop\leaf\captured_images'
# Load the image
#img = cv2.imread('C:\\Users\ANDREA NARCIS\Desktop\leaf\captured_images\captured_8.png')
for filename in os.listdir(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reshape the image to a 2D array of pixels
    pixels = gray.reshape((-1, 1))

    # Convert the pixels to float32 for k-means clustering
    pixels = np.float32(pixels)

    # Define the k-means criteria and apply k-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 3  # number of clusters
    ret, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Reshape the labels and centers to match the original image shape
    labels = labels.reshape((gray.shape))
    centers = np.uint8(centers)

    # Create a segmented image by assigning each pixel to its nearest cluster center
    segmented_img = centers[labels]


# Display the original and segmented images side-by-side
cv2.imshow('Original Image', img)
cv2.imshow('Segmented Image', segmented_img)
cv2.waitKey(0)