with open('day01.txt') as f:
    data = f.readlines()
    data = [int(i.rstrip()) for i in data]

    depth_increases = 0
    for i in range(len(data)):
        if i != 0:
            if data[i] > data[i-1]:
                depth_increases += 1
    print(f'Depth increases = {depth_increases}')

    depth_increases_sliding_window = 0
    new_data = []
    copy_data = data[:] + [0, 0]
    for i in range(len(data)):
        new_data.append(copy_data[i] + copy_data[i+1] + copy_data[i+2])

    for i in range(len(new_data)):
        if i != 0:
            if new_data[i] > new_data[i-1]:
                depth_increases_sliding_window += 1
    print(f'Depth increases sliding window = {depth_increases_sliding_window}')
