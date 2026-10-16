import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer

import spacy


# create function to handle each album dataset
def make_df(path):
    with open(path, 'r') as f:
        data = json.load(f)
    
    rows = [
    {
        'album': data['name'],
        'date_year': data['release_date_components']['year'],
        'title': t['song']['title'] if 'title' in t['song'] else t['song']['full_title'],
        'lyrics': t['song']['lyrics'],
    }
    
    for t in data['tracks']]
    
    df = pd.DataFrame(rows)

    return df



# Radiohead

df_amn = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_amnesiac.json')
df_msp = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_a_moon_shaped_pool.json')
df_httt = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_hail_to_the_thief.json')
df_ir = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_in_rainbows.json')
df_ka = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_kid_a.json')
df_oc = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_ok_computer.json')
df_ph = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_pablo_honey.json')
df_tb = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_the_bends.json')
df_kol = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_the_king_of_limbs.json')

df_total_rh = pd.concat([df_msp,df_amn,df_httt,df_ir,df_ka,df_tb,df_oc,df_kol,df_ph], axis=0).reset_index(drop=True)

df_total_rh.to_csv('rh_df.csv', index=False)



# The Smile

df_lfaa = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/The Smile/saved_album_lyrics_the_smile_a_light_for_attracting_attention.json')
df_c = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/The Smile/saved_album_lyrics_the_smile_cutouts.json')
df_swoe = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/The Smile/saved_album_lyrics_the_smile_wall_of_eyes.json')

df_total_ts = pd.concat([df_lfaa, df_c, df_swoe], axis=0).reset_index(drop=True)
df_total_ts.to_csv('ts_df.csv')


## Clean lyrics


### Radiohead

df_total_rh = pd.read_csv('data/lyrics/processed/raw/rh_df.csv')

##### delete spaces represnted as \n
##### lowercase the lyrics
##### delete stop words
##### delete punctuations
##### stem the lyrics

# python -m spacy download en_core_web_sm



df_total_rh[df_total_rh['lyrics'].isnull()]
# we have 3 instrumental songs in our dataset 
# 1. Hunting Bears, 2. Treefingers, 3.Untitled (from Kid A)
df_total_rh = df_total_rh.dropna(subset=['lyrics']).reset_index(drop=True)


df_total_rh['clean_lyrics'] = df_total_rh.lyrics.str.lower()
df_total_rh['clean_lyrics'] = df_total_rh.clean_lyrics.str.replace('\n',' ')

df_total_rh.to_csv('clean_rh.csv', index=False)




### The Smile

df_total_ts = pd.read_csv('data/lyrics/processed/ts_df.csv')


df_total_ts['lyrics_clean'] = df_total_ts['lyrics'].apply(clean_lyrics) 
df_total_ts.to_csv('clean_ts.csv', index=False)


