import sys
import os
from PIL import Image



def get_image_name(image_path):
    path_ele = image_path.split("/")

    return path_ele[-1]




if __name__ == "__main__":
    n = len(sys.argv)

    for i in range(1, n):
        print(sys.argv[i])
    
    arguementList = sys.argv[1:]

    jpg = False   #-c
    jpeg = False  #-m
    png = False #-l
    webp = False #-w

    #if an argument does not start with '-' or '--' then it is a input file 

    for argument in arguementList:
        if (argument[0] != '-') or (argument[0] != '-' and argument[1] != '-'):
                image_file_path = argument

    if image_file_path:
        image_file = get_image_name(image_file_path)

        image_file_name = image_file.split(".")[0]
        image_file_ext = image_file.split(".")[1]

    try:
        image = Image.open(image_file)

    except FileNotFoundError:
        print("Couldn't find the provided Image")
        exit(0)
      
    


    

    for argument in arguementList:
        if argument in ("-jpg"):
            jpg = True
        
        elif argument in ("-jpeg"):
            jpeg = True
        
        elif argument in ("-png" ):
            png = True
    
        elif argument in ('-webp'):
            webp = True

        
     

      
    

    

    
    if(jpg):
        image = image.conver('RGB')

        image.save(image_file_name + ".jpg")

    if(jpeg):
        image = image.conver('RGB')
        image.save(image_file_name + ".jpeg")

    if(png):
        image.save(image_file_name + ".png")

    
    if(webp):
        image.save(image_file_name + ".webp")

    print("file_converted Succesfully")













