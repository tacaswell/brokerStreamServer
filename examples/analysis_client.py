__author__ = 'arkilic'


from broker import config as cfg
import numpy as np

from broker.client import read_json_from_socket


def rough_center(img, axis):
    ret = np.mean(np.argmax(img, axis=axis))
    return ret


def main():
    while True:
        # read the data from the socket
        data = read_json_from_socket(cfg.HOST, cfg.SEND_PORT)
        for d in data:
            if 'img' in d:
                img = d['img']
                print("center: ({}, {})".format(
                    rough_center(img, axis=0),
                    rough_center(img, axis=1)))


if __name__ == '__main__':
    main()
