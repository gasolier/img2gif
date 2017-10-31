import imageio
import os


def create_gif(target):
    os.chdir(target)
    image_list = []

    for file in os.listdir(os.curdir):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_list.append(file)

    image_list = sorted(image_list, key=lambda x: int(x[:-4]))

    with imageio.get_writer('output.gif', mode="I") as writer:
        for image_ in image_list:
            image = imageio.imread(image_)
            writer.append_data(image)
