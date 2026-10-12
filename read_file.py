
phone = open("phone.txt", "r")

 #print(phone.readlines())

for person in phone.readlines():
    person = person.replace("\n", "")
    print(person)

phone.close()

# readline() là một phương thức được sử dụng để đọc một dòng từ tệp. Khi gọi phương thức này, nó sẽ trả về một chuỗi chứa nội dung của dòng tiếp theo trong tệp. Nếu đã đọc hết các dòng trong tệp, phương thức sẽ trả về một chuỗi rỗng.
# realines() là một phương thức được sử dụng để đọc tất cả các dòng từ tệp và trả về chúng dưới dạng một danh sách các chuỗi. Mỗi phần tử trong danh sách sẽ tương ứng với một dòng trong tệp. Nếu tệp rỗng, phương thức sẽ trả về một danh sách rỗng.