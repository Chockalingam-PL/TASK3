user_input = [10,501,22,37,100,999,87,351]

even_number_list = []
odd_number_list =[]
for number in user_input: # 10,501,22,37,100,999,87,351
    if number % 2 == 0:
        even_number_list.append(number)
    else:
        odd_number_list.append(number)

print(even_number_list)
print(odd_number_list)