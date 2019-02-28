import sys, os
import json

in_name_dog = sys.argv[1]
in_name_cow = sys.argv[2]
out_name = sys.argv[3]

list_out = []

def add_bbox(in_name):
	global list_out
	with open(in_name) as df:
		lines = df.readlines()
	for line in lines:
		elem  = {}
		line_contents = line.split()
		image_id = line_contents[0]
		vall = 0
		elem["category_id"] = 0
		if "dog" in image_id:
			vall = 10000
			elem["category_id"] = 1
		image_id = vall + int(image_id[4:])
		elem["image_id"] = image_id
		line_contents = line_contents[1:]
		new = []
		for line_content in line_contents:
			new.append(float(line_content))
		line_contents = new
		elem["score"] = line_contents[0]
		elem["bbox"] = []
		elem["bbox"].append(int(line_contents[1]))
		elem["bbox"].append(int(line_contents[2]))
		elem["bbox"].append(int(line_contents[3]-line_contents[1]))
		elem["bbox"].append(int(line_contents[4]-line_contents[2]))
		list_out.append(elem)

add_bbox(in_name_dog)
add_bbox(in_name_cow)

with open(out_name,'w') as fp:
	json.dump(list_out, fp)



