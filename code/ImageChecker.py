from scipy.ndimage import label


def is_atomic(image):
    PERCENT = 0.5
    MIN_GRAY = 0.3

    binary = image > MIN_GRAY
    percent = binary.sum() / (binary.size - (image == 0).sum())
    return percent


def label_peak_list(image_list):
    MIN_GRAY = 90

    binary_list = [image > MIN_GRAY for image in image_list]
    result = [label(binary)[0] for binary in binary_list]

    return result
