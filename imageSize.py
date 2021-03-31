from PIL import Image
import os

# Put this script into your photos directory then run it 

# Image size x, y PX
imgSize = (2560,1440)

# Get script directory
directory = os.getcwd()

# Check output dir 
if(os.path.isdir(os.getcwd()+'/output') == True):
    # if output dir is exists
    print('Ten folder juz istnieje')
else:
    # create dir
    os.mkdir('output')

for filename in os.listdir(directory):
    # If file type is
    if filename.endswith((".jpg",".jpeg",".png")):
        # Load image
        img = Image.open(filename)
        # Resize img
        resized = img.resize(imgSize)
        # Generate file name
        nameGenerated = 'IMG_'+filename
        # Save image to output directory
        resized.save(directory+'/output/'+nameGenerated)
        continue
    else:
        continue