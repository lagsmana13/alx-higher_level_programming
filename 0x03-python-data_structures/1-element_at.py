#!/usr/bin/python3

# This function retrieves an element from a list, similar to indexing in C.

def element_at(my_list, idx):
    # Added a comment explaining the index range check
    if idx < 0 or idx >= len(my_list):
        return None  # Changed the return value to explicit None instead of implicit
    return my_list[idx]  # Removed extra whitespace for consistency
