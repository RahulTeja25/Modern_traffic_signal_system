import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
vid = cv2.VideoCapture(1)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object


    #im1 = cv2.imread('image.jpg')
    #im2 = cv2.imread('lane2.jpeg')
    #im3 = cv2.imread('lane3.jpeg')
    #im4 = cv2.imread('lane4.jpeg')
    im = cv2.imread(frame)
    bbox1, label1, conf1 = cv.detect_common_objects(frame)
    # bbox2, label2, conf2 = cv.detect_common_objects(im2)
    # bbox3, label3, conf3 = cv.detect_common_objects(im3)
    # bbox4, label4, conf4 = cv.detect_common_objects(im4)
    #output_image1 = draw_bbox(im1, bbox1, label1, conf1)
    #output_image2 = draw_bbox(im2, bbox2, label2, conf2)
    #output_image3 = draw_bbox(im3, bbox3, label3, conf3)
    #output_image4 = draw_bbox(im4, bbox4, label4, conf4)
    d11=label1.count('car')
    d12=label1.count('motorcycle')
    d13=label1.count('bus')

    t1=d11+d12+d13

    print("Modern traffic system")
    print('Number of vehicles in the lane1 is ')
    print(t1)
    plt.imshow(output_image1)
    plt.show()

vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
