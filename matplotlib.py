from matplotlib import pyplot as plt


def get_data(file):
    file = open(file, 'r', encoding='utf8')
    city_name = []
    nums = []
    total = ()
    for line in file:
        name = line.strip().split(':')
        city_name.append(name[0])
        num = line.split(':')[1].strip().split(', ')
        num = list(map(int, num))

        nums.append(num)

    file.close()
    return city_name, nums


print(get_data('dots.txt'))
