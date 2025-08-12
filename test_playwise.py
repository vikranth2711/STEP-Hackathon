from playlist_engine import PlaylistEngine
from playback_history import PlaybackHistory
from song_rating_tree import SongRatingTree
from song_lookup import SongLookup
from playlist_sorter import PlaylistSorter
from system_snapshot import SystemSnapshot
from pinned_songs import PinnedSongs
from playlist_summary import PlaylistSummary

def test_playwise():
    """
    Test all functionalities of the PlayWise Hackathon modules.
    Prints results of each test for verification.
    Note: Tests core operations and edge cases for each module.
    """
    # Initialize components
    playlist = PlaylistEngine()
    history = PlaybackHistory(playlist)
    rating_tree = SongRatingTree()
    lookup = SongLookup(playlist)
    sorter = PlaylistSorter(playlist)
    snapshot = SystemSnapshot(playlist, rating_tree, history, sorter)
    pinned = PinnedSongs(playlist)
    summary_gen = PlaylistSummary(playlist)

    # Test PlaylistEngine
    print("Testing PlaylistEngine:")
    playlist.add_song("Song A", "Artist X", 180)
    playlist.add_song("Song B", "Artist Y", 200)
    playlist.add_song("Song C", "Artist Z", 150)
    print("Initial playlist:")
    playlist.print_playlist()

    playlist.move_song(0, 2)
    print("After moving Song A to index 2:")
    playlist.print_playlist()

    playlist.reverse_playlist()
    print("After lazy reversal:")
    playlist.print_playlist()

    playlist.delete_song(1)
    print("After deleting song at index 1:")
    playlist.print_playlist()

    # Test PlaybackHistory
    print("\nTesting PlaybackHistory:")
    history.add_played_song("Song D", "Artist W", 170)
    history.add_played_song("Song E", "Artist V", 190)
    print("History:", history.get_history())
    undone = history.undo_last_play()
    print("Undone song:", undone)
    print("Updated history:", history.get_history())
    print("Playlist after undo:")
    playlist.print_playlist()

    # Test SongRatingTree
    print("\nTesting SongRatingTree:")
    rating_tree.insert_song("song1", "Song A", "Artist X", 180, 4)
    rating_tree.insert_song("song2", "Song B", "Artist Y", 200, 4)
    rating_tree.insert_song("song3", "Song C", "Artist Z", 150, 3)
    print("Songs with rating 4:", rating_tree.search_by_rating(4))
    rating_tree.delete_song("song1")
    print("Songs with rating 4 after deletion:", rating_tree.search_by_rating(4))
    print("Songs with rating 5 (empty):", rating_tree.search_by_rating(5))

    # Test SongLookup
    print("\nTesting SongLookup:")
    song_id1 = lookup.sync_add("Song D", "Artist W", 170)
    song_id2 = lookup.sync_add("Song A", "Artist X", 180)  # Duplicate title
    print("Lookup by ID:", lookup.lookup_by_id(song_id1))
    print("Lookup by title (Song A):", lookup.lookup_by_title("Song A"))
    lookup.sync_delete(song_id1)
    print("After deleting Song D, lookup by ID:", lookup.lookup_by_id(song_id1))
    print("Playlist after deletion:")
    playlist.print_playlist()

    # Test PlaylistSorter
    print("\nTesting PlaylistSorter:")
    sorter.sort_playlist(criterion='title')
    print("Sorted by title:")
    playlist.print_playlist()
    sorter.sort_playlist(criterion='duration', reverse=True)
    print("Sorted by duration (descending):")
    playlist.print_playlist()
    sorter.sort_playlist(criterion='recently_added')
    print("Sorted by recently added:")
    playlist.print_playlist()

    # Test SystemSnapshot
    print("\nTesting SystemSnapshot:")
    result = snapshot.export_snapshot()
    print("Snapshot:")
    print("Top 5 Longest Songs:", result["top_5_longest"])
    print("Recent Plays:", result["recent_plays"])
    print("Rating Counts:", result["rating_counts"])

    # Test PinnedSongs
    print("\nTesting PinnedSongs:")
    # Add a fresh song to ensure we have something to pin
    playlist.add_song("Pin Test Song", "Pin Artist", 160)
    print("Playlist before pinning:")
    playlist.print_playlist()
    
    # Pin the song we just added (it should be at the last index)
    pinned.pin_song("pin_test", "Pin Test Song", 0)
    pinned.shuffle_playlist()
    print("After shuffling with Pin Test Song pinned at index 0:")
    playlist.print_playlist()
    pinned.unpin_song("pin_test")
    pinned.shuffle_playlist()
    print("After unpinning and shuffling again:")
    playlist.print_playlist()

    # Test PlaylistSummary
    print("\nTesting PlaylistSummary:")
    genre_map = {
        "Song A": "Pop",
        "Song B": "Rock",
        "Song C": "Jazz",
        "Song E": "Pop",
        "Pin Test Song": "Electronic"
    }
    summary = summary_gen.generate_summary(genre_map)
    print("Playlist Summary:")
    print("Genre Distribution:", summary["genre_distribution"])
    print("Total Playtime:", summary["total_playtime"], "seconds")
    print("Artist Count:", summary["artist_count"])

if __name__ == "__main__":
    test_playwise()