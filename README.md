# -.obj-file-alignment
---Introduce(En)---
This is a tool for aligning obj files exported from zbrush through rotation, translation, and scaling.
Through the two obj files of an object before and after transformation, calculate the rotation matrix, translation matrix and scaling coefficient, and apply the transformation to other obj files.

---Usage(En)---
1. Put the obj files before and after transformation in the root directory, rename the obj files before transformation to source.obj, and rename the transformed obj files to target.obj.
  Note: source.obj and target.obj should be exactly the same except for direction, position, and size
2. Put the obj file that needs to be processed into the 'input' folder
3. run trans.py
4. The processed files will be saved in the 'output' folder



---说明(Ch)---
这是一个用于对齐Zbrush导出的obj文件的工具。
通过一个物体在变换前后的两个obj文件，计算旋转矩阵、平移矩阵以及缩放系数，并将变换应用于其他代处理的obj文件

---使用(Ch)---
1. 将变换前后的obj文件放在根目录中，将变换前的obj文件重命名未source.obj，将变换后的obj文件重命名未target.obj。
  注意：source.obj和target.obj除方向、位置、大小外，应完全一致
2. 将带处理的obj文件放入input文件夹中
3. 运行trans.py
4. 处理后的文件将会保存在output文件夹中
