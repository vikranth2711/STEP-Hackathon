from playlist_engine import PlaylistEngine

def test_playlist_engine():
    """
    Test the PlaylistEngine functionality individually.
    Tests add, delete, move, reverse operations and edge cases.
    """
    print("=== Testing PlaylistEngine ===")
    
    # Initialize playlist
    playlist = PlaylistEngine()
    print("1. Initialize empty playlist")
    playlist.print_playlist()
    
    # Test adding songs
    print("\n2. Adding songs:")
    playlist.add_song("Song A", "Artist X", 180)
    playlist.add_song("Song B", "Artist Y", 200)
    playlist.add_song("Song C", "Artist Z", 150)
    print("After adding 3 songs:")
    playlist.print_playlist()
    print(f"Playlist size: {playlist.size}")
    
    # Test moving songs
    print("\n3. Testing move_song:")
    print("Moving Song A (index 0) to index 2:")
    playlist.move_song(0, 2)
    playlist.print_playlist()
    
    # Test lazy reversal
    print("\n4. Testing lazy reversal:")
    print("Before reversal:")
    playlist.print_playlist()
    playlist.reverse_playlist()
    print("After reversal (lazy - O(1)):")
    playlist.print_playlist()
    
    # Test adding to reversed playlist
    print("\n5. Adding song to reversed playlist:")
    playlist.add_song("Song D", "Artist W", 170)
    print("After adding Song D:")
    playlist.print_playlist()
    
    # Test deleting from reversed playlist
    print("\n6. Testing delete_song in reversed state:")
    print("Deleting song at index 1:")
    playlist.delete_song(1)
    playlist.print_playlist()
    print(f"Playlist size after deletion: {playlist.size}")
    
    # Test edge cases
    print("\n7. Testing edge cases:")
    
    # Test invalid delete
    try:
        playlist.delete_song(10)
    except IndexError as e:
        print(f"Expected error for invalid delete index: {e}")
    
    # Test invalid move
    try:
        playlist.move_song(0, 10)
    except IndexError as e:
        print(f"Expected error for invalid move index: {e}")
    
    # Test moving song to same index
    print("Moving song to same index (should do nothing):")
    playlist.move_song(0, 0)
    playlist.print_playlist()
    
    # Test multiple reversals
    print("\n8. Testing multiple reversals:")
    playlist.reverse_playlist()  # Back to normal
    print("After second reversal (back to normal):")
    playlist.print_playlist()
    
    # Test deleting until empty
    print("\n9. Deleting all songs:")
    while playlist.size > 0:
        print(f"Deleting song at index 0, size before: {playlist.size}")
        playlist.delete_song(0)
        playlist.print_playlist()
    
    print("\n=== PlaylistEngine Testing Complete ===")

if __name__ == "__main__":
    test_playlist_engine()