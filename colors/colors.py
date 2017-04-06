#!/usr/bin/python3
import sys
from PIL import Image
import pyscreenshot as ImageGrab
import scipy
import scipy.misc
import scipy.cluster
import matplotlib.colors as colors


def main(image):
    NUM_CLUSTERS = 5

    print('reading image')
    # im = Image.open(image)
    im = ImageGrab.grab()
    print('resizing image')
    im = im.resize((200, 200))
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])

    print('finding clusters')
    # features = scipy.cluster.vq.whiten(ar)
    codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)
    # codes, dist = scipy.cluster.vq.kmeans(features, NUM_CLUSTERS)
    # print('cluster centres:\n', codes)

    # assign codes
    vecs, dist = scipy.cluster.vq.vq(ar, codes)

    # count occurrences
    counts, bins = scipy.histogram(vecs, len(codes))

    # normalize between 0 and 1
    normalized_codes = codes / codes.max()
    # normalized_codes = codes

    # find most frequent
    index_max = scipy.argmax(counts)
    peak = normalized_codes[index_max]
    colour = colors.rgb2hex(peak)
    print('most frequent is {} ({})'.format(peak, colour))

    # bonus: save image using only the N most common colours
    c = ar.copy()
    # c = features.copy
    for i, code in enumerate(codes):
        c[scipy.r_[scipy.where(vecs == i)], :] = code
    scipy.misc.imsave('clusters.png', c.reshape(*shape))
    print('saved clustered image')


if __name__ == '__main__':
    main(sys.argv[1])
