n = int(input()) 
 
for num in range(1, n + 1):
    digit_count = 0
    count_numbers = num
    while count_numbers > 0:
        digit_count += count_numbers
        count_numbers = int(count_numbers)
if digit_count == 5 or digit_count == 7 or digit_count == 11:
    print(f"{num}-> True")
else:    
    print(f"{num}-> False")        