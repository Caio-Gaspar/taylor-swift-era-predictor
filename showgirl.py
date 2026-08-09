import pandas as pd

SHOWGIRL_ALBUM_ID = "showgirl_2025_id"
TAYLOR_ARTIST_ID = "06HL4z0CvFAxyA2316fA3w"

showgirl_tracks = [
    {
        "track_name": "The Fate of Ophelia", "track_id": "sg_tr_01", "duration_ms": 226000, "explicit": False, "track_number": 1,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.68, "energy": 0.75, "loudness": -5.2, "speechiness": 0.04, "acousticness": 0.15, "instrumentalness": 0.0, "liveness": 0.12, "valence": 0.62
    },
    {
        "track_name": "Elizabeth Taylor", "track_id": "sg_tr_02", "duration_ms": 208000, "explicit": False, "track_number": 2,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.62, "energy": 0.68, "loudness": -6.1, "speechiness": 0.05, "acousticness": 0.22, "instrumentalness": 0.0, "liveness": 0.10, "valence": 0.55
    },
    {
        "track_name": "Opalite", "track_id": "sg_tr_03", "duration_ms": 235000, "explicit": False, "track_number": 3,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.72, "energy": 0.80, "loudness": -4.8, "speechiness": 0.06, "acousticness": 0.10, "instrumentalness": 0.0, "liveness": 0.15, "valence": 0.78
    },
    {
        "track_name": "Father Figure", "track_id": "sg_tr_04", "duration_ms": 212000, "explicit": True, "track_number": 4,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.50, "energy": 0.45, "loudness": -8.5, "speechiness": 0.03, "acousticness": 0.60, "instrumentalness": 0.0, "liveness": 0.09, "valence": 0.38
    },
    {
        "track_name": "Eldest Daughter", "track_id": "sg_tr_05", "duration_ms": 246000, "explicit": False, "track_number": 5,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.48, "energy": 0.42, "loudness": -9.0, "speechiness": 0.03, "acousticness": 0.65, "instrumentalness": 0.0, "liveness": 0.11, "valence": 0.35
    },
    {
        "track_name": "Ruin the Friendship", "track_id": "sg_tr_06", "duration_ms": 220000, "explicit": False, "track_number": 6,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.70, "energy": 0.72, "loudness": -5.5, "speechiness": 0.05, "acousticness": 0.18, "instrumentalness": 0.0, "liveness": 0.14, "valence": 0.65
    },
    {
        "track_name": "Actually Romantic", "track_id": "sg_tr_07", "duration_ms": 163000, "explicit": False, "track_number": 7,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.52, "energy": 0.48, "loudness": -8.0, "speechiness": 0.04, "acousticness": 0.58, "instrumentalness": 0.0, "liveness": 0.08, "valence": 0.45
    },
    {
        "track_name": "Wish List", "track_id": "sg_tr_08", "duration_ms": 207000, "explicit": False, "track_number": 8,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.65, "energy": 0.62, "loudness": -6.8, "speechiness": 0.04, "acousticness": 0.30, "instrumentalness": 0.0, "liveness": 0.10, "valence": 0.58
    },
    {
        "track_name": "Wood", "track_id": "sg_tr_09", "duration_ms": 150000, "explicit": True, "track_number": 9,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.78, "energy": 0.85, "loudness": -4.2, "speechiness": 0.07, "acousticness": 0.08, "instrumentalness": 0.0, "liveness": 0.18, "valence": 0.82
    },
    {
        "track_name": "Cancelled!", "track_id": "sg_tr_10", "duration_ms": 211000, "explicit": True, "track_number": 10,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.66, "energy": 0.70, "loudness": -5.8, "speechiness": 0.06, "acousticness": 0.20, "instrumentalness": 0.0, "liveness": 0.13, "valence": 0.52
    },
    {
        "track_name": "Honey", "track_id": "sg_tr_11", "duration_ms": 181000, "explicit": False, "track_number": 11,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.58, "energy": 0.50, "loudness": -7.5, "speechiness": 0.03, "acousticness": 0.45, "instrumentalness": 0.0, "liveness": 0.09, "valence": 0.60
    },
    {
        "track_name": "The Life of a Showgirl (feat. Sabrina Carpenter)", "track_id": "sg_tr_12", "duration_ms": 241000, "explicit": False, "track_number": 12,
        "album_id": SHOWGIRL_ALBUM_ID, "album_name": "The Life of a Showgirl", "album_release_date": "2025-10-03", "album_total_tracks": 12, "album_type": "album",
        "artist_name": "Taylor Swift", "artist_id": TAYLOR_ARTIST_ID,
        "danceability": 0.64, "energy": 0.66, "loudness": -6.0, "speechiness": 0.05, "acousticness": 0.25, "instrumentalness": 0.0, "liveness": 0.12, "valence": 0.60
    }
]


df_showgirl = pd.DataFrame(showgirl_tracks)
df_showgirl.to_csv('showgirl.csv', index=False)

print("✨ Arquivo 'showgirl.csv' gerado com sucesso!")