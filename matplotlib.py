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

def plot_dots(names, global_dots):
    for i, dots in enumerate(global_dots):
        x = dots[::2]
        y = dots[1::2]
        plt.scatter(x, y, label=names[i])

    plt.plot(x, y)
    plt.title("График точек")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.show()


names, dots = get_data('newfile.txt')
plot_dots(names, dots)
