# PlayWise - Advanced Playlist Management System

A high-performance playlist management system built with optimized data structures and algorithms for efficient music playlist operations.

## 🎵 Overview

PlayWise is a comprehensive playlist management system designed for the STEP Hackathon. It implements advanced data structures including doubly linked lists, binary search trees, hash maps, and stacks to provide efficient playlist operations with optimal time and space complexity.

## 🚀 Features

### Core Functionality

- **Playlist Engine**: Doubly linked list-based playlist with O(1) add/delete operations
- **Lazy Reversal**: O(1) playlist reversal using deferred execution
- **Smart Song Movement**: Constant-time node swapping for efficient reordering
- **Playback History**: Stack-based undo functionality for recently played songs
- **Song Rating System**: BST-based rating management (1-5 stars)
- **Fast Song Lookup**: HashMap-based O(1) song retrieval by ID or title
- **Advanced Sorting**: Merge sort implementation with multiple criteria
- **System Snapshots**: Live statistics generation with top songs and rating distribution
- **Pinned Songs**: Fisher-Yates shuffle with position locking
- **Playlist Analytics**: Genre distribution and comprehensive summaries

### Performance Optimizations

- **O(1)** song addition and deletion
- **O(1)** playlist reversal (lazy evaluation)
- **O(log n)** rating-based song search
- **O(n log n)** stable sorting with merge sort
- **O(1)** song lookup by ID/title

## 📁 Project Structure

```
PlayWise/
├── playlist_engine.py      # Core doubly linked list playlist
├── song_node.py           # Song node data structure
├── playback_history.py    # Stack-based playback history
├── song_rating_tree.py    # BST for song ratings
├── song_lookup.py         # HashMap for fast song lookup
├── playlist_sorter.py     # Merge sort implementation
├── system_snapshot.py     # Live statistics generator
├── pinned_songs.py        # Shuffle with position locking
├── playlist_summary.py    # Analytics and summaries
├── test_playlist_engine.py # Individual playlist tests
├── test_system_snapshot.py # Individual snapshot tests
├── test_playwise.py       # Comprehensive system tests
├── .gitignore            # Git ignore configuration
└── Documents/            # Project documentation
    └── whole.txt         # Complete project documentation
```

## 🛠️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/vikranth2711/PlayWise.git
   cd PlayWise
   ```

2. **Python Requirements**

   - Python 3.7 or higher
   - No external dependencies required (uses only standard library)

3. **Verify Installation**
   ```bash
   python test_playlist_engine.py
   python test_system_snapshot.py
   python test_playwise.py
   ```

## 🔧 Usage Examples

### Basic Playlist Operations

```python
from playlist_engine import PlaylistEngine

# Initialize playlist
playlist = PlaylistEngine()

# Add songs
playlist.add_song("Bohemian Rhapsody", "Queen", 355)
playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)
playlist.add_song("Hotel California", "Eagles", 391)

# Move songs
playlist.move_song(0, 2)  # Move first song to third position

# Reverse playlist (O(1) lazy operation)
playlist.reverse_playlist()

# Print current state
playlist.print_playlist()
```

### Advanced Features

```python
from song_rating_tree import SongRatingTree
from playback_history import PlaybackHistory
from system_snapshot import SystemSnapshot

# Rating system
rating_tree = SongRatingTree()
rating_tree.insert_song("song1", "Bohemian Rhapsody", "Queen", 355, 5)

# Playback history with undo
history = PlaybackHistory(playlist)
history.add_played_song("Stairway to Heaven", "Led Zeppelin", 482)
undone = history.undo_last_play()  # Returns song to playlist

# Generate system snapshot
snapshot = SystemSnapshot(playlist, rating_tree, history, sorter)
stats = snapshot.export_snapshot()
print("Top 5 longest songs:", stats["top_5_longest"])
print("Rating distribution:", stats["rating_counts"])
```

### Pinned Shuffle

```python
from pinned_songs import PinnedSongs

pinned = PinnedSongs(playlist)

# Pin favorite song to stay at top
pinned.pin_song("fav1", "Bohemian Rhapsody", 0)

# Shuffle playlist (pinned songs stay in place)
pinned.shuffle_playlist()
```

## 🧪 Testing

### Run Individual Module Tests

```bash
# Test core playlist functionality
python test_playlist_engine.py

# Test system snapshot generation
python test_system_snapshot.py

# Test complete system integration
python test_playwise.py
```

### Test Coverage

- ✅ Core playlist operations (add, delete, move, reverse)
- ✅ Lazy reversal functionality
- ✅ Song rating and search operations
- ✅ Playback history with undo
- ✅ Sorting algorithms (merge sort vs built-in)
- ✅ System snapshot generation
- ✅ Pinned song shuffling
- ✅ Edge cases and error handling

## ⚡ Performance Benchmarks

| Operation         | Time Complexity | Space Complexity |
| ----------------- | --------------- | ---------------- |
| Add Song          | O(1)            | O(1)             |
| Delete Song       | O(n)            | O(1)             |
| Move Song         | O(n)            | O(1)             |
| Reverse Playlist  | O(1)            | O(1)             |
| Song Lookup       | O(1) avg        | O(1)             |
| Rating Search     | O(log n)        | O(1)             |
| Sort Playlist     | O(n log n)      | O(n)             |
| Generate Snapshot | O(n log n)      | O(n)             |

## 🎯 Key Algorithms

- **Doubly Linked List**: Efficient bidirectional traversal
- **Lazy Evaluation**: Deferred playlist reversal
- **Binary Search Tree**: Balanced rating-based organization
- **HashMap**: Constant-time song lookup
- **Merge Sort**: Stable O(n log n) sorting
- **Fisher-Yates Shuffle**: Unbiased randomization
- **Stack**: LIFO playback history management

## 📖 Documentation

For detailed technical documentation, algorithm explanations, and implementation details, refer to:

- [`Documents/whole.txt`](Documents/whole.txt) - Complete project documentation
- Individual module docstrings for specific functionality
- Test files for usage examples and edge cases

## 🤝 Contributing

This project was developed for the STEP Hackathon. For improvements or bug fixes:

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Ensure all existing tests pass
5. Submit a pull request

## 📄 License

This project is part of the STEP Hackathon submission. Please refer to the hackathon guidelines for usage terms.

## 🏆 Hackathon Features

- **Optimized Data Structures**: Custom implementations for maximum efficiency
- **Comprehensive Testing**: Full test coverage with edge cases
- **Performance Analysis**: Time/space complexity documentation
- **Real-world Applications**: Practical playlist management features
- **Scalable Design**: Modular architecture for easy extension

---

**Built with ❤️ for the STEP Hackathon**

For questions or support, please refer to the documentation in the [`Documents/`](Documents/) folder.
