
# guess là một trò chơi đơn giản trong Python, nơi người chơi cố gắng đoán một số mà máy tính đã chọn ngẫu nhiên. 
# Máy tính sẽ cung cấp phản hồi cho người chơi về việc số đoán của họ là quá cao, quá thấp hay chính xác. 
# Trò chơi tiếp tục cho đến khi người chơi đoán đúng số hoặc quyết định dừng lại.

secret_word = "python"
hint = "It's a popular programming language."
guess = ""
guess_count = 0
guess_limit = 3

print(hint)

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        break
if guess == secret_word:
        print("Congratulations! You guessed the secret word.")
else:
        print("Incorrect guess. Try again.")