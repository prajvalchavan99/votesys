from django.shortcuts import render
from django.http import HttpResponse
import cv2
import time

# Create your views here.
def home(request):
    return render(request,'home1.html')

def capture(request):
    # while True:
    try:
        webcam=cv2.VideoCapture(0)
        key=cv2.waitKey(1)
        frame=webcam.read()
        time.sleep(3)
        cv2.imwrite(filename="savedimage.jpg",img=frame)
        webcam.release()
        # if key==ord('q'):
        #     webcam.release()
        #     cv2.destroyAllWindows()
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()

    return render(request,'home1.html')

def confirm(request):
    return render(request,'confirm.html')
