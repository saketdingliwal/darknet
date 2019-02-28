import os, sys

dir_name = sys.argv[1]
csv_name = sys.argv[2]

os.system("wget https://owncloud.iitd.ac.in/nextcloud/index.php/f/7553236")
os.system("python convert.py " + dir_name + " " + csv_name)

out_file = open('data/test.txt','w')
for root, dirs, files in os.walk(dir_name):
	for file in files:
		if file.endswith(".jpg"):
			out_file.write(dir_name + '/' + file + "\n")
out_file.close()

os.system("./darknet detector valid data/coco.data cfg/yolov3.cfg yolov3.weights")
os.system("python convert_to_json.py results/comp4_det_test_cow.txt results/comp4_det_test_cow.txt yolo_res.json")

