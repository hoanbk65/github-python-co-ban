
# Exception (Ngoại lệ)
# Throw an exception (Ném một ngoại lệ) là một cơ chế trong lập trình để xử lý các tình huống lỗi hoặc bất thường xảy ra trong quá trình thực thi chương trình. Khi một ngoại lệ được ném, chương trình sẽ dừng thực hiện bình thường và chuyển sang xử lý ngoại lệ.   
# Handling an exception (Xử lý ngoại lệ) là quá trình bắt và xử lý các ngoại lệ đã được ném. Điều này cho phép chương trình tiếp tục thực hiện mà không bị gián đoạn hoặc kết thúc đột ngột.  

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")