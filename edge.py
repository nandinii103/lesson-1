import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_displayed(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_displayed("Original Grayscale Image", gray_image)

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            sobel_x_coordinates = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y_coordinates = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel_coordinates = cv2.bitwise_or(sobel_x_coordinates.astype(np.uint8), sobel_y_coordinates.astype(np.uint8))
            image_displayed("Sobel Edge Detection", combined_sobel_coordinates)

        elif choice == "2":
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_threshold = int(input("Enter Lower threshold: "))
            upper_threshold = int(input("Enter Upper threshold: "))
            edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)
            image_displayed("Canny Edge Detection", edges)

        elif choice == "3":
            lap = cv2.Laplacian(gray_image, cv2.CV_64F)
            image_displayed("Laplacian Edge Detection", np.abs(lap).astype(np.uint8))

        elif choice == "4":
            print(" kernel gaussian size  (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size ( DO AN odd number): "))
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            image_displayed("Gaussian Smoothed Image", blurred)

        elif choice == "5":
            print(" kernel  median size (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))
            median_filtered = cv2.medianBlur(image, kernel_size)
            image_displayed("Median Filtered Image", median_filtered)

        elif choice == "6":
            print("Exitiing the site now")
            break

        else:
            print("wrongpick a number form 1-6")

edge_detection('image.jpg')

