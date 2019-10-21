import matplotlib.pyplot as plot
from skimage.color import rgb2gray


def visualize(what, label='', cmap='viridis'):
    plot.figure(figsize=(8,8))
    plot.imshow(what, cmap=cmap)
    plot.title(label)
    plot.show()


def image_to_grayscale(image):
    result = rgb2gray(image)
    result *= (255.0 / result.max())  # rescale

    return result
