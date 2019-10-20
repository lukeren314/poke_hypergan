import os
from PIL import Image
output_folder = "merged_data"

if not os.path.exists(output_folder):
    os.mkdir(output_folder)
index = 0
for dirname, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if(not dirname == output_folder and (".png" in filename)):
            img = Image.open(os.path.join(dirname, filename))
            img.save(output_folder+"/"+str(index)+".png")
            index += 1
print("Done")
