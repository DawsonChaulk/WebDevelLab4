def split_the_bill(total, tip, number_of_guests):
    return (total + tip) / number_of_guests

print(split_the_bill(90, 15, 2))
print(split_the_bill(45.67, 10, 2))
print(split_the_bill(85.50, 20, 5))