class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.occupied = 0

    def get_num_slots(self):
        return self.capacity


    def get_load_factor(self):
        return self.occupied / self.capacity # current occupied buckets / capacity


    # not doing this one
    def fnv1(self, key):
        pass


    def djb2(self, key):
        hash_value = 5381
        for x in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(x)
        return hash_value


    def hash_index(self, key):
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        # bucket being added to
        current = self.table[self.hash_index(key)]

        # for adding new value to empty bucket
        if current is None:
            self.table[self.hash_index(key)] = HashTableEntry(key, value)
        else:
            # for changing value of item
            if key == current.key:
                current.value = value
            else:
                holder = current
                while current.next is not None:
                    current = holder.next

                current = HashTableEntry(key, value)


    def delete(self, key):
        current = self.table[self.hash_index(key)]
        if current.key == key:
            if current.next is not None:
                current = current.next
            else:
                current.value = None
        else:
            print("No value was found in this location")


    def get(self, key):
        search = self.table[self.hash_index(key)]
        searching = None

        if search is not None:
            if search.key != key:
                searching = search
                while searching.next is not None:
                    searching = searching.next
                return searching.value
            else:
                return search.value

        else:
            return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"), "SHOULD RETURN POEM")

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
