from playlist_engine import PlaylistEngine
from song_rating_tree import SongRatingTree
from playback_history import PlaybackHistory
from playlist_sorter import PlaylistSorter

# System Snapshot for generating live playlist statistics
class SystemSnapshot:
    def __init__(self, playlist_engine, song_rating_tree, playback_history, playlist_sorter):
        """
        Initialize the system snapshot module.
        Args:
            playlist_engine: Instance of PlaylistEngine
            song_rating_tree: Instance of SongRatingTree
            playback_history: Instance of PlaybackHistory
            playlist_sorter: Instance of PlaylistSorter
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.playlist_engine = playlist_engine
        self.song_rating_tree = song_rating_tree
        self.playback_history = playback_history
        self.playlist_sorter = playlist_sorter

    def export_snapshot(self):
        """
        Generate a snapshot with top 5 longest songs, most recently played songs,
        and song count by rating.
        Returns:
            dict: Snapshot containing:
                - top_5_longest: List of top 5 songs by duration (descending)
                - recent_plays: List of recently played songs (up to 5)
                - rating_counts: Dict of rating (1-5) to song count
        Time Complexity: O(n log n) for sorting, O(h) for BST traversal, O(n) for history
        Space Complexity: O(n) for storing sorted songs and output
        """
        snapshot = {
            "top_5_longest": [],
            "recent_plays": [],
            "rating_counts": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        }

        # Extract songs from playlist, respecting reversed state
        songs = []
        current = self.playlist_engine.head
        index = 0
        while current:
            songs.append({
                "title": current.title,
                "artist": current.artist,
                "duration": current.duration,
                "added_order": index
            })
            current = current.next if not self.playlist_engine.reversed else current.prev
            index += 1

        # Sort by duration (descending) using Merge Sort
        sorted_songs = self.playlist_sorter.merge_sort(songs, key="duration", reverse=True)
        snapshot["top_5_longest"] = sorted_songs[:5]

        # Get up to 5 most recent plays (most recent first)
        snapshot["recent_plays"] = self.playback_history.get_history()[-5:][::-1]

        # Traverse BST to count songs per rating
        def traverse_bst(node):
            if not node:
                return
            snapshot["rating_counts"][node.rating] = len(node.songs)
            traverse_bst(node.left)
            traverse_bst(node.right)

        traverse_bst(self.song_rating_tree.root)
        return snapshot