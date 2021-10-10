import numpy as np


def start():
    print('hello')
    x_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y_train = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(x_train)
    print(y_train)

    w0 = np.random.normal()
    w1 = np.random.normal()
    err = 1
    print(w0, w1, err)


def h(w0, w1, x):
    return w0 + w1 * x


if __name__ == '__main__':
    start()
