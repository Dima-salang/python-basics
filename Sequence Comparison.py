#  Sequence comparison will compare individual elements within a sequence and if first elements are equal, move on
#  with second element of both lists and so on.

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [1, 2, 3, 4, 5]
print(num_list1 == num_list2)  # True

num_list3 = [1, 2, 4]
num_list4 = [1, 2, 3]
print(num_list3 < num_list4)  # False

abc = ["a", "b", "c"]
ABC = ["D", "E", "F"]
print(abc > ABC)  # True because lowercase letters are greater

string_list = ["a", "b", "c"]
string_list2 = ["d", "b", "c"]
print(string_list > string_list2)  # False because d is greater than a
