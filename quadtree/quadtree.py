def quadtree(compressed_img):
    if compressed_img[0] != 'x':
        return compressed_img


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        compressed_img = raw_input()
        print quadtree(compressed_img)
