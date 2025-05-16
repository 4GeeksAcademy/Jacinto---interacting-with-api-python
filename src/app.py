import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#Autenticacion de Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)




##https://open.spotify.com/intl-es/artist/1WWezGDnjvHxS6DjIq9GjT

artist_id = "1WWezGDnjvHxS6DjIq9GjT"


# Seleccion de canciones mas populares
top_tracks = spotify.artist_top_tracks(artist_id)["tracks"]
track_data = [
    {
        "name": track["name"],
        "popularity": track["popularity"],
        "duration_min": track["duration_ms"] / 60000  # Convertir de ms a minutos
    }
    for track in top_tracks
]

# Convertir a DF
df = pd.DataFrame(track_data)

# Ordenar por popularidad y mostrar el top 10
df_sorted = df.sort_values(by="popularity", ascending=True).head(3)
print(df_sorted)

# Analizar relación entre duración y popularidad
sns.scatterplot(data=df, x="duration_min", y="popularity")
plt.xlabel("Duración (min)")
plt.ylabel("Popularidad")
plt.title("Relación entre duración y popularidad")
plt.show()
