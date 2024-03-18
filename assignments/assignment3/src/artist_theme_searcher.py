import os
import sys
sys.path.append("..")
import pandas as pd
import gensim.downloader as api
import re
import argparse

parser = argparse.ArgumentParser(
                    prog='Artist Theme Searcher',
                    description='Helps you find out how much your favorite artist sings about a theme',
                    epilog='Thank you!')
parser.add_argument('theme', help="name the keyword you find central for the theme")
parser.add_argument('artist', help="name the artist you want to search for")
args = parser.parse_args()
    


def main():
    key_word = args.theme
    artist = args.artist
    #Load data and model
    inpath = os.path.join("data", "spot_mil_song_lyr.csv")
    lyrics = pd.read_csv(inpath)
    model = api.load("glove-wiki-gigaword-50")

    #Preprocess
    keys = gensim_most_similar(model, key_word) #From word-model
    artists = preprocess_artist_themes(lyrics, keys) #Preprocess dataset

    #Calculate and print
    calculate_artist(artist, artists, lyrics, key_word)
    return None


def gensim_most_similar(model, key_word):
    result = model.most_similar(positive=key_word, topn=10)
    key_words = [i[0] for i in result]
    return key_words

def preprocess_artist_themes(lyrics, keys):
    artist_list = []

    for index, row in lyrics.iterrows():
        lyr = row['text']
        lyr = re.sub(r'[^\w\s]', ' ', lyr)

        if any(ele in lyr for ele in keys): #Moving into the rows with the words https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/
            artist_list.append(row['artist'])

    return artist_list

def calculate_artist(specific_artist, artist_list, df, key_word):
    num_lov_songs = artist_list.count(specific_artist)
    tot_songs = df['artist'].value_counts()[specific_artist]
    print("The artist " + specific_artist + " sing about " + key_word + " " + str(num_lov_songs) + " out of " + str(tot_songs) + " times.")

    percentage = num_lov_songs/tot_songs*100
    return percentage

if __name__ == "__main__":
    main()