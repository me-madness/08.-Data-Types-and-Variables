n = int(input()) 
 
for num in range(1, n + 1):
    count_numbers = str(num)
    digit_count = 0
    for number in count_numbers:
        digit_count += int(number)
    if digit_count == 5 or digit_count == 7 or digit_count == 11:
        print(f"{num}-> True")
    else:    
        print(f"{num}-> False")        