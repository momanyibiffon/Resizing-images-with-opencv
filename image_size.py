import cv2 as cv

# read an image
image = cv.imread("horse.png")

# display the image
cv.imshow("Unresized Image", image)

# printing original dimensions
print("Image dimensions: ", image.shape)

# percentage by which image has to be scaled
scale_percent = 20


width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

dim = (width, height)

# resizing the image
resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)

# printing new dimensions
print("Resized dimensions: ", resized.shape)

# displaying the new image with resized dimensions
cv.imshow("Resized Image", resized)

cv.waitKey(0)
cv.destroyAllWindows()

