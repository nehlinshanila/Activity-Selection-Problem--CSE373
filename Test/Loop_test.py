start = 10
end = 1000000

array_size = []

while start <= end:
    print(start)

    if start < 100:
        start += 10
    elif start < 1000:
        start += 100
    elif start < 10000:
        start += 1000
    else:
        start += 10000
    
    array_size.append(start)
    


with open('input_size.txt', 'w') as file:
    for size in array_size:
        file.write(str(f'{size:.2f}') + '\n')