from song_node import SongNode

# Optimized Playlist Engine using Doubly Linked List
class PlaylistEngine:
    def __init__(self):
        """
        Initialize the playlist engine with a doubly linked list.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None  # Head of the doubly linked list
        self.tail = None  # Tail of the doubly linked list
        self.size = 0     # Number of songs in the playlist
        self.reversed = False  # Flag for lazy reversal to optimize reverse operation

    def add_song(self, title, artist, duration):
        """
        Add a song to the end of the playlist (or front if reversed).
        Args:
            title (str): Song title
            artist (str): Song artist
            duration (int): Song duration in seconds
        Time Complexity: O(1) for appending to tail or head
        Space Complexity: O(1) for node creation
        """
        new_node = SongNode(title, artist, duration)
        if self.reversed:
            # Add to front (logical end in reversed state)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            # Add to end
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
        self.size += 1

    def delete_song(self, index):
        """
        Delete a song at the specified index.
        Args:
            index (int): Index of the song to delete
        Raises:
            IndexError: If index is invalid
        Time Complexity: O(n) to traverse to index
        Space Complexity: O(1) for pointer updates
        """
        if index < 0 or index >= self.size or not self.head:
            raise IndexError("Invalid index")

        # Adjust index for reversed state
        if self.reversed:
            index = self.size - 1 - index

        current = self.head
        # Fix: Remove the incorrect traversal logic that was causing the bug
        for _ in range(index):
            current = current.next

        # If deleting the only node
        if self.size == 1:
            self.head = None
            self.tail = None
        # If deleting the head
        elif current == self.head:
            self.head = current.next
            self.head.prev = None
        # If deleting the tail
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = None
        # Deleting a middle node
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1

    def move_song(self, from_index, to_index):
        """
        Move a song from from_index to to_index using node swaps.
        Args:
            from_index (int): Source index
            to_index (int): Destination index
        Raises:
            IndexError: If indices are invalid
        Time Complexity: O(n) to traverse to indices, O(1) for swap
        Space Complexity: O(1) for pointer updates
        Optimization: Uses constant-time node swaps instead of re-linking
        """
        if from_index < 0 or from_index >= self.size or to_index < 0 or to_index >= self.size:
            raise IndexError("Invalid index")
        if from_index == to_index:
            return

        # Adjust indices for reversed state
        if self.reversed:
            from_index = self.size - 1 - from_index
            to_index = self.size - 1 - to_index

        # Find nodes at from_index and to_index
        from_node = self.head
        for _ in range(from_index):
            from_node = from_node.next if not self.reversed else from_node.prev

        to_node = self.head
        for _ in range(to_index):
            to_node = to_node.next if not self.reversed else to_node.prev

        # Swap nodes
        self._swap_nodes(from_node, to_node)

    def _swap_nodes(self, node1, node2):
        """
        Swap two nodes in the doubly linked list in constant time.
        Args:
            node1: First node
            node2: Second node
        Time Complexity: O(1)
        Space Complexity: O(1)
        Note: Handles adjacent and non-adjacent nodes, updating head/tail as needed
        """
        if node1 == node2:
            return

        # Handle adjacent nodes
        if node1.next == node2:
            node1.next = node2.next
            node2.prev = node1.prev
            node1.prev = node2
            node2.next = node1
        elif node2.next == node1:
            node2.next = node1.next
            node1.prev = node2.prev
            node2.prev = node1
            node1.next = node2
        else:
            # Swap pointers for non-adjacent nodes
            node1.next, node2.next = node2.next, node1.next
            node1.prev, node2.prev = node2.prev, node1.prev

        # Update next node's prev pointers
        if node1.next:
            node1.next.prev = node1
        if node2.next:
            node2.next.prev = node2

        # Update prev node's next pointers
        if node1.prev:
            node1.prev.next = node1
        if node2.prev:
            node2.prev.next = node2

        # Update head and tail if necessary
        if self.head == node1:
            self.head = node2
        elif self.head == node2:
            self.head = node1
        if self.tail == node1:
            self.tail = node2
        elif self.tail == node2:
            self.tail = node1

    def reverse_playlist(self):
        """
        Reverse the playlist using lazy reversal (toggle a flag).
        The actual reversal is deferred until traversal is needed.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.reversed = not self.reversed

    def print_playlist(self):
        """
        Print the playlist, respecting the reversed state.
        Time Complexity: O(n) to traverse the list
        Space Complexity: O(1)
        """
        if not self.head:
            print("Empty playlist")
            return
        if self.reversed:
            current = self.tail
            while current:
                print(f"{current.title} by {current.artist} ({current.duration}s)")
                current = current.prev
        else:
            current = self.head
            while current:
                print(f"{current.title} by {current.artist} ({current.duration}s)")
                current = current.next