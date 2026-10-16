import spacy
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer


df_rh = pd.read_csv('/Users/pouniq/RadioHead_recom/data/lyrics/processed/clean/clean_rh.csv')

nlp_token = spacy.load('en_core_web_sm')
doc = nlp_token(df_rh.lyrics_clean[0])




def token_lemma_is_not_stop(text):
    doc = nlp_token(text)
    output = [token.lemma_ for token in doc if not token.is_stop]
    output = ' '.join(output)
    return output


df_rh['clean_norm_lyrics'] = df_rh.clean_lyrics.apply(token_lemma_is_not_stop)


tfv = TfidfVectorizer(stop_words='english',min_df = 0.1, max_df=0.8)
tfidf = tfv.fit_transform(df_rh.clean_lyrics)

tfidf_df = pd.DataFrame(tfidf.toarray(), columns = tfv.get_feature_names_out())

from sklearn.metrics.pairwise import cosine_similarity

def top_k_similar(idx, X, titles, k=5):
    sims = cosine_similarity(X.iloc[[idx]], X).ravel()
    sims[idx] = -1                      # exclude the song itself
    top = sims.argsort()[::-1][:k]
    return [(titles[i], round(sims[i], 3)) for i in top]

# call it with the DataFrame as X

top_k_similar(74, tfidf_df, df_rh.title.tolist(), k=5)

