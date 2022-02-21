import cv2

image_path = input("Enter the path to the image:")
image = cv2.imread(image_path)

width = int((image.shape[1])/3)
height = int((image.shape[0])/3)

resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
print(f'The original image size is: {(image.shape[0],image.shape[1])}\nThe new image size is: {resized_image.shape[0],resized_image.shape[1]}')

cv2.imshow("Original image", image)
cv2.imshow("Resized image", resized_image)

print("Do you want to save the image (y/n):")
answer = input("")

if answer == 'y':
    cv2.imwrite("resized_image.jpg", resized_image)
    print("Image saved")
elif answer == 'n':
    pass
else:
    print("Invalid answer!")

cv2.waitKey()
cv2.destroyAllWindows()