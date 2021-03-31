import random
import sys
import codecs

t = int(input().strip())

for tc in range(t):
    songs = input().strip().split('\t')
    artists = input().strip().split('\t')

    pl_dict = dict()
    for i, a in enumerate(artists):
        if a not in pl_dict:
            pl_dict[a] = []
        pl_dict[a].append([songs[i], 0])

    for art_songs in pl_dict.values():
        song_cnt = len(art_songs)
        if song_cnt == 1:
            art_songs[0][1] = random.random()
        else:
            ratio = 1 / (song_cnt + 1)
            random.shuffle(art_songs)
            for i, s in enumerate(art_songs):
                art_songs[i][1] = ratio * (i + 1) + random.uniform(-ratio / 4, ratio / 4)

    pl = [s for art_songs in pl_dict.values() for s in art_songs]
    pl_str = ''
    pl = sorted(pl, key=lambda s: s[1])
    for s in pl:
        pl_str += '\t' + s[0]
    pl_str = pl_str.strip()
    print(pl_str)
