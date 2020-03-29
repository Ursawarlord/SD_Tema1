def bit_value(number, bit):
    mask = 1 << bit
    if number & mask != 0:
        return 1
    return 0

def counting_sort(the_list, bit):
    counts = [0, 0]
    for item in the_list:
        counts[ bit_value(item, bit) ] += 1
    indices = [0, counts[0]]
    sorted_list = [None] * len(the_list)
    for item in the_list:
        item_bit_value = bit_value(item, bit)
        sorted_list[ indices[item_bit_value] ] = item
        indices[item_bit_value] += 1
    return sorted_list

def radix_sort_bit(the_list):
    for bit_index in range(64):
        the_list = counting_sort(the_list, bit_index)
    return the_list

