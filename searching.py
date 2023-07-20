shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "eggs"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
if item_to_find in shopping_list: #không cần dùng vòng lặp để tìm mà có thể dùng hàm i
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} is not found".format(item_to_find))

