from playlist_engine import PlaylistEngine
from song_rating_tree import SongRatingTree
from playback_history import PlaybackHistory
from playlist_sorter import PlaylistSorter
from system_snapshot import SystemSnapshot

def test_system_snapshot():
    """
    Test the SystemSnapshot functionality individually.
    Tests snapshot generation with various data configurations.
    """
    print("=== Testing SystemSnapshot ===")
    
    # Initialize all required components
    playlist = PlaylistEngine()
    rating_tree = SongRatingTree()
    history = PlaybackHistory(playlist)
    sorter = PlaylistSorter(playlist)
    snapshot = SystemSnapshot(playlist, rating_tree, history, sorter)
    
    print("1. Testing with empty data:")
    result = snapshot.export_snapshot()
    print("Empty snapshot:")
    print(f"  Top 5 Longest: {result['top_5_longest']}")
    print(f"  Recent Plays: {result['recent_plays']}")
    print(f"  Rating Counts: {result['rating_counts']}")
    
    # Add songs to playlist
    print("\n2. Adding songs to playlist:")
    playlist.add_song("Epic Journey", "Rock Band", 450)  # Longest
    playlist.add_song("Quick Beat", "DJ Fast", 120)      # Shortest
    playlist.add_song("Smooth Jazz", "Jazz Master", 280)
    playlist.add_song("Pop Anthem", "Pop Star", 210)
    playlist.add_song("Classical Symphony", "Orchestra", 720)  # Longest
    playlist.add_song("Electronic Pulse", "Synth King", 190)
    
    print("Playlist contents:")
    playlist.print_playlist()
    
    # Add songs to rating tree
    print("\n3. Adding songs to rating tree:")
    rating_tree.insert_song("song1", "Epic Journey", "Rock Band", 450, 5)
    rating_tree.insert_song("song2", "Quick Beat", "DJ Fast", 120, 3)
    rating_tree.insert_song("song3", "Smooth Jazz", "Jazz Master", 280, 4)
    rating_tree.insert_song("song4", "Pop Anthem", "Pop Star", 210, 4)
    rating_tree.insert_song("song5", "Classical Symphony", "Orchestra", 720, 5)
    rating_tree.insert_song("song6", "Electronic Pulse", "Synth King", 190, 3)
    rating_tree.insert_song("song7", "Bonus Track", "Mystery Artist", 160, 2)
    rating_tree.insert_song("song8", "Hidden Gem", "Indie Artist", 240, 1)
    
    # Add playback history
    print("\n4. Adding playback history:")
    history.add_played_song("Classical Symphony", "Orchestra", 720)
    history.add_played_song("Epic Journey", "Rock Band", 450)
    history.add_played_song("Smooth Jazz", "Jazz Master", 280)
    history.add_played_song("Pop Anthem", "Pop Star", 210)
    history.add_played_song("Quick Beat", "DJ Fast", 120)
    history.add_played_song("Electronic Pulse", "Synth King", 190)
    
    print(f"History has {len(history.get_history())} entries")
    
    # Generate comprehensive snapshot
    print("\n5. Generating comprehensive snapshot:")
    result = snapshot.export_snapshot()
    
    print("=== SNAPSHOT RESULTS ===")
    print("\nTop 5 Longest Songs:")
    for i, song in enumerate(result['top_5_longest'], 1):
        print(f"  {i}. {song['title']} by {song['artist']} - {song['duration']}s")
    
    print("\nRecent Plays (up to 5, most recent first):")
    for i, play in enumerate(result['recent_plays'], 1):
        print(f"  {i}. {play['title']} by {play['artist']} - {play['duration']}s")
    
    print("\nRating Distribution:")
    for rating in range(1, 6):
        count = result['rating_counts'][rating]
        stars = "★" * rating + "☆" * (5 - rating)
        print(f"  {stars} ({rating}): {count} songs")
    
    # Test with reversed playlist
    print("\n6. Testing with reversed playlist:")
    playlist.reverse_playlist()
    print("Reversed playlist:")
    playlist.print_playlist()
    
    result_reversed = snapshot.export_snapshot()
    print("\nTop 5 Longest (from reversed playlist):")
    for i, song in enumerate(result_reversed['top_5_longest'], 1):
        print(f"  {i}. {song['title']} - {song['duration']}s")
    
    # Test edge case - delete some ratings
    print("\n7. Testing after deleting some ratings:")
    rating_tree.delete_song("song1")  # Remove a 5-star song
    rating_tree.delete_song("song8")  # Remove the only 1-star song
    
    result_after_delete = snapshot.export_snapshot()
    print("Rating Distribution after deletions:")
    for rating in range(1, 6):
        count = result_after_delete['rating_counts'][rating]
        stars = "★" * rating + "☆" * (5 - rating)
        print(f"  {stars} ({rating}): {count} songs")
    
    # Test with limited history
    print("\n8. Testing with limited history (undo some plays):")
    history.undo_last_play()
    history.undo_last_play()
    history.undo_last_play()
    
    result_limited = snapshot.export_snapshot()
    print(f"\nRecent Plays after undoing 3 plays ({len(result_limited['recent_plays'])} remaining):")
    for i, play in enumerate(result_limited['recent_plays'], 1):
        print(f"  {i}. {play['title']} by {play['artist']}")
    
    print("\n=== SystemSnapshot Testing Complete ===")

if __name__ == "__main__":
    test_system_snapshot()