x= input("Enter a number: ")
y = input("Enter another number: ")
sum = float(x) + float(y)
print("The sum is:", sum)


# formatting strings
my_age =26
my_height = 5.9
text ="I am {1} years old and my height is {0} feet."
print(text.format(my_height, my_age))

# dữ liệu danh sách
teams = ["Team A", "Team B", "Team C"]
teams[1] = "Team D"
print(teams)

# append: thêm phần tử vào cuối danh sách
# insert: thêm phần tử vào vị trí chỉ định
# remove: xóa phần tử khỏi danh sách
# clear: xóa tất cả các phần tử khỏi danh sách
# pop: xóa phần tử khỏi danh sách và trả về giá trị của phần tử đó
# index: trả về vị trí của phần tử trong danh sách
# count: trả về số lần xuất hiện của phần tử trong danh sách
# sort: sắp xếp danh sách theo thứ tự tăng dần
# reverse: sắp xếp danh sách theo thứ tự giảm dần
# copy: tạo một bản sao của danh sách

student_names = ["Alice", "Bob", "Charlie"]
math_scores = [85, 92, 78]

'''student_names.append("David")
print(student_names) '''

'''student_names.insert(1, "Eve")
print(student_names)'''

student_names.remove("Bob")
print(student_names)


# tuple: giống như danh sách nhưng không thể thay đổi giá trị của các phần tử trong tuple

x = (1, 2, 3)
print(x[0])  


