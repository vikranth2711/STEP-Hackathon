from playlist_engine import PlaylistEngine

# Playback History using a stack to track recently played songs
class PlaybackHistory:
    def __init__(self, playlist_engine):
        """
        Initialize the playback history stack.
        Args:
            playlist_engine: Instance of PlaylistEngine to interact with the playlist
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.history = []  # Stack to store recently played songs
        self.playlist_engine = playlist_engine  # Reference to the playlist engine

    def add_played_song(self, title, artist, duration):
        """
        Push a played song onto the history stack.
        Args:
            title (str): Song title
            artist (str): Song artist
            duration (int): Song duration in seconds
        Time Complexity: O(1)
        Space Complexity: O(1) per song
        """
        self.history.append({"title": title, "artist": artist, "duration": duration})

    def undo_last_play(self):
        """
        Pop the last played song and re-add it to the playlist.
        Returns:
            dict: The song that was re-added, or None if history is empty
        Time Complexity: O(1) for pop, O(1) for adding to playlist
        Space Complexity: O(1)
        """
        if not self.history:
            return None
        last_song = self.history.pop()
        self.playlist_engine.add_song(last_song["title"], last_song["artist"], last_song["duration"])
        return last_song

    def get_history(self):
        """
        Return a copy of the current playback history.
        Returns:
            list: List of song dictionaries in the history stack
        Time Complexity: O(n) to copy the list
        Space Complexity: O(n) for the returned list
        """
        return self.history.copy()