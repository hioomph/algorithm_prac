import glob
import os

import numpy as np
import torch
from torch import nn

# # 从linear scale到log scale的非均匀采样
# a = 0.0001
# b = 1
# m = np.log10(a)  # -4.0
# n = np.log10(b)  # 0.0
# r = np.random.rand()  # 生成一个[0,1)范围内的浮点数
# r = m + (n-m)*r  # 取[m,n)内任意值
# r = np.power(10, r)  # 反推到[a,b]区间
#
#
# i = '+'
# tmp1 = 1
# tmp2 = 2
# # print(f'tmp2 + {i} + tmp1')
#
# nums = [1,2,3,4,7,2,4]
# root_index = nums.index(max(nums))
# # print(root_index)
#
# k = 10
# p = k // 2 if isinstance(k, int) else [x // 2 for x in k]
# # print(p)
#
# k = [2, 4, 5]
# p = k // 2 if isinstance(k, int) else [x // 2 for x in k]
# # print(p)
#
# import numpy
# arr = np.random.rand(2,3,2,2,4)
# print(arr)
# print('-------------------')
# print(arr[...,0])
#
# nums = [1, 2, 3]
# for i in range(len(nums)-1, -1, -1):
#     print("第{}个数是{}".format(i+1, nums[i]))

frames_dir = r'D:\\PostGraduate\\pythonex\\'

video_list = os.listdir(frames_dir)

for i in range(len(video_list)):
    print('processing video {}'.format(video_list[i]))
    frames = glob.glob(frames_dir + video_list[i] + '/*')
    print(frames)





