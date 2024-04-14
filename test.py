# def binary_search(list:list,target:int)->int:
#     low = 0
#     high = len(list) - 1
#     while low < high:
#         mid = low + (high-low) // 2
#         if list[mid] == target:
#             return mid
#         elif list[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1

# def naive_search(lst,target):
#     for i in range(len(list)):
#         if list[i] == target:
#             return i
#     return -1

# def recursive_search(list,target,low=0,high=-1):
#     if high < 0:
#         high = len(list)-1
#     if low > high:
#         return -1
#     mid = low + (high-low)//2
#     if list[mid] == target:
#         return mid
#     elif list[mid] > target:
        
#         return recursive_search(list,target,low,mid-1)
#     else:
        
#         return recursive_search(list,target,mid+1,high)

# list = [3,6,8,54,32,54,7,84,6,51,58,234]
# list = sorted(list)
# # res = binary_search(list, 32)
# # print(res)
# # res = naive_search(list,32)
# # print(res)
# res = recursive_search(list,31)
# print(res)





#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import openpyxl
# from openpyxl import load_workbook

# # 程序主入口
# if __name__ == "__main__":
#     # 读取excel数据
#     wb = load_workbook('test.xlsx', data_only=True)
#     sheet = wb.active
#     # 写表excel数据
#     write_wb = openpyxl.Workbook()
#     write_sheet = write_wb.active
#     print('开始写入excel')
#     # 表头信息
#     cxcel_title = [
#         'title_1',
#         'title_2',
#         'title_3',
#         'title_4',
#         'title_5',
#         'title_6'
#     ]
#     # 表头写入Excel中
#     write_sheet.append(cxcel_title)
#     # 循环写入旧Excel数据
#     for row in sheet.rows:
#         # 行信息
#         title_1 = row[0].value
#         title_2 = row[1].value
#         title_3 = row[2].value
#         title_4 = row[3].value
#         title_5 = row[4].value
#         title_6 = row[5].value
#         excel_row = [
#             title_1,
#             title_2,
#             title_3,
#             title_4,
#             title_5,
#             title_6
#         ]
#         # 写入Excel中
#         write_sheet.append(excel_row)
#     # 生成excel文件
#     write_wb.save('new_test.xlsx')
#     print('写入excel完成！')



