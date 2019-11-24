from scipy.ndimage import label


def is_atomic(image):
    PERCENT = 0.5
    MIN_GRAY = 0.6

    useless_pixels = (image <= 0.2).sum()
    binary = image > MIN_GRAY
    percent = (binary.sum()) / (binary.size - useless_pixels)
    return percent


def is_background(image):
    PERCENT = 0.85
    MAX_GRAY = 0.2

    useless_pixels = (image == 0).sum()
    binary = image <= MAX_GRAY
    percent = (binary.sum() - useless_pixels) / (binary.size - useless_pixels)
    return percent >= PERCENT


def label_peak_amount(image):
    MIN_GRAY = 0.52
    MIN_SIZE = 35

    binary = image > MIN_GRAY
    result, amount = label(binary)

    for i in range(1, amount+1):
        label_only = result == i
        if label_only.sum() > MIN_SIZE:
            continue

        result[label_only == 1] = 0

    return result, amount
