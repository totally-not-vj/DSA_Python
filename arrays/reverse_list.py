# Method 1: Using slicing
def reverse_list_slicing(lst):
    return lst[::-1]

# Method 2: Using the reverse() method (modifies the list in place)
def reverse_list_in_place(lst):
    lst.reverse()
    return lst

# Method 3: Using the reversed() function (returns an iterator)
def reverse_list_reversed(lst):
    return list(reversed(lst))

# Method 4: Using a manual loop
def reverse_list_manual(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Example usage
sample_list = [1, 2, 3, 4, 5]
print("Using slicing:", reverse_list_slicing(sample_list))
print("Using reverse():", reverse_list_in_place(sample_list[:]))  # [:] to avoid modifying original
print("Using reversed():", reverse_list_reversed(sample_list))
print("Using manual loop:", reverse_list_manual(sample_list))
