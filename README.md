# 🎶 AI-Powered Spotify Playlist Generator

This project automatically creates a Spotify playlist based on a natural language prompt.

It uses:
- OpenAI (GPT-3.5) to suggest artists and genres
- Spotify Web API (Spotipy) to search and create playlists
- Python for orchestration

## 🚀 Features

- Input a vibe or character and get a matching playlist.
- GPT suggests artists and genres based on canon references.
- Searches Spotify for real songs and assembles a playlist.
- Playlist is automatically created on the user's Spotify account.
- Flask backend to handle AI, Spotify API calls.
- Future: Frontend in React


## 💻 Technologies Used

- **Flask** backend (`app_backend.py`)
- **OpenAI API** for GPT prompts (`gpt_service.py`)
- **Spotify API** for search, playlist creation (`spotify_utils.py`, `spotify_auth.py`)
- `.env` file to store your OpenAI and Spotify credentials.


## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/spotify-ai-playlist.git
cd spotify-ai-playlist
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with:
```python
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
OPENAI_API_KEY=your_openai_key
```

4. Run the backend:
```bash
python python app_backend.py
```

5. Make a POST request to http://127.0.0.1:5000/create_playlist with JSON body:
```json
{
  "prompt": "Lorelai Gilmore"
}
```

6. It returns a Spotify playlist link!


## 🔨 Development Notes
- `requirements.txt` was generated using [`pipreqs`](https://github.com/bndr/pipreqs) to only include libraries actually imported in the code.
- To regenerate requirements after code changes:

```bash
pip install pipreqs
pipreqs . --force
```

## ✍🏻 To-Do
- Frontend
- Production deployment (backend + frontend)
- Other: Advanced