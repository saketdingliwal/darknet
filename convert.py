import os,sys

dir_name = sys.argv[1]
csv_name = sys.argv[2]

def center(xmin,ymin,xmax,ymax):
	return ((xmin+xmax)/2),((ymin + ymax)/2) 
def dimensions(xmin,ymin,xmax,ymax):
	return (xmax-xmin),(ymax-ymin)


image_map = {}
with open(csv_name,'r') as file:
	annotations = file.readlines()

for annotation in annotations:
	data_point = annotation.split(',')
	file_name = data_point[0]
	image_map[file_name] = data_point[1:]



for root, dirs, files in os.walk(dir_name):
	for file in files:
		if file.endswith(".jpg"):
			complete_file_name = os.path.join(root, file)
			print (image_map[file])
			new_text_file = complete_file_name[:-3] + "txt"
			label_file = open(new_text_file,'w')
			label_str = image_map[file][2]
			if "dog" in label_str:
				label = "16"
			else:
				label = "19"
			label_file.write(label + " ")
			width = int(image_map[file][0])
			height = int(image_map[file][1])
			xmin = int(image_map[file][3])
			ymin = int(image_map[file][4])
			xmax = int(image_map[file][5])
			ymax = int(image_map[file][6])
			c_x, c_y = center(xmin,ymin,xmax,ymax)
			box_width, box_height = dimensions(xmin,ymin,xmax,ymax)
			label_file.write(str((c_x*1.0)/width) + " " + str((c_y*1.0)/height) + " " + str((box_width*1.0)/width) + " " + str((box_height*1.0)/height))
			label_file.close()

