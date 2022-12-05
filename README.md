# lyric-generator

This software project generates a graph of lyrics provided by the user to generate a random text predicted song.

Files Included: 

  - Song text files
      These files are text files of lyrics that I used to test the program, including lyrics from Eminem and the Strokes.
  - Python program files
      song.py
        -> creates stats for the main program including verse length, song length, words per line, etc.
      graph.py
        -> a file containing a graph class, a vertex class, and a population function for creating a Markov chain graph of words used in the lyrics.
      scraper.py
        -> uses BeautifulSoup to scrape the lyrics off lyricsfreak.com 
      song_gen_scraper.py
        -> this version of the song generator scrapes the lyrics off lyricsfreak.com and runs through the program to generate a song.
      song_generator.py
        -> this version of the song generator uses a command line interface to get direct text files from the user to use in generating the song.
        
Notes:

  - The web scraper version is still a little buggy. There is a problem in scraping the lyrics and putting them in a text file for the generator.
  - There is still a small bug in quitting the command line interface in some cases in the song_generator.py version.
