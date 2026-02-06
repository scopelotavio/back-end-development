num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

counter = 0

for i, number in enumerate(num_list):
    if number == 36:
        print(f"Number found at position: ", i)
        break
    counter += 1

print(counter)




