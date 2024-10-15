from matplotlib import pyplot as plt


def get_data(file):
    file = open(file, 'r', encoding='utf8')
    city_name = []
    nums = []

    for line in file:
        name = line.strip().split(':')
        city_name.append(name[0])
        num = line.split(':')[1].split(' ')[1].replace(',', '.')
        nums.append(float(num))

    print(city_name)
    print(nums)
    file.close()

    return city_name, nums


plt.bar(*get_data('newfile.txt'))
plt.show()