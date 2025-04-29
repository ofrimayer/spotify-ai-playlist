// Handles communication with the Flask backend

// Sends a POST request to the backend with the user-provided prompt
export async function createPlaylist(prompt) {
    const response = await fetch('http://127.0.0.1:5000/create_playlist', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt }), // Turns { prompt: "some text" } into JSON
    });
  
    // If the response is not OK (200 range), throw an error
    if (!response.ok) {
      throw new Error('Failed to create playlist');
    }
  
    const data = await response.json();
    return data;
  }
  