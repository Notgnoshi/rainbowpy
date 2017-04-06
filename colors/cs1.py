#!/usr/bin/python3
from PIL import Image
import pyscreenshot as ImageGrab
from matplotlib.colors import rgb2hex
import scipy
import scipy.cluster
import scipy.misc
from pprint import pprint
import sys


def main(img):
    image = Image.open(img)
    # image = ImageGrab.grab()
    image = image.resize((200, 200))
    NUM_CLUSTERS = 5

    # Convert image into array of values for each point.
    ar = scipy.misc.fromimage(image)

    # Reshape array of values to merge color bands.
    ar = ar.reshape(scipy.product(ar.shape[:2]), ar.shape[2])

    # Get NUM_CLUSTERS worth of centroids.
    codes, _ = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)

    # Pare centroids, removing blacks and whites and shades of really dark and really light.
    original_codes = codes
    for low, hi in [(60, 200), (35, 230), (10, 250)]:
        codes = scipy.array([code for code in codes
                             if not ((code[0] < low and code[1] < low and code[2] < low) or
                                     (code[0] > hi and code[1] > hi and code[2] > hi))])
        if not len(codes):
            codes = original_codes
        else:
            break

    # Assign codes (vector quantization). Each vector is compared to the centroids
    # and assigned the nearest one.
    vecs, _ = scipy.cluster.vq.vq(ar, codes)

    # Count occurences of each clustered vector.
    counts, bins = scipy.histogram(vecs, len(codes))
    normalized_codes = codes / codes.max()

    # Show colors for each code in its hex value.
    colors = [rgb2hex(c) for c in normalized_codes]
    total = float(scipy.sum(counts))
    # top N colors as a proportion of the image
    color_dist = dict(zip(colors, (count / total for count in counts)))
    pprint(color_dist)

    # Find the most frequent color, based on the counts.
    # TODO: no need to use scipy for this.
    index_max = scipy.argmax(counts)
    peak = normalized_codes[index_max]
    color = rgb2hex(peak)
    print(color)


if __name__ == '__main__':
    main(sys.argv[1])
