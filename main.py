from spotify_auth import get_spotify_client
from gpt_service import analyze_prompt
from spotify_utils import create_playlist, add_tracks, search_tracks

# Connects to Spotify (authenticates user)
sp = get_spotify_client()
user_id = sp.current_user()["id"]

# Asks user for a playlist idea
prompt = input("What's the vibe of your playlist? ")

# Analyzes the prompt
suggestions = analyze_prompt(prompt)
print(f"\n🧠 GPT Suggests:\n{suggestions}\n")

# Searches Spotify for tracks matching those suggestions
track_uris = search_tracks(sp, suggestions, limit=30)

# Checks if tracks found
if not track_uris:
    print("❌ No songs found from the GPT suggestions. Try a more detailed or different prompt.")
else:
    # Create playlist
    playlist_id = create_playlist(sp, user_id, f"AI Playlist: {prompt}")
    add_tracks(sp, playlist_id, track_uris)
    print(f"\n🎵 Playlist created: https://open.spotify.com/playlist/{playlist_id}")