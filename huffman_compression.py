import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)
    
    return heap[0]

def build_huffman_codes(node, current_code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}
    
    if node is None:
        return
    
    if node.char is not None:
        huffman_codes[node.char] = current_code
    
    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)
    
    return huffman_codes

def huffman_compress(text):
    root = build_huffman_tree(text)
    huffman_codes = build_huffman_codes(root)
    
    compressed_bits = ""
    for char in text:
        compressed_bits += huffman_codes[char]
    
    return compressed_bits, huffman_codes

def huffman_decompress(compressed_bits, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    decoded_text = ""
    current_code = ""
    
    for bit in compressed_bits:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""
    
    return decoded_text

# Example usage 
original_text = "hello world"    #type your text here
compressed_bits, huffman_codes = huffman_compress(original_text)
decompressed_text = huffman_decompress(compressed_bits, huffman_codes)

print(f"Original text: {original_text}")
print(f"Compressed bits: {compressed_bits}")
print(f"Decompressed text: {decompressed_text}")
