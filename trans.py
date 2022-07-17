import numpy as np
from numpy import *
import os

imput_Path = 'input/'
output_Path = 'output/'

def read_Points(txt_file):
    #read .obj file as .txt file
    points_lst = []
    for line in txt_file:
        if 'v' in line and '#' not in line:
            line_split = line.split(' ')
            x = float(line_split[1])
            y = float(line_split[2])
            z = float(line_split[3][:-1])
            points_lst.append([x,y,z])
    return points_lst

def get_all_side_length(points):
	all_dis=[]
	for i in range(len(points)-1):
		for j in range(i+1,len(points)):
			all_dis.append(points[i]-points[j])
	all_dis=np.array(all_dis)
	return np.linalg.norm(all_dis,axis=1)
	
def get_scale(A,B):
	dis_A=get_all_side_length(np.array(A))
	dis_B=get_all_side_length(np.array(B))
	scale=np.abs(dis_B/dis_A)
	mask=np.abs(scale)>0.0001  
	scale_sort=np.sort(scale[mask].reshape(-1))
	d_n=len(scale_sort)
	s_mean=scale_sort[int(d_n/4):int(d_n*3/4)].mean() #only use medium data
	return s_mean

def estimate_transform(source, target):
	## compute rotation matrix
    assert len(source) == len(target)
    N = source.shape[0]
    mu_source = mean(source, axis=0)
    mu_target = mean(target, axis=0)

    sourceA = source - tile(mu_source, (N, 1))
    targetB = target - tile(mu_target, (N, 1))
    H = transpose(sourceA) * targetB

    U, S, Vt = linalg.svd(H)
    rotation_Matrix = Vt.T * U.T

    if linalg.det(rotation_Matrix) < 0:
        print("Reflection detected")
        Vt[2, :] *= -1
        rotation_Matrix = Vt.T * U.T

    s_mean=get_scale(source,target)

    translation_Matrix = -s_mean * rotation_Matrix * mu_source.T + mu_target.T

    return rotation_Matrix, translation_Matrix ,s_mean

source = open("source.obj", 'r', encoding='utf-8')
target = open("target.obj", 'r', encoding='utf-8')


source_points = read_Points(source)
target_points = read_Points(target)

rotation_Matrix, translation_Matrix ,s_mean = estimate_transform(mat(source_points), mat(target_points))
sR = s_mean*rotation_Matrix



for filename in os.listdir(imput_Path):

    objects = open(imput_Path + filename, 'r', encoding='utf-8')
    object_points = read_Points(objects)

    #apply the transformation
    object_points = mat(object_points)
    object_points = (sR*object_points.T)+ translation_Matrix
    object_points = object_points.T
    object_points = np.array(object_points)


    transed = open(output_Path + filename, 'w', encoding='utf-8')
    objects = open(imput_Path + filename, 'r', encoding='utf-8')

    i = 0

    for o_line in objects:
        if 'v' in o_line and '#' not in o_line:
            transed.write('v ')

            transed.write(str(object_points[i][0]) + ' ')
            transed.write(str(object_points[i][1]) + ' ')
            transed.write(str(object_points[i][2]) + '\n')
            i += 1
        else:
            transed.write(o_line)
    
    transed.close()
    objects.close()
