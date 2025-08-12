from playlist_engine import PlaylistEngine

# Song Lookup using HashMap for O(1) access by song_id or title
class SongLookup:
    def __init__(self, playlist_engine):
        """
        Initialize the song lookup HashMap.
        Args:
            playlist_engine: Instance of PlaylistEngine to sync with
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.song_id_map = {}       # HashMap: song_id -> metadata
        self.title_to_id = {}       # HashMap: title -> list of song_ids
        self.playlist_engine = playlist_engine

    def add_song(self, song_id, title, artist, duration):
        """
        Add or update a song in the HashMap.
        Args:
            song_id (str): Unique identifier for the song
            title (str): Song title
            artist (str): Song artist
            duration (int): Song duration in seconds
        Time Complexity: O(1) average case
        Space Complexity: O(1) per song
        """
        song_data = {"song_id": song_id, "title": title, "artist": artist, "duration": duration}
        self.song_id_map[song_id] = song_data
        if title not in self.title_to_id:
            self.title_to_id[title] = []
        self.title_to_id[title].append(song_id)

    def delete_song(self, song_id):
        """
        Delete a song from the HashMap by song_id.
        Args:
            song_id (str): Unique identifier of the song
        Returns:
            bool: True if deletion was successful, False if song_id not found
        Time Complexity: O(1) average case
        Space Complexity: O(1)
        """
        if song_id not in self.song_id_map:
            return False
        song_data = self.song_id_map[song_id]
        title = song_data["title"]
        self.title_to_id[title].remove(song_id)
        if not self.title_to_id[title]:
            del self.title_to_id[title]
        del self.song_id_map[song_id]
        return True

    def lookup_by_id(self, song_id):
        """
        Retrieve song metadata by song_id.
        Args:
            song_id (str): Unique identifier of the song
        Returns:
            dict: Song metadata, or None if not found
        Time Complexity: O(1) average case
        Space Complexity: O(1)
        """
        return self.song_id_map.get(song_id)

    def lookup_by_title(self, title):
        """
        Retrieve song metadata by song title.
        Args:
            title (str): Song title
        Returns:
            list: List of song metadata dictionaries for the title
        Time Complexity: O(1) average case
        Space Complexity: O(1) excluding output
        Note: Returns a list to handle non-unique titles
        """
        song_ids = self.title_to_id.get(title, [])
        return [self.song_id_map[sid] for sid in song_ids]

    def sync_add(self, title, artist, duration):
        """
        Sync with PlaylistEngine by adding a song to both the playlist and HashMap.
        Args:
            title (str): Song title
            artist (str): Song artist
            duration (int): Song duration in seconds
        Returns:
            str: Generated song_id
        Time Complexity: O(1) average case
        Space Complexity: O(1)
        """
        import time
        song_id = f"{title}_{int(time.time())}"  # Simple unique ID generation
        self.add_song(song_id, title, artist, duration)
        self.playlist_engine.add_song(title, artist, duration)
        return song_id

    def sync_delete(self, song_id):
        """
        Sync with PlaylistEngine by deleting a song from both the playlist and HashMap.
        Args:
            song_id (str): Unique identifier of the song
        Returns:
            bool: True if deletion was successful, False otherwise
        Time Complexity: O(n) due to PlaylistEngine traversal
        Space Complexity: O(1)
        """
        song_data = self.lookup_by_id(song_id)
        if not song_data:
            return False
        title = song_data["title"]
        current = self.playlist_engine.head
        index = 0
        while current:
            if current.title == title:
                self.delete_song(song_id)
                self.playlist_engine.delete_song(index)
                return True
            current = current.next if not self.playlist_engine.reversed else current.prev
            index += 1
        return False