import os 
  
# Function to rename multiple files 
def rename(): 
    i = 1
      
    for filename in os.listdir("Input_Images"): 
        dst = str(i) + ".jpg"
        src = 'Input_Images/'+ filename 
        dst ='Input_Images/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  