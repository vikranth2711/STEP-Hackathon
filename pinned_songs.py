import random
from playlist_engine import PlaylistEngine

# Pinned Songs for fixing songs at specific indices during shuffles
class PinnedSongs:
    def __init__(self, playlist_engine):
        """
        Initialize the pinned songs module.
        Args:
            playlist_engine: Instance of PlaylistEngine
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.playlist_engine = playlist_engine
        self.pinned_indices = {}  # HashMap: song_id -> pinned index
        self.index_to_song_id = {}  # HashMap: index -> song_id for pinned positions

    def pin_song(self, song_id, title, index):
        """
        Pin a song to a specific index in the playlist.
        Args:
            song_id (str): Unique identifier for the song
            title (str): Song title (for lookup in PlaylistEngine)
            index (int): Desired index for pinning
        Raises:
            IndexError: If index is invalid
            ValueError: If song_id is already pinned or index is occupied
        Time Complexity: O(n) due to move_song and traversal
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.playlist_engine.size:
            raise IndexError("Invalid index")
        if song_id in self.pinned_indices:
            raise ValueError("Song is already pinned")
        if index in self.index_to_song_id:
            raise ValueError("Index is already pinned")

        # Find the song in the playlist
        current = self.playlist_engine.head
        current_index = 0
        found = False
        while current:
            if current.title == title:
                found = True
                break
            current = current.next if not self.playlist_engine.reversed else current.prev
            current_index += 1

        if not found:
            raise ValueError("Song not found in playlist")

        # Move song to the desired index
        self.playlist_engine.move_song(current_index, index)
        self.pinned_indices[song_id] = index
        self.index_to_song_id[index] = song_id

    def unpin_song(self, song_id):
        """
        Unpin a song, allowing it to be shuffled.
        Args:
            song_id (str): Unique identifier of the song
        Returns:
            bool: True if unpinned, False if song_id not pinned
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if song_id not in self.pinned_indices:
            return False
        index = self.pinned_indices[song_id]
        del self.pinned_indices[song_id]
        del self.index_to_song_id[index]
        return True

    def shuffle_playlist(self):
        """
        Shuffle the playlist, keeping pinned songs at their fixed positions.
        Time Complexity: O(n) for Fisher-Yates shuffle
        Space Complexity: O(n) for temporary array
        Note: Uses Fisher-Yates shuffle for unbiased randomization of non-pinned songs
        """
        # Extract songs, respecting reversed state
        songs = []
        current = self.playlist_engine.head
        index = 0
        while current:
            songs.append({
                "title": current.title,
                "artist": current.artist,
                "duration": current.duration,
                "index": index
            })
            current = current.next if not self.playlist_engine.reversed else current.prev
            index += 1

        # Create list of available indices (excluding pinned ones)
        available_indices = [i for i in range(len(songs)) if i not in self.index_to_song_id]

        # Fisher-Yates shuffle for non-pinned songs
        non_pinned_songs = [song for song in songs if song["index"] not in self.index_to_song_id]
        for i in range(len(non_pinned_songs) - 1, 0, -1):
            j = random.randint(0, i)
            non_pinned_songs[i], non_pinned_songs[j] = non_pinned_songs[j], non_pinned_songs[i]

        # Reconstruct playlist with pinned songs in place
        result = [None] * len(songs)
        for idx in self.index_to_song_id:
            for song in songs:
                if song["index"] == idx:
                    result[idx] = song
                    break

        non_pinned_idx = 0
        for i in range(len(songs)):
            if i not in self.index_to_song_id:
                result[i] = non_pinned_songs[non_pinned_idx]
                non_pinned_idx += 1

        # Rebuild playlist
        self.playlist_engine.head = None
        self.playlist_engine.tail = None
        self.playlist_engine.size = 0
        for song in result:
            self.playlist_engine.add_song(song["title"], song["artist"], song["duration"])