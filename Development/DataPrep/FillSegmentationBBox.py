# Check ann with pycocotools
from pycocotools.coco import COCO
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import os

#coco = COCO(os.path.join(ann_dir, annFile))
#coco = COCO(os.path.join("./DS_sorted/Real", "train.json"))
import json

# Open and read the JSON file
with open(os.path.join("./DS_sorted/Real", "testDiff.json"), 'r') as file:
    data = json.load(file)

for ann in data["annotations"]:
    box = ann["bbox"]
    ann["segmentation"] = [[box[0],box[1]+box[3],box[0]+box[2],box[1]+box[3],box[0]+box[2],box[1],box[0],box[1]]]
    #[[df["x_left"][rowId], df["y_up"][rowId], df["x_right"][rowId], df["y_up"][rowId], df["x_right"][rowId], df["y_down"][rowId], df["x_left"][rowId], df["y_down"][rowId]]]

with open(os.path.join("./DS_sorted/Real", "testDiff.json"), "w") as outfile: 
    json.dump(data, outfile)

"""
# Check ann with pycocotools
from pycocotools.coco import COCO
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np

#coco = COCO(os.path.join(ann_dir, annFile))
coco = COCO(os.path.join("./", annFile))

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['detector'])
imgIds = coco.getImgIds(catIds=catIds)
#imgIds = coco.getImgIds(imgIds=[0])
ranIdx = np.random.randint(0,len(imgIds))
imgs = coco.loadImgs(imgIds[ranIdx:ranIdx+2])

for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)

    I = io.imread("./DS_sorted/Real/train/images/"+ img['file_name'])
    plt.axis('off')
    plt.imshow(I)
    coco.showAnns(anns, draw_bbox=False)
    plt.show()
"""
