# number = [1,3,45,56,79,34,4,2]
# highest = 0
# second_highest = 0
#
# for num in number:
#     if num > highest:
#         second_highest = highest
#         highest = num
# print("highest number is:", highest)
# print("second_highest number is:", second_highest)

number = [1,93,45,56,79,34,4,2]
highest = 0
second_highest = 0

for num in number:
    if num > highest:
        second_highest= highest
        highest = num

    elif num > second_highest:
        second_highest = num

print("highest number is:", highest)
print("second_highest number:", second_highest)















