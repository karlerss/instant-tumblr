import multiprocessing

from video import Video
import random
import re
import pysrt

def main(a):
    srt = pysrt.open('tmp/sub.srt')
    for i in range(0, 10):
        text = random.choice(srt).text
        path = 'F:\Filmid\[ www.CpasBien.cm ] Zootopia.2016.MULTi.1080p.BluRay.x264-VENUE.mkv'
        video = Video(text, path, a)
        video.start()
        print i


if __name__ == '__main__':
    pool = multiprocessing.Pool(8)
    offset = 10
    out1, out2, out3 = zip(*pool.map(main, range(0, 10 * offset, offset)))
