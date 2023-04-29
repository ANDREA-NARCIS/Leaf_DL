import numpy as np
import cv2
import joblib
import os.path
from DataPreProcessing import obtainXY,getAllFeatures,getTreeData
from TestingClassifiers import makeClassifiers
import sys
import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
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
  

def imageX(image_path):
    meanX, stdX = np.loadtxt('normalValues.txt')
    length, width, area, perimeter, aspect_ratio, form_factor, rectangularity, hu, hist = getAllFeatures(image_path)
    x = np.array([])
    # x = np.append(x, length)
    # x = np.append(x, width)
    x = np.append(x, area)
    x = np.append(x, perimeter)
    x = np.append(x, aspect_ratio)
    x = np.append(x, form_factor)
    x = np.append(x, rectangularity)
    x = np.append(x, hu)
    x = np.append(x, hist)
    x = x.reshape(1, x.shape[0])
    x = (x - meanX)/stdX
    return(x)

def Execute(image_path):
    if os.path.exists("C:\\Users\patha\OneDrive\Desktop\leaf-recognition-master\normalValues.txt")==False:
        makeClassifiers()

    clf1 = joblib.load('knnDump.pkl')
    clf2 = joblib.load('svmDump.pkl')
    clf3 = joblib.load('mlpDump.pkl')

    x = imageX(image_path)

    print("Data Read In")

    prediction = np.array([clf1.predict(x)[0], clf2.predict(x)[0], clf3.predict(x)[0]])
    print(prediction)
    counts = np.bincount(prediction)
    finalPre = np.argmax(counts)
    treeJson = getTreeData(str(finalPre))
    print(treeJson)
    treeJson=eval(treeJson)
    print(treeJson["CommonName"])
    match treeJson['CommonName']:
        case "Japanese Maple":
            print("EDIBLE")
            print("Medical values- treats bruies,hepatic disorder, eye disease and pain,detoxification")
        
        case "Deodara":
            print("EDIBLE")
            print("Medicinal value- treats disorder of mind,infections,disease of skin amd blood")
        case "Chinese Redbud":
            print('EDIBLE')
            print("")
            
        

Execute(r"C:\\Users\patha\OneDrive\Desktop\helmet\leaf-recognition-master\Leaf Database\Acer Palmatum\1271.jpg")
# Execute('./Test Leaves/Cedrus Deodara/2397.jpg')lab ab to m
# Execute('./Test Leaves/Cercis Chinensis/1173.jpg')
# Execute('./Test Leaves/Citrus Reticulata Blanco/3616.jpg')
# Execute('./Test Leaves/Ginkgo Biloba/2483.jpg')
# Execute('./Test Leaves/Liriodendron Chinense/3561.jpg')
# Execute('./Test Leaves/Nerium Oleander/2597.jpg')

cv2.waitKey(0)
vid.release()
cv2.destroyAllWindows()