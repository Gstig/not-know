# numbers = [1, 2, 3, 4, 5, True, 'Python', ['q', 'w', 'e', 'r', 't', 'y']]

# numbers[0] = 25
# numbers[6] = 'Assembler'
# numbers[3] = 1024

# if numbers[4] == 25:
#     print("Yes, it is 25")
# else:
#     print(numbers[-1][4], 'There is no 25!')


# nums = [1, 2, 7, 4, 8, 8]

# nums.append(31415)
# nums.append(True)


# #nums.sort()
# #nums.reverse()
# #nums.insert(2, 'Python')

# nums.extend(['s', 't', 'i', 'g'])
# n = [5380704]
# nums.extend(n)

# nums.pop(-1)
# nums.remove(7)
# #nums.clear()

# print('Counting of index\'s quantity equals:', nums.count(8))
# print('Leight of index list equals:', len(nums))

# print(nums)


# list = [1, 2, 3, 4, 5, 6, 7, 'World', False]

# for el in list:
#     el *= 3
#     print(el)


prop = int(input('Enter lenght: '))

user_list = []

elm = 0

while elm < prop:
    string = 'enter element #' + str(elm + 1) + ': ' 
    user_list.append(input(string))
    elm += 1
print(user_list)