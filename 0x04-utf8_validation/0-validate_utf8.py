#!/usr/bin/python3

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list of int): A list of integers representing bytes of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0  # Number of bytes in the current UTF-8 character

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7  # Mask to check the leading bit

        if n_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & num:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue  # 1-byte character

            if n_bytes == 1 or n_bytes > 4:
                return False  # Invalid length

        else:
            # Check continuation bytes start with 10
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0  # All characters must be completely checked
