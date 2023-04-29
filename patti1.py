from PIL import Image
import glob
import os
#from time import sleep
path = "C:\\Users\ANDREA NARCIS\Desktop\leaf\captured_images"


#CONVERT TO GRAYSCALE
def get_imlist_gs(path):
       
    list_of_images_in_folder =  [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.png')]
    print ("")   
    print ("...finding images")
    
    print ("") 
  
    print ("...found the following images")
    print ("")
   
    print (list_of_images_in_folder)
    print ("")
    
     
    # Enter the new size that you want
    print ("Please enter your new sizes in pixels")
    print ("")
    width_new = int(input("Enter that width "))
    height_new = int(input("Enter that height "))
    
   # new_image_fill_name = 0
    
    for image in list_of_images_in_folder:
        
        # Opens a image in RGB mode

        #print (image)

        
        original_im = Image.open(image)
        # Resize the image
        newsize = (width_new, height_new)
        final_image = original_im.resize(newsize)
        final_image = final_image.convert('LA')
        # Shows the image in image viewer
        final_image.show() # for testing

        #extract the filename from the image list
        #extract_filename = image
        #start = extract_filename.find("resize/")
        #finish = extract_filename.find(".png")
        #print (start) #for testing
        #print (finish) #for testing
        #final_filename = extract_filename[start:finish]
        #print (final_filename) #for testing  

        #sleep (15)
        # Saves the new image
        '''change the file names!'''
        Resized="C:\\Users\ANDREA NARCIS\Desktop\leaf\captured_images\Resized"
        if not os.path.exists(Resized):
            os.makedirs(Resized)
        count=0
        for i in list_of_images_in_folder:
            name='new_image'+str(count)+'.png'
            count+=1
    

            final_image.save(os.path.join(Resized,name) )
get_imlist_gs(path)