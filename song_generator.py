from tkinter import W
import graph
import song
import math
import random
import sys

def setup(f_in):
        if f_in == 'f':
            return 1
        try:
            open(f_in, 'r')
            song_files.append(f_in)
            cur_song = song.Song()
            cur_song.song_stats(f_in)
            stats.songs.append(cur_song)
            graph.populate(g, f_in)
            return 0
        except FileNotFoundError:
            print("  oops! not a valid file name. try again.")
            return 0

if __name__=="__main__":
    # take user input for songs, and generate stats for them in a Stats() object
    # concurrently generates a markov graph of the words in the songs
    stats = song.Stats()
    g = graph.Graph()
    song_files = []
    while True:
        f_in = input("enter a song text file, or 'f' to finish: ")
        ret = setup(f_in)
        if ret:
            break
    stats.total_stats()
    #print(stats.full_printout())

    # take user start words and generate a song for them based on 
    #   average song stats and word prediction using the graph
    start_word = input("Enter a word to start the song, or [quit] to quit: ")
    if start_word == "[[quit]]":
        sys.exit()
    while True:
        if start_word not in g.vertexes:
            start_word = input("oops! your artist has not used that word in any songs. try again: ")
        else:
            break
    max_lines = math.ceil(stats.avg_lines)
    max_words = math.ceil(stats.avg_words_line)
    max_verse = math.ceil(stats.avg_verse_len)
    cur_verse_len = 0
    mva = [max_verse, max_verse, max_verse+1, max_verse+2, max_verse+3]     # max verse length array
    mwa = [max_words, max_words, max_words+2, max_words+3, max_words+3]     # max words array
    mww = [1, 1, 1, 1, 1]                                                   # max word weights
    gen_lines = 0
    gen_words = 0
    gen_verses = 0
    out = open("generated_song.txt", 'w')   
    # steps:
    #   1. traverse the graph starting at the starting words
    #   2. randomly choose the next words based on current words adjacency list, weighted by adjacent words edge weight
    #   3. append these words to 'out' file in a line until the number of words in that line hits max_words
    #   4. keep doing this until the current number of lines equals max_lines
    #print("start:" + start_word)
    out.write(start_word + " ")
    cur = start_word
    gen_words += 1
    while True:
        # set up choices list and probability list for random.choice() method
        cur_vertex = g.vertexes[cur]
        cur_adj = cur_vertex.adj
        adj = []
        weights = []
        for v in cur_adj:
            adj.append(v.value)
            weights.append(v.weight)
        if len(adj) > 0:
            cur = random.choices(adj, weights, k=1)
        else:
            break
        out.write(cur[0] + " ")
        cur = cur[0]
        
        gen_words += 1
        if gen_words >= max_words:
            gen_words = 0
            gen_lines += 1
            cur_verse_len += 1
            out.write("\n")
            if cur_verse_len >= max_verse:
                out.write("\n")
                cur_verse_len = 0
                max_verse = random.choices(mva, mww, k=1)
                max_verse = max_verse[0]
            max_words = random.choices(mwa, mww, k=1)
            max_words = max_words[0]
        if gen_lines >= max_lines:
            break
    out.close()