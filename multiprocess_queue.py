# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 5. Using multiprocessing.Queue for Interprocess Communication (IPC)
# December 17, 2022

# Imports

# 1
import time
from hashlib import md5
from itertools import product
from string import ascii_lowercase

# 3: Encapsulating the formula for the combination in a new class - Combinations
class Combinations:
    def __init__(self, alphabet, length):
        self.alphabet = alphabet
        self.length = length

    def __len__(self):
        return len(self.alphabet) ** self.length

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return "".join(
            self.alphabet[
                (index // len(self.alphabet) ** i) % len(self.alphabet)
            ]
            for i in reversed(range(self.length))
        )

# 1: Reversing an MD5 Hash on a Single Thread
def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
    for length in range(1, max_length + 1):
        for combination in product(alphabet, repeat=length):
            text_bytes = "".join(combination).encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

def main():
    t1 = time.perf_counter()
    text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960")
    print(f"{text} (found in {time.perf_counter() - t1:.1f}s)")

# 2: Distributing Workload Evenly in Chunks, Helper Function
def chunk_indices(length, num_chunks):
    start = 0
    while num_chunks > 0:
        num_chunks = min(num_chunks, length)
        chunk_size = round(length / num_chunks)
        yield start, (start := start + chunk_size)
        length -= chunk_size
        num_chunks -= 1

if __name__ == "__main__":
    main()  