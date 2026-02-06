import time
start_time = time.time()



# outer loop
for i in range(100):
    # inner loop
    for j in range(1000):
        print(0, end = " ")
    print()

print(round(time.time() - start_time, 2))