import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = '/Users/pouniq/RadioHead_recom/data/lyrics/Radiohead/saved_album_lyrics_radiohead_amnesiac.json'




    
tracks = data['tracks'][0]['song']['lyrics']







df_msp = pd.DataFrame(rows)




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

df_total_rh.to_csv('rh_df.csv')



# The Smile

df_lfaa = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/The Smile/saved_album_lyrics_the_smile_a_light_for_attracting_attention.json')
df_c = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/The Smile/saved_album_lyrics_the_smile_cutouts.json')
df_swoe = make_df('/Users/pouniq/RadioHead_recom/data/lyrics/The Smile/saved_album_lyrics_the_smile_wall_of_eyes.json')

df_total_ts = pd.concat([df_lfaa, df_c, df_swoe], axis=0).reset_index(drop=True)

