# 🎶 AI-Powered Spotify Playlist Generator

Automatically create custom Spotify playlists from natural language prompts, powered by GPT-3.5 and the Spotify API.

## Overview
This project combines OpenAI's GPT capabilities with Spotify's Web API to build personalized playlists based on user input. A Flask backend handles API calls and playlist generation, while a React frontend provides an easy-to-use web interface.

## Features
- Input a vibe, character, or theme and generate a playlist.
- GPT suggests artists and genres based on known references.
- Spotify search API retrieves real tracks matching suggestions.
- Playlists are automatically created in the user's Spotify account.
- Full-stack architecture with separate backend and frontend services.


## 💻 Tech Stack

| Layer        | Technology |
|--------------|------------|
| AI Engine    | OpenAI GPT-3.5 |
| Backend      | Python, Flask, Spotipy |
| Frontend     | React |
| Auth         | OAuth2 (Spotify) |
| Config       | `.env` via `python-dotenv` |

## ⚙️ Setup Instructions

### Backend Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/spotify-ai-playlist.git
cd spotify-ai-playlist
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Create a `.env` file in the project root with:
```python
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
OPENAI_API_KEY=your_openai_key
```

5. Run the Flask server:
```bash
python python app_backend.py
```

The backend will be available at: `http://127.0.0.1:5000`


6. Once the backend is running locally, you can test it using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/create_playlist \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Lorelai Gilmore"}'
```
This will return a JSON object with a playlist_url linking directly to the created Spotify playlist.

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

The frontend will be available at: `http://localhost:3000`


### Development Notes
- `requirements.txt` was generated using [`pipreqs`](https://github.com/bndr/pipreqs) to only include libraries actually imported in the code.
- To regenerate requirements after code changes:

```bash
pip install pipreqs
pipreqs . --force
```

## ✍🏻 To-Do
- UI improvements
- Deployment
- Other: Advanced