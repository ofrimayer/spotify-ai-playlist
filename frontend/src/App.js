// Main React component that handles UI and displays results
import React, { useState } from 'react';
import { createPlaylist } from './api';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState(''); // State to hold the user's text input
  const [playlistUrl, setPlaylistUrl] = useState(''); // Holds the playlist URL
  const [message, setMessage] = useState(''); // State to hold a success or error message
  const [loading, setLoading] = useState(false); // loading state

  // When the user submits the form
  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setMessage('');
    try {
      const data = await createPlaylist(prompt); // Send prompt to backend and wait for response
      setPlaylistUrl(data.playlist_url); // Save the returned URL separately
    } catch (error) {
      console.error(error);
      setMessage('Failed to create playlist. Try again!');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="App">
      <h1>
        <img src="/icons8-spotify-120.png" alt="Spotify" className="spotify-img" />
        <span className="highlight">Spotify</span> AI Playlist Generator
        </h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter a vibe, character, or theme"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Generating...' : 'Generate Playlist'}
        </button>
      </form>

      {loading && <div className="spinner"></div>}

      {!loading && playlistUrl && (
        <p>
          Playlist created! Check it <a href={playlistUrl} target="_blank" rel="noopener noreferrer">here</a>.
        </p>
      )}

      {!loading && message && !playlistUrl && <p>{message}</p>}
    </div>
  );
}


export default App;
