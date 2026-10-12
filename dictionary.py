
# dictionary là một kiểu dữ liệu trong Python được sử dụng để lưu trữ các cặp khóa-giá trị (key-value pairs). 
# Mỗi khóa trong dictionary phải là duy nhất và có thể được sử dụng để truy xuất giá trị tương ứng. 
# Dictionary được định nghĩa bằng cách sử dụng dấu ngoặc nhọn {} và các cặp khóa-giá trị được phân tách bằng dấu hai chấm (:).

english_vietnamese_dictionary = {
    
    "hello": "xin chào",
    "goodbye": "tạm biệt",
    "thank you": "cảm ơn",
    "yes": "vâng",
    "no": "không"
}

print(english_vietnamese_dictionary.get("hello"))  
print(english_vietnamese_dictionary.get("dog")) 
