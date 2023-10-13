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

    jpg = False   
    jpeg = False  
    png = False 
    webp = False 

    if ("--help" in arguementList):
        print("Usage img-change.py [filename]/[filepath] options")
        print("OPTIONS")
        print("-jpeg \n -jpg \n -png \n -webp")
        print("For example: img-change.py images/test.png -jpeg")

    #if an argument does not start with '-' or '--' then it is a input file 

    for argument in arguementList:
        if (argument[0] != '-') or (argument[0] != '-' and argument[1] != '-'):
                image_file_path = argument
                break
        


    if image_file_path:
        image_file = get_image_name(image_file_path)

        image_file_name = image_file.split(".")[0]
        image_file_ext = image_file.split(".")[1]

    try:
        image = Image.open(image_file)

    except FileNotFoundError:
        print("Couldn't find the provided Image")
        print("See --help")
        exit(0)
      
    
    for argument in arguementList:
       

        if argument in ("-jpg"):
            if (image_file_ext == "jpg"):
                print(f"{image_file_name} is already jpg")
                exit(0)
            jpg = True
        
        if argument in ("-jpeg"):
            if (image_file_ext == "jpeg"):
                print(f"{image_file_name} is already jpeg")
                exit(0)
            jpeg = True
        
        if argument in ("-png" ):
            if (image_file_ext == "png"):
                print(f"{image_file_name} is already png")
                exit(0)
            png = True
    
        if argument in ('-webp'):
            if (image_file_ext == "webp"):
                print(f"{image_file_name} is already webp")
                exit(0)
            webp = True
        
        

    if not (jpg or jpeg or png or webp):
        print("see --help")



    if(jpg):
        image = image.conver('RGB')

        image.save(image_file_name + ".jpg")
        print("file converted to jpg")


    if(jpeg):
        image = image.conver('RGB')
        image.save(image_file_name + ".jpeg")
        print("file converted to jpeg")

    if(png):
        image.save(image_file_name + ".png")
        print("file converted to png")

    
    if(webp):
        image.save(image_file_name + ".webp")
        print("file converted to webp")














