# Node for Binary Search Tree, representing a rating bucket
class RatingNode:
    def __init__(self, rating):
        """
        Initialize a rating node for the BST.
        Args:
            rating (int): Rating value (1 to 5)
        """
        self.rating = rating  # Rating value (1 to 5)
        self.songs = []      # List to store songs with this rating
        self.left = None     # Left child node
        self.right = None    # Right child node

# Song Rating Tree using Binary Search Tree
class SongRatingTree:
    def __init__(self):
        """
        Initialize the song rating BST.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root = None
        self.song_id_to_node = {}  # HashMap to map song_id to (rating, song_index) for O(1) deletion

    def insert_song(self, song_id, title, artist, duration, song_rating):
        """
        Insert a song into the BST under the given rating bucket.
        Args:
            song_id (str): Unique identifier for the song
            title (str): Song title
            artist (str): Song artist
            duration (int): Song duration in seconds
            song_rating (int): Rating from 1 to 5
        Time Complexity: O(h) where h is tree height (O(log n) balanced, O(n) skewed)
        Space Complexity: O(1) for node creation (excluding song data)
        """
        if song_rating < 1 or song_rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        song_data = {"song_id": song_id, "title": title, "artist": artist, "duration": duration}
        
        # If tree is empty, create root
        if not self.root:
            self.root = RatingNode(song_rating)
            self.root.songs.append(song_data)
            self.song_id_to_node[song_id] = (song_rating, 0)
            return

        # Find or create the rating node
        current = self.root
        while current:
            if song_rating == current.rating:
                current.songs.append(song_data)
                self.song_id_to_node[song_id] = (song_rating, len(current.songs) - 1)
                return
            elif song_rating < current.rating:
                if current.left is None:
                    current.left = RatingNode(song_rating)
                    current.left.songs.append(song_data)
                    self.song_id_to_node[song_id] = (song_rating, 0)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = RatingNode(song_rating)
                    current.right.songs.append(song_data)
                    self.song_id_to_node[song_id] = (song_rating, 0)
                    return
                current = current.right

    def search_by_rating(self, rating):
        """
        Return all songs with the specified rating.
        Args:
            rating (int): Rating to search for (1 to 5)
        Returns:
            list: List of song dictionaries with the given rating
        Time Complexity: O(h) where h is tree height (O(log n) balanced, O(n) skewed)
        Space Complexity: O(1) excluding the output list
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        current = self.root
        while current:
            if rating == current.rating:
                return current.songs
            elif rating < current.rating:
                current = current.left
            else:
                current = current.right
        return []

    def delete_song(self, song_id):
        """
        Delete a song by its song_id from the BST.
        Args:
            song_id (str): Unique identifier of the song to delete
        Returns:
            bool: True if deletion was successful, False if song_id not found
        Time Complexity: O(h) for finding the rating node, O(1) for removing song from list
        Space Complexity: O(1)
        Note: Simplified deletion; removes empty buckets but does not rebalance the BST
        """
        if song_id not in self.song_id_to_node:
            return False

        rating, song_index = self.song_id_to_node[song_id]
        current = self.root
        while current:
            if rating == current.rating:
                if song_index >= len(current.songs):
                    return False
                # Remove the song from the bucket
                current.songs.pop(song_index)
                del self.song_id_to_node[song_id]
                # If the bucket is empty, remove the node
                if not current.songs:
                    self._remove_empty_node(current, rating)
                return True
            elif rating < current.rating:
                current = current.left
            else:
                current = current.right
        return False

    def _remove_empty_node(self, node, rating):
        """
        Remove an empty rating node from the BST.
        Args:
            node: The RatingNode to remove
            rating: The rating of the node
        Time Complexity: O(h) to find parent
        Space Complexity: O(1)
        Note: Simplified removal; does not fully rebalance the BST
        """
        if not self.root or node.songs:
            return

        if node == self.root:
            self.root = None
            return

        # Find parent
        parent = None
        current = self.root
        while current and current.rating != rating:
            parent = current
            if rating < current.rating:
                current = current.left
            else:
                current = current.right

        if not current:
            return

        # Remove reference from parent
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None