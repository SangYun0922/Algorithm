N = int(input())
voca_list = []
voca_dict = {}
value_list = []

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
result = 0
for i in range(N) :
    voca = input()
    voca_list.append(voca)

for i in range(len(voca_list)) :
    for j in range(len(voca_list[i])) :
        if (not voca_list[i][j] in voca_dict) :
            voca_dict[voca_list[i][j]] = 10 ** (len(voca_list[i]) - j - 1)
        else :
            voca_dict[voca_list[i][j]] += 10 ** (len(voca_list[i]) - j - 1)

for i in voca_dict.values() :
    value_list.append(i)
value_list = sorted(value_list, reverse=True)

for i in range(len(value_list)) :
    result += value_list[i] * int(nums[i])

print(result)

