import os

import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def display_result(list_scores, img_dir_path="./datasets/flickr8k/Images"):
    """
        Display the images in Pycharm backend
    :param list_scores: list of (image path, score) tuple
    :param img_dir_path: the path to the image directory
    :return:
    """
    for img, score in list_scores:
        img_path = os.path.join(img_dir_path, img)
        try:
            img = mpimg.imread(img_path)
            plt.imshow(img)
            plt.show()
        except FileNotFoundError:
            print("Words or relating images not existing!")
            continue
