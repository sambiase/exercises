import time

list_nr=[int(i) for i in range(0,1000000)]
start = time.time()
for i in list_nr:
    print(i)

end = time.time() - start

print(f'It took: {end:2f} seconds to run this program')