import matplotlib.pyplot as plt
import numpy as np


def start():
    print("start")
    x_train = np.array([1, 2, 3.3, 4.2, 4.5, 6, 7, 8, 9])
    y_train = np.array([2.1, 3, 4, 5.5, 6, 7.5, 8.1, 8.8, 10.1])
    print(x_train)
    print(y_train)

    w0 = np.random.normal()
    w1 = np.random.normal()
    print("init setting: (%f, %f)" % (w0, w1))

    count = 10000
    rate = 0.001
    for i in range(count):
        for x, y in zip(x_train, y_train):
            w0 = w0 - rate * (h(w0, w1, x) - y) * 1
            w1 = w1 - rate * (h(w0, w1, x) - y) * x
        err = 0.0
        for x, y in zip(x_train, y_train):
            err += (y - h(w0, w1, x)) ** 2
        m = len(x_train)
        err = float(err / (2 * m))
        print("%d:\t(%f, %f)\terr: %f" % (i, w0, w1, err))
        if err < 0.01:
            break

    print(w0, w1)
    draw(x_train, y_train, w0, w1)


def h(w0, w1, x):
    return w0 + w1 * x


def draw(x_train, y_train, w0, w1):
    # draw
    plt.scatter(x_train, y_train, s=10, c='blue')
    # Set chart title.
    plt.title("Linear regression")
    # Set x, y label text.
    plt.xlabel("y = %f + %fx" % (w0, w1))
    plt.ylabel("y")

    x_number_list = list(range(0, 12))
    y_number_list = [h(w0, w1, x) for x in x_number_list]
    plt.plot(x_number_list, y_number_list, linewidth=1, c='green')
    plt.axis([0, 10, 0, 15])

    plt.show()


if __name__ == '__main__':
    start()
