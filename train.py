import json
import os
import glob

basepath="/mnt/c/Users/aofek/Desktop/proj"
markup_json_path_glob=basepath+"/training/annotations/*/ball_markup.json"

for markup_file in list(glob.glob(markup_json_path_glob)):
    with open(markup_file, 'r') as f:
        data = json.load(f)
        imagespath = os.path.dirname(markup_file).replace("annotations", "images")
        for item in data.items():
            x=item[1]['x']
            y=item[1]['y']
            if (x!=-1 and y!=-1):
                newdata = f"32 {x - 20} {y - 20} 40 40\n"
                print(imagespath + f"/img_{int(item[0]):07d}.txt")
                with open(imagespath + f"/img_{int(item[0]):07d}.txt", "w") as fw:
                    fw.write(newdata)
