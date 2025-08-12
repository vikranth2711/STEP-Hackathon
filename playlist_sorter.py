from playlist_engine import PlaylistEngine

# Playlist Sorter using Merge Sort for stable sorting
class PlaylistSorter:
    def __init__(self, playlist_engine):
        """
        Initialize the playlist sorter.
        Args:
            playlist_engine: Instance of PlaylistEngine to sort
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.playlist_engine = playlist_engine

    def merge_sort(self, songs, key, reverse=False):
        """
        Sort a list of songs using Merge Sort based on the specified key.
        Args:
            songs (list): List of song dictionaries
            key (str): Sorting criterion ('title', 'duration', 'added_order')
            reverse (bool): If True, sort in descending order
        Returns:
            list: Sorted list of song dictionaries
        Time Complexity: O(n log n) for recursive sorting
        Space Complexity: O(n) for temporary arrays
        """
        if len(songs) <= 1:
            return songs

        mid = len(songs) // 2
        left = self.merge_sort(songs[:mid], key, reverse)
        right = self.merge_sort(songs[mid:], key, reverse)
        return self._merge(left, right, key, reverse)

    def _merge(self, left, right, key, reverse):
        """
        Merge two sorted lists based on the key.
        Args:
            left (list): Left half of songs
            right (list): Right half of songs
            key (str): Sorting criterion
            reverse (bool): If True, sort in descending order
        Returns:
            list: Merged sorted list
        Time Complexity: O(n) for merging
        Space Complexity: O(n) for result array
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            left_val = left[i][key]
            right_val = right[j][key]
            if key == 'added_order':
                left_val = -left_val  # Higher index is more recent
                right_val = -right_val
            if (left_val <= right_val) != reverse:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_playlist(self, criterion='title', reverse=False):
        """
        Sort the playlist based on the specified criterion.
        Args:
            criterion (str): 'title', 'duration', or 'recently_added'
            reverse (bool): If True, sort in descending order
        Raises:
            ValueError: If criterion is invalid
        Time Complexity: O(n log n) for sorting, O(n) for reconstructing playlist
        Space Complexity: O(n) for temporary list
        """
        if criterion not in ['title', 'duration', 'recently_added']:
            raise ValueError("Invalid sorting criterion")

        # Extract songs from the playlist, respecting reversed state
        songs = []
        current = self.playlist_engine.head
        index = 0
        while current:
            songs.append({
                'title': current.title,
                'artist': current.artist,
                'duration': current.duration,
                'added_order': index
            })
            current = current.next if not self.playlist_engine.reversed else current.prev
            index += 1

        # Map criterion to key
        key = 'added_order' if criterion == 'recently_added' else criterion
        sorted_songs = self.merge_sort(songs, key, reverse)

        # Reconstruct the playlist
        self.playlist_engine.head = None
        self.playlist_engine.tail = None
        self.playlist_engine.size = 0
        for song in sorted_songs:
            self.playlist_engine.add_song(song['title'], song['artist'], song['duration'])

    def sort_playlist_builtin(self, criterion='title', reverse=False):
        """
        Sort the playlist using Python's built-in sort (Timsort) for comparison.
        Args:
            criterion (str): 'title', 'duration', or 'recently_added'
            reverse (bool): If True, sort in descending order
        Raises:
            ValueError: If criterion is invalid
        Time Complexity: O(n log n) for Timsort, O(n) for reconstructing playlist
        Space Complexity: O(n) for temporary list
        """
        if criterion not in ['title', 'duration', 'recently_added']:
            raise ValueError("Invalid sorting criterion")

        songs = []
        current = self.playlist_engine.head
        index = 0
        while current:
            songs.append({
                'title': current.title,
                'artist': current.artist,
                'duration': current.duration,
                'added_order': index
            })
            current = current.next if not self.playlist_engine.reversed else current.prev
            index += 1

        key = 'added_order' if criterion == 'recently_added' else criterion
        songs.sort(key=lambda x: (-x[key] if key == 'added_order' else x[key]), reverse=reverse)

        # Reconstruct the playlist
        self.playlist_engine.head = None
        self.playlist_engine.tail = None
        self.playlist_engine.size = 0
        for song in songs:
            self.playlist_engine.add_song(song['title'], song['artist'], song['duration'])