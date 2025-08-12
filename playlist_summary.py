from playlist_engine import PlaylistEngine

# Playlist Summary for generating genre distribution, playtime, and artist count
class PlaylistSummary:
    def __init__(self, playlist_engine):
        """
        Initialize the playlist summary generator.
        Args:
            playlist_engine: Instance of PlaylistEngine
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.playlist_engine = playlist_engine

    def generate_summary(self, genre_map):
        """
        Generate a summary of the playlist including genre distribution,
        total playtime, and artist count.
        Args:
            genre_map (dict): Mapping of song titles to genres
        Returns:
            dict: Summary containing:
                - genre_distribution: Dict of genre to count
                - total_playtime: Total duration in seconds
                - artist_count: Number of unique artists
        Time Complexity: O(n) for traversing the playlist
        Space Complexity: O(k) where k is the number of unique genres/artists
        """
        summary = {
            "genre_distribution": {},
            "total_playtime": 0,
            "artist_count": 0
        }

        # Use HashMaps for aggregation
        genre_counts = {}
        artist_set = set()
        total_duration = 0

        # Traverse playlist, respecting reversed state
        current = self.playlist_engine.head
        while current:
            title = current.title
            artist = current.artist
            duration = current.duration

            # Update genre distribution
            genre = genre_map.get(title, "Unknown")
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

            # Update artist set
            artist_set.add(artist)

            # Update total playtime
            total_duration += duration

            current = current.next if not self.playlist_engine.reversed else current.prev

        summary["genre_distribution"] = genre_counts
        summary["total_playtime"] = total_duration
        summary["artist_count"] = len(artist_set)
        return summary