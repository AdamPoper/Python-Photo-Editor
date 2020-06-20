from tkinter import *
from PIL import ImageTk, Image, ImageEnhance

CANVAS_SIZE = 650
def adjustSize(img):
    width, height = img.size
    scale = 1
    if width > CANVAS_SIZE or height > CANVAS_SIZE:
        if width > height:
            scale = CANVAS_SIZE / width
        elif height > width:
            scale = CANVAS_SIZE / height
        else:
            scale = 1
    width *= scale
    height *= scale
    return width, height

def brighten(slider):
    val = slider.get()
    global mainImg 
    global viewImg
    global mainImgLabel
    global originalImg
    mainImg = originalImg
    enhancer = ImageEnhance.Brightness(mainImg)
    mainImg = enhancer.enhance(val)
    viewImg = ImageTk.PhotoImage(mainImg)
    mainImgLabel.configure(image=viewImg)

def adjustContrast(slider):
    val = slider.get()
    global mainImg
    global viewImg
    global mainImgLabel
    global originalImg
    mainImg = originalImg
    enhancer = ImageEnhance.Contrast(mainImg)
    mainImg = enhancer.enhance(val)
    viewImg = ImageTk.PhotoImage(mainImg)
    mainImgLabel.configure(image=viewImg)
    
def applyChanges():
    global mainImg
    global originalImg
    originalImg = mainImg

def adjustSaturation(slider):
    val = slider.get()
    global mainImg
    global viewImg
    global mainImgLabel
    global originalImg
    mainImg = originalImg
    enhancer = ImageEnhance.Color(mainImg)
    mainImg = enhancer.enhance(val)
    viewImg = ImageTk.PhotoImage(mainImg)
    mainImgLabel.configure(image=viewImg)

def adjustSharpness(slider):
    val = slider.get()
    global mainImg
    global viewImg
    global mainImgLabel
    global originalImg
    mainImg = originalImg
    enhancer = ImageEnhance.Sharpness(mainImg)
    mainImg = enhancer.enhance(val)
    viewImg = ImageTk.PhotoImage(mainImg)
    mainImgLabel.configure(image=viewImg)

def openImage(tbox):
    global mainImg
    global originalImg
    global viewImg
    global mainImgLabel
    mainImg = Image.open(tbox.get())
    resize = adjustSize(mainImg)
    mainImg.thumbnail(resize)
    originalImg = mainImg
    viewImg = ImageTk.PhotoImage(mainImg)
    mainImgLabel.configure(image=viewImg)
    #mainImgLabel.image = viewImg

def saveImage(tbox):
    global mainImg
    mainImg.save(tbox.get() + ".jpg")

def main():
    window = Tk()
    window.geometry("900x540")
    global originalImg
    global mainImg
    global viewImg
    global mainImgLabel
    mainImgLabel = Label(window)

    sliderBrightness = Scale(window, from_=0, to=3, resolution=0.1, orient=HORIZONTAL)
    sliderBrightness.set(1)
    sliderContrast = Scale(window, from_=0, to=3, resolution=0.1, orient=HORIZONTAL)
    sliderContrast.set(1)
    sliderSaturation = Scale(window, from_=0, to=3, resolution=0.1, orient=HORIZONTAL)
    sliderSaturation.set(1)
    sliderSharpness = Scale(window, from_=0, to=3, resolution=0.1, orient=HORIZONTAL)
    sliderSharpness.set(1)
    
    filePathLabel = Label(window, text="Enter Image File Path: ")
    filePathTbox = Entry(window, width=30)

    imageSaveLabel = Label(window, text="Save Image As: ")
    imageSaveTbox = Entry(window, width=30)
   
    changeBrightnessButt = Button(window, text="change brightness", command=lambda:brighten(sliderBrightness))
    applyButt = Button(window, text="submit changes", command=applyChanges)
    changeContrastButt = Button(window, text="change contrast", command=lambda:adjustContrast(sliderContrast))
    changeSaturationButt = Button(window, text="change saturation", command=lambda:adjustSaturation(sliderSaturation))
    changeSharpnessButt = Button(window, text="change sharpness", command=lambda:adjustSharpness(sliderSharpness))
    loadImageButt = Button(window, text="Open Image", command=lambda:openImage(filePathTbox))
    saveImageButt = Button(window, text="Save Image", command=lambda:saveImage(imageSaveTbox))

    mainImgLabel.grid(row=0, column=0, rowspan=6, columnspan=3)
    sliderBrightness.grid(row=0, column=3)
    changeBrightnessButt.grid(row=0, column=4)
    applyButt.grid(row=6, column=3)
    sliderContrast.grid(row=2, column=3)
    changeContrastButt.grid(row=2, column=4)
    sliderSaturation.grid(row=3, column=3)
    changeSaturationButt.grid(row=3, column=4)
    sliderSharpness.grid(row=4, column=3)
    changeSharpnessButt.grid(row=4, column=4)
    filePathLabel.grid(row=6, column=0)
    filePathTbox.grid(row=6, column=1)
    loadImageButt.grid(row=6, column=2)
    imageSaveLabel.grid(row=7, column=0)
    imageSaveTbox.grid(row=7, column=1)
    saveImageButt.grid(row=7, column=2)
    window.mainloop()
main()
