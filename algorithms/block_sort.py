def block_sort(arr, block_size=5):
    def insertion_sort(subarr):
        for i in range(1, len(subarr)):
            key = subarr[i]
            j = i - 1
            while j >= 0 and subarr[j] > key:
                subarr[j + 1] = subarr[j]
                j -= 1
            subarr[j + 1] = key
    
    n = len(arr)
    blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
    
    for block in blocks:
        insertion_sort(block)
    
    sorted_arr = []
    while blocks:
        min_block = min(blocks, key=lambda x: x[0] if x else float('inf'))
        sorted_arr.append(min_block.pop(0))
        if not min_block:
            blocks.remove(min_block)
        yield sorted_arr + [item for sublist in blocks for item in sublist]
