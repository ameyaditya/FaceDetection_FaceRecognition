#importing the the opencv package here
import cv2

#go to C:->Users-><username>->Anaconda3/4->Library->etc->haarcascades
#haarcascade is a object detection algorithm mainly used to detect faces eyes etc
#we will see how to code our own cascades later
#following is an example of face detection algorithm

#importing the faceCascade algorithm using the CascadeClassifier funtion of cv2 and storing it in face_cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#this function is to capture use your webcam
#if you have more than one camera, the attributes of VideoCapture will be incremented
frame = cv2.VideoCapture(0)

#while true, meaning, we want to loop continously until a key is pressed
while True:
    #the above frame variable capture the video, but is not stored anywhere
    #so we use the .read() function to get frames captured
    #notice this is in the loop, so will value of img will continously change every second
    #ret,img is used as the .read() function returns two values
    ret,img = frame.read()
    #Computers or algorithms always work with gray images as it makes the work a lot easier.
    #so here we convert the image to gray
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
    #The use of detectMultiScale()

    #basically what this does is finds a face and return the height and width of a face as if a rectangle is drawn
    #its visualization is seen below in the for loop
    faces = face_cascade.detectMultiScale(gray_img)
    #looping through the values, x-coordinate, y-coordinate which are the starting coordinates of the face
    #w is width and h is height
    for (x,y,w,h) in faces:
        #the .rectangle function is used to draw rectangles on an image
        #first parameter - where the rectangle is to be drawn
        #second - initial coordinates
        #third - width and height
        #fourth - colour of the rectangle
        #fifth - thickness of the rectangle
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #imshow function is to display the output in a separate window
    cv2.imshow('Face_recognition',img)
    #the waitkey fucntion basically takes the input from the keyboard and stores it in k
    k = cv2.waitKey(30) & 0xff
    #if the key pressed by the user is 'esc' which has a value equal to 27 thus 'k == 27'
    #break from the while loop
    if k == 27:
        break
#these are basically opencv conventions
#we always release the frame, meaning we had captured all video from webcam,
# just ending all connections the program made with the webcam
frame.release()
#this is to destroy all windows which were opened by the program
#example, we opened a window using imshows
cv2.destroyAllWindows()
