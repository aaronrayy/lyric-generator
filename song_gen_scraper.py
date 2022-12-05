from tkinter import W
import graph
import song
import scraper
import math
import random
import sys

# this version uses web scraping from the website lyricsfreak.com to get the lyrics

def setup_link(link_in, file_out):
        scraper.scrape(link_in, file_out)
        song_links.append(link_in)
        cur_song = song.Song()
        cur_song.song_stats(file_out)
        stats.songs.append(cur_song)
        graph.populate(g, file_out)

def setup_file(f_in):
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
            print("\n  --oops! not a valid file name. try again.\n")
            return 0

def link_input():
        link_in = input("enter a link from lyricsfreak.com for a song, or 'f' to finish: ")
        if link_in == 'f':
            return 1
        file_out = input("Enter a text file name for the song, including the .txt extension: ")
        if file_out[-4:] == ".txt":
            setup_link(link_in, file_out)
        else:
            print("\n  --oops! not a valid file name. try again--\n")
        return 0

def file_input():
        f_in = input("enter a song text file, or 'f' to finish: ")
        if f_in == 'f':
            return 1
        ret_file = setup_file(f_in)
        if ret_file:
            return 1
        return 0

if __name__=="__main__":
    # take user input for songs, and generate stats for them in a Stats() object
    # concurrently generates a markov graph of the words in the songs
    stats = song.Stats()
    g = graph.Graph()
    song_links = []
    song_files = []
    while True:
        setup_type = input("Would you like to enter a link or a text file for lyrics?\n   enter 'link' or 'file', 'f' to finish input, or 'q' to quit: ")
        if setup_type == 'f':
            break
        elif setup_type == 'q':
            sys.exit()
        elif setup_type == 'link':
            ret = link_input()
            if ret:
                break
            print("--done--".center(57))
        elif setup_type == 'file':
            ret = file_input()
            if ret:
                break
            print("--done--".center(57))
        else:
            print("\n   --not a valid input type. try again--\n")
            
    stats.total_stats()
    #print(stats.full_printout())

    # take user start words and generate a song for them based on 
    #   average song stats and word prediction using the graph
    start_word = input("Enter a word to start the song, or [q] to exit: ")
    if start_word == "[q]":
        sys.exit()
    while True:
        if start_word not in g.vertexes:
            start_word = input("\n --oops! your artist has not used that word in any songs.--\n\ntry again, or type [q] to exit: ")
            if start_word == "[q]":
                sys.exit()
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