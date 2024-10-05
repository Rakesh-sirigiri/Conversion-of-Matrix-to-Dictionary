list = [[5,6,7], [8,3,2], [8,2,1]]
print("The original list is : " +str(list))
res = {idx + 1 : list[idx] for idx in range(len(list))}
print("The constructed dictionary : " + str(res))
