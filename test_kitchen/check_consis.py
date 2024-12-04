import os

images = sorted(os.listdir('/media/sber20/Be2R/data/SLAM/Kitchen_data/zedx_livox_kitchen_V1_1/mav0/cam0/data'))
images = [img[:-4] for img in images]

with open('./traj_zedx_kitchen_1.txt',  'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip().split(' ')[0][:-2]
    if line not in images:
        print(line)