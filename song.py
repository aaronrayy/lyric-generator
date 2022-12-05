import math
class Song:
    def __init__(self):
        self.lines = 0
        self.words = 0
        self.num_verses = 1
        self.avg_verse_len = 0
        self.file = ""
    def song_stats(self, f_in):
        f = open(f_in, 'r') 
        for line in f:
            self.lines += 1
            l = line.split()
            self.words += len(l)
            if len(l) <= 1:
                self.num_verses += 1
        self.avg_verse_len = math.ceil(self.lines/self.num_verses)

class Stats:
    def __init__(self):
        self.num_songs = 0
        self.tot_lines = 0
        self.tot_words = 0
        self.avg_lines = 0 
        self.avg_words_line = 0
        self.tot_verse_lines = 0
        self.avg_verse_len = 0
        self.songs = []
    def total_stats(self):
        for s in self.songs:
            self.num_songs += 1
            self.tot_lines += s.lines
            self.tot_words += s.words
            self.tot_verse_lines += s.avg_verse_len
        if self.num_songs > 0:
            self.avg_lines = self.tot_lines / self.num_songs
            self.avg_verse_len = self.tot_verse_lines / self.num_songs
        if self.tot_lines > 0:
            self.avg_words_line = self.tot_words / self.tot_lines
    def full_printout(self):
        s = "Total stats:\n   num_songs: " + str(self.num_songs) + "\n   tot_lines: " + str(self.tot_lines) + "\n   tot_words: " + str(self.tot_words) + "\n   avg_lines: " + str(self.avg_lines) + "\n   avg_words_line: " + str(self.avg_words_line)
        return s