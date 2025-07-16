import os
import time
import random

from tqdm import tqdm
from PIL import Image

random.seed(0)

rootFolder = "Datasets/Generate/"
backgroundFolder = os.path.join(rootFolder,"B1B2")
sampleFolder = os.path.join(rootFolder,"Cidlo")
newFolder = os.path.join(rootFolder, "Gen6")

if not os.path.exists(newFolder):
    os.makedirs(newFolder)
f = open(os.path.join(newFolder, "annotation.csv"), "w")
f.write("name,x_left,y_up,x_right,y_down\n")


pbar = tqdm(os.listdir(backgroundFolder))
for background in pbar:
    for sample in tqdm(os.listdir(sampleFolder)):
        # Update tqdm progress bar
        pbar.set_postfix_str(f"B: {background.split('.')[0]}| S: {sample.split('.')[0]}")
        # Read images by PIL
        bgrImg = Image.open(os.path.join(backgroundFolder, background)).convert("RGBA").resize((224,224))
        splImg = Image.open(os.path.join(sampleFolder, sample)).resize((224,224))
        
        # Crop samples by alpha
        alpha = splImg.getchannel("A")
        abox = alpha.getbbox()
        splImg = splImg.crop(abox)

        for iter in range(10):
            # Resize sample 
            reduction = random.random() * 0.5 + 0.1 #* 50 + 10 #*2 2
            newImg = splImg.resize((int(splImg.size[0]*reduction),int(splImg.size[1]*reduction)))
            # Create mask for blending
            newSplImg = Image.new("RGBA", bgrImg.size)
            # Choose place for sample
            borders = tuple((n-o) for n, o in zip(bgrImg.size, newImg.size)) # To the center
            left = int(random.random() * (borders[0])) 
            up = int(random.random() * (borders[1]))
            box = tuple((left, up))
            # Paste sample to mask
            newSplImg.paste(newImg, box)
            # Compose background and mask
            img = Image.alpha_composite(bgrImg, newSplImg)
            #img.show()
            #time.sleep(5)

            # Save result
            nameFile = f"{background.split('.')[0]}_{sample.split('.')[0]}_{sample.split('.')[1]}_I{iter}.png"
            img.save(os.path.join(newFolder, nameFile))
            f.write(f"{nameFile},{left},{up},{left + newImg.size[0]},{up + newImg.size[1]}\n")
f.close()