import random
def search_tracks(sp, gpt_response, limit=10):
    artist_lines = []

    # Extracts artist names from GPT output
    for line in gpt_response.splitlines():
        line = line.strip()
        if line.startswith("-") or any(line.startswith(f"{n}.") for n in range(1, 10)):
            artist_lines.append(line)

    queries = []
    for line in artist_lines:
        if "-" in line:
            name = line.split("-")[0].strip(" -1234567890.").strip()
        else:
            name = line.strip(" -1234567890.").strip()
        if name:
            queries.append(name)

    track_uris = []

    for query in queries:
        print(f"🔍 Searching Spotify for artist: {query}")
        result = sp.search(q=f'artist:{query}', type='artist', limit=1)

        if result["artists"]["items"]:
            artist_id = result["artists"]["items"][0]["id"]
            # Gets top tracks by that artist
            top_tracks = sp.artist_top_tracks(artist_id)
            for track in top_tracks["tracks"][:2]:  # Get 2 top tracks per artist
                track_uris.append(track["uri"])
        else:
            print(f"⚠️ Artist not found, searching for track: {query}")
            result = sp.search(q=query, type='track', limit=1)
            for item in result["tracks"]["items"]:
                track_uris.append(item["uri"])

    if not track_uris:
        print("⚠️ No tracks found from GPT suggestions.")
        return []

    random.shuffle(track_uris)

    return track_uris[:limit]

def create_playlist(sp, user_id, name, description="Generated with AI"):
    # Create a new playlist
    playlist = sp.user_playlist_create(user=user_id, name=name, public=True, description=description)
    return playlist["id"]


def add_tracks(sp, playlist_id, track_uris):
    # Add the list of songs to the playlist
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
