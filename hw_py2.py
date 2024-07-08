import random

def get_numbers_ticket(min, max, quantity):
   
    # turn input data into integers
    min = int(min)
    max = int(max)
    quantity = int(quantity)

    # check if data matches condition
    if min < 1 or max >= 1000 or quantity > (max - min + 1) or min > max:
        print(min)
        return "Ви ввели некоректні дані"
    
    # randomize and sort
    numbers = random.sample(range(min, max + 1), quantity) 
    numbers.sort()
    return numbers

min = input("Введіть мінімальне число: ")
max = input("Введіть максимальне число (max: 1000): ")
quantity = input("кількість переможних варіантів: ")
print(get_numbers_ticket(min, max, quantity))  
