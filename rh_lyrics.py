import lyricsgenius

token = 'f3jFiQg1hEOdqx4nbJ7qBwW8mzHJf8RJ9NdQYNvQXPgTEs0SR57_ibvtCxxQxmVj'
genius = lyricsgenius.Genius(token)

genius = lyricsgenius.Genius(
    token,
    timeout=15,
    retries=3,
    sleep_time=1,                 # pause between requests to avoid rate limits
    remove_section_headers=True,  # drops [Verse 1], [Chorus], etc.
    skip_non_songs=True,          # skips tracklists, booklets, etc.
    excluded_terms=["(Remix)", "(Live)", "(Demo)", "(Acoustic)", "Live at", "- Live", "Demo", "Remix"]
)


album = genius.search_album("Cutouts", "the smile")
album.save_lyrics()
