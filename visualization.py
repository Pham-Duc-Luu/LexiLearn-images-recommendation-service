import os
from IPython.display import display, Image, HTML


def display_result(list_scores, img_dir_path="./datasets/flickr8k/Images"):
    for img, score in list_scores:
        img_path = os.path.join(img_dir_path, img)
        try:
            display(Image(filename=img_path))
            display(HTML(f"<p style='text-align: center; font-size: 16px;'>{img}</p>"))
        except:
            print("Words or relating images not existing!")
            continue
