# lfu cache

'''
revision of LRU cache 
class Node:
    #represents a node in doubly linked list
class LRUCache:
    #initializes the LRU cache with a given capacity
    def __init__(self, capacity:int):
        #initializes the LRU cache with a given capacity
    def _add_node(sefl,node: Node):
        # adds a node to the head of the doubly linked list (most recently used)
    def _remove_node(Self, node:Node):
        # removes a node from the doubly linked list
    def _move_to_head(sefl, node:Node):
        # moves a node to the head of the doubly linked list (marks as recently used)
    def _pop_tail(self):
        # removes and returns the least recently used node (the one before the tail)
    def get(sefl, key:int):
        # gets the value associated with the given key if the key exists in the cache
        updates the key's position in the doubly linked list to mark it as recently used
    def put(self, key, value):
        # puts a key value pair into the cache
        if the key already exists, updates the value and moves it to the head
        if the cache is full, evicts the least recently used item before adding the new one  
        
SUMMARY
 > initialize LRU cache with capacity = 2, keep two dummy nodes head and tail to perform operations easily
 > put(1,1): since(key, value) = (1,1) -> (highest priority) is not present and cache is not full, we can put (1,1) after the head
 > put(2,2): since(key, value) = (2,2) -> (highest priority), [(1,1) -> becomes (lowest priority)] since (2,2) is not present and cache 
 is not full, we can put (2,2) after the head
 > get(1): since key = 1 is present, we can simply return 1 which is the corresponding value and update the prioirty of (1,1) to highest and (2,2) to lowest
 > put (3,3): since(key, value) = (3,3) -> (highest priority) is not present and the size of cache is full, apply LRU algorithm to remove the leat recently used key(2) and we can put (3,3) after the head
 now, we will have removed 2 and added (3,3) next to the head and (1,1) would be near the tail
 > get(2): since key = 2 is not present, we can return -1
 > and so on...
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Node:
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                lru_node = self._pop_tail()
                del self.cache[lru_node.key]

'''
LFU cache requires us to maintain not only key-value pairs but also the frequency of access and the recency 
with each frequency level to efficiently handle evictions based on the LFU policy as a tie-breaer.

the combination of a hash map and a frequency-based doubly linked list is an effective way to solve this problem

SUMMARY:
> Initialize LFU cache with a capacity of 2 and minFreq of 0
> put(1,1): since the key-value pair(1,1) is not present and cache is not full,
first create two dummy nodes, head and tail, with frequency 1, as the cache is empty
insert(1,1) after the head, indicating it has the highest priority. minFreq is updated to 1.
> put(2,2): since the key-value pair(2,2) is not present and the cache is not full, we can insert (2,2) after the head of frequency 1
> get(1): since the key = 1 is present, we can simply return 1, aslo the frequency of key=1 is incremented to 2
A new linked list of frequency 2 is created and key = 1 is inserted into it while being removed from frequency 1
> put(3,3): since the key-value pair(3,3) is not present and the cache is full, remoce the least priority element (2,2) from the doubly lined list of minimum frequency
curently, the minFreq is 1, so remove key = 2 we can insert (3,3) after the head of frequency 1
> get(2): since the key = 2 is not present, we can simply return -1
> put(4,4): since the key-value pair(4,4) is not present and the cache is full, remoce the least priority element (3,3) from the doubly lined list of minimum frequency
curently, the minFreq is 1, so remove key = 3 we can insert (4,4) after the head of frequency 1
> get(3): since the key = 3 is not present, we can simply return -1
> get(4): since the key = 4 is present, we can simply return 4, aslo the frequency of key=4 is incremented to 2
insert key = 4 into linked list of frequency 2 and key = 4 is inserted into it while being removed from frequency 1
> finally, since there are no nodes left in frequency 1, the linked list of frequency 1 is deleted and minFreq is changed to 2
'''
class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_map = {}
        self.min_freq = 0

    def _add_node(self, node):
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].add_head(node)

    def _remove_node(self, node):
        self.freq_map[node.freq].remove(node)
        if self.freq_map[node.freq].size == 0 and self.min_freq == node.freq:
            self.min_freq += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove_node(node)
        node.freq += 1
        self._add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            node.freq += 1
            self._add_node(node)
        else:
            if len(self.cache) == self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                evict_node = lfu_list.pop_tail()
                del self.cache[evict_node.key]
                if lfu_list.size == 0:
                    del self.freq_map[self.min_freq]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.min_freq = 1

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def pop_tail(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None