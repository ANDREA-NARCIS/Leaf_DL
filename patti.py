"""import os
import cv2
from PIL import Image

# Define image folder
folder_path = 'C:\\Users\ANDREA NARCIS\Desktop\leaf\captured_images'

# Loop through all images in the folder
for filename in os.listdir(folder_path):
    # Check if file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load image and perform some operation
        img = Image.open(os.path.join(folder_path, filename))
        # Do some processing on the image
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


        # Save the image with a new name or in a new folder
        img.save(os.path.join('processed_images', filename))"""
import os
from PIL import Image

# Define image folder
folder_path = 'C:\\Users\ANDREA NARCIS\Desktop\leaf\captured_images'

# Loop through all images in the folder
for filename in os.listdir(folder_path):
    # Check if file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load image and convert to grayscale
        img = Image.open(os.path.join(folder_path, filename)).convert('L')
        # Save the grayscale image with a new name or in a new folder
        img.save(os.path.join('grayscale_images', filename))