# 🎶 AI-Powered Spotify Playlist Generator

This project automatically creates a Spotify playlist based on a natural language prompt.

It uses:
- OpenAI (GPT-3.5) to suggest artists and genres
- Spotify Web API (Spotipy) to search and create playlists
- Python for orchestration

## 🚀 Features

- Analyze user prompt using GPT
- Extract real artists and genres
- Search for tracks by these artists on Spotify
- Create a brand new public playlist on your account


## 💻 Technologies Used

- Python
- OpenAI GPT-3.5 (via `openai` Python package)
- Spotify Web API (via `spotipy`)
- Environment variables for secrets (`python-dotenv`)


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

4. Run the app:
```bash
python main.py
```


## 🔨 Development Notes
- `requirements.txt` was generated using [`pipreqs`](https://github.com/bndr/pipreqs) to only include libraries actually imported in the code.
- To regenerate requirements after code changes:

```bash
pip install pipreqs
pipreqs . --force
```