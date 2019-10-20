import imageio
import os
input_folder = "./old_saves/samples"
model_name = "128x128model1"
output_folder = "./gifs"

if(not os.path.exists(output_folder)):
    os.mkdir(output_folder)
images = []
for each in os.listdir(os.path.join(input_folder, model_name)):
    images.append(imageio.imread(os.path.join(input_folder, model_name, each)))
imageio.mimsave(os.path.join(output_folder, model_name)+".gif", images)
print("Done!")
