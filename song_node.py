# SongNode class for doubly linked list nodes in PlaylistEngine
class SongNode:
    def __init__(self, title, artist, duration):
        """
        Initialize a song node for the doubly linked list.
        Args:
            title (str): Song title
            artist (str): Song artist
            duration (int): Song duration in seconds
        """
        self.title = title
        self.artist = artist
        self.duration = duration  # Duration in seconds
        self.prev = None  # Pointer to previous node
        self.next = None  # Pointer to next node