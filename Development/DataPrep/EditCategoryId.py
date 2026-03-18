import os
import json
from pycocotools.coco import COCO

folder = "Datasets/NoveAnotovana/Dataset04_COCO_fromGen5/"

coco = COCO(os.path.join(folder, "result.json"))
coco.dataset["categories"][0]["id"] = 5
for value in coco.dataset["annotations"]:
    value["category_id"] = 5

with open(os.path.join("D4-repaired.json"), "w") as outfile: 
    json.dump(coco.dataset, outfile)