# Flask backend server with two endpoints (/analyze, /create_playlist)
from flask import Flask, request, jsonify
from spotify_auth import get_spotify_client
from spotify_utils import create_playlist, add_tracks, search_tracks
from gpt_service import analyze_prompt

# Create a new Flask app instance
app = Flask(__name__)

# Connect to Spotify when the server starts
sp = get_spotify_client()
user_id = sp.current_user()["id"]

# Define an endpoint for analyzing a prompt
@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Accepts a POST request with a JSON body containing 'prompt',
    sends it to GPT to get artist/genre suggestions, and returns the result.
    """
    data = request.get_json() # Parses the incoming JSON request
    prompt = data.get("prompt") # Extracts the prompt field from JSON
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    suggestions = analyze_prompt(prompt) # Sends prompt to GPT
    return jsonify({"suggestions": suggestions}) # Returns GPT's answer as JSON


@app.route('/create_playlist', methods=['POST'])
def create_playlist_endpoint():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    # Analyzes with GPT
    suggestions = analyze_prompt(prompt)

    # Searchs for tracks
    track_uris = search_tracks(sp, suggestions, limit=30)

    # Fallback if no tracks found
    if not track_uris:
        print("⚠️ No tracks found, falling back to indie-pop playlist")
        track_uris = fallback_tracks(sp, genres=["indie", "pop"], limit=30)

    if not track_uris:
        return jsonify({"error": "Still no tracks found"}), 400

    # Creates playlist
    playlist_id = create_playlist(sp, user_id, f"AI Playlist: {prompt}")
    
    add_tracks(sp, playlist_id, track_uris)

    return jsonify({"playlist_url": f"https://open.spotify.com/playlist/{playlist_id}"}), 200

def fallback_tracks(sp, genres=["pop"], limit=30):
    try:
        recs = sp.recommendations(seed_genres=genres[:2], limit=limit)
        return [track["uri"] for track in recs["tracks"]]
    except Exception as e:
        print(f"❌ Failed fallback: {e}")
        return []


if __name__ == "__main__":
    app.run(port=5000, debug=True)
