import cv2 as cv
from tkinter import *
import tkinter.filedialog
from PIL import Image
from PIL import ImageTk
import os


def select_image():
    global panelA
    
    path = tkinter.filedialog.askopenfilename()
    if len(your_name.get()) != 0:
        # read an image
        image = cv.imread(path)

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
        # saving the resized image
        cv.imwrite("resized_image" + os.path.basename(path), resized)

        cv.waitKey(0)
        cv.destroyAllWindows()

        # displaying file name of selected image
        file_name.configure(text="Previously selected: " + os.path.basename(path))
        
    else:
        # error to display when the users name is missing
        error = "You must enter your name before selecting an image!"
        error_label.configure(text=error)


def submit_name():
    # checking to ensure name field is not empty
    if len(your_name.get()) != 0:
        # getting the name from name entry field to be displayed on the GUI
        name = "Your name is: "+ your_name.get()

        name_label.configure(text=name)
        
        lbl.configure(text="Green button submitted your name !!")
    else:
        # error appearing when you try to select an image before adding your name to the name field
        name_label.configure(text="Name cannot be empty")
        # focuses on the name field
        your_name.focus()


# GUI main window
root = Tk()
# window title
root.title("Reducing image size")

#window size
root.geometry("350x200")

# text label
enter_name = Label(text="Enter your name", font=("Arial Bold", 10))
enter_name.grid(column=0, row=0)

# users name entry field
your_name = Entry(root)
your_name.grid(column=2, row=0, columnspan=2)
#your_name.focus()

# button which submits users name
btn = Button(root, text="Submit name", bg="green", fg="white", command=submit_name)
btn.grid(column=4, row=0)

# text labels
label = Label(root, text="Select an image", font=("Arial Bold", 10))
label.grid(column=0, row=3)
error_label = Label(text="")
error_label.grid(column=0, row=4, columnspan=6)

# select image button
btn = Button(root, text="Select image", bg="blue", fg="white", command=select_image)
btn.grid(column=0, row=5)

# file name label
file_name = Label(text="")
file_name.grid(column=0, row=6, columnspan=3)

# lebel displaying when the green button is clicked
lbl = Label(root, text="")
lbl.grid(column=0, row=10, columnspan=4)

# label showing users name when its submitted
name_label = Label(text="")
name_label.grid(column=0, row=11, columnspan=5)


root.mainloop()




