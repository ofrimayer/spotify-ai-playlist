def search_tracks(sp, gpt_response, limit=10):
    artist_lines = []

    # Parse GPT response, extract artist names
    for line in gpt_response.splitlines():
        line = line.strip()
        if line.startswith("-"):
            artist_lines.append(line)
        elif any(line.startswith(f"{n}.") for n in range(1, 10)):
            artist_lines.append(line)

    queries = []
    for line in artist_lines:
        # Clean and extract just artist names
        if "-" in line:
            name = line.split("-")[0].strip(" -1234567890.").strip()
        else:
            name = line.strip(" -1234567890.").strip()
        if name:
            queries.append(name)

    track_uris = []

    for query in queries:
        print(f"🔍 Searching Spotify for: {query}")
        results = sp.search(q=query, limit=1)
        for item in results["tracks"]["items"]:
            track_uris.append(item["uri"])

    if not track_uris:
        print("⚠️ No tracks found from the GPT suggestions.")

    return track_uris


def create_playlist(sp, user_id, name, description="Generated with AI"):
    # Create a new playlist
    playlist = sp.user_playlist_create(user=user_id, name=name, public=True, description=description)
    return playlist["id"]


def add_tracks(sp, playlist_id, track_uris):
    # Add the list of songs to the playlist
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
