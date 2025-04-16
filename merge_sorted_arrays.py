# def merged_array(arr1,arr2):
#     merged=[]
#     i,j=0,0
#     while i<len(arr1) & j< len(arr2):
#         if arr1[i] <= arr2[j]:
#             merged.append(arr1[i])
#             i=i+1
#         else:
#             merged.append(arr2[j])
#             j=j+1
#     merged.extend(arr1[i:])
#     merged.extend(arr2[j:])
#     return merged

# a=merged_array([1,3,5],[2,6,8,9])
# print(a)


# second type 
# def merged_array(arr1,arr2):
#     len1,len2=len(arr1),len(arr2)
#     result=""
#     max_length=max(len1,len2)
#     for i in range(max_length):
#         if i<len1:
#             result=result+arr1[i]
#         if i<len2:
#             result=result+ arr2[i]
#     return result
# a=merged_array(['1','2'],['2','4','5'])
# print(a)