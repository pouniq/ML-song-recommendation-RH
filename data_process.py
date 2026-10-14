import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = 'data/lyrics/Radiohead/saved_album_lyrics_radiohead_a_moon_shaped_pool.json'

with open(path, 'r') as f:
    data = json.load(f)
    
lyrics = data['lyrics']