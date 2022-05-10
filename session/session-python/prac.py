item_list = ["윤한", "현우", "수연", "다민", "민서"]
print(item_list[3])

item_list[0] = "지원"

item_list.append("영권")
print(item_list)

item_dic = {"key1":111, "key2":222}
item_dic["key1"] = 222
item_dic["key3"] = 333
print(item_dic["key1"])
dic_val = item_dic.values()
print(dic_val)
item_dic.items()
item_dic.keys()

for item in item_list:
    if item == "다민":
        print(item)

num_list = [1,2,3,4,5,6,7,8,9,10]

new_data= []
for n in num_list:
    if n % 2 == 0:
        new_data.append(n)

print(new_data)

str = "윤한 현우 수연 다민 민서"
name = "윤한"
if name in str:
    print("윤한이가 있대")
else: print("걔 없대")