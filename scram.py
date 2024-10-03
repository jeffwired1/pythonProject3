def scramble_binary(data, shift):
    return bytes((byte + shift) % 256 for byte in data)


def descramble_binary(data, shift):
    return bytes((byte - shift) % 256 for byte in data)


def process_binary_file(file_path, shift, mode):
    with open(file_path, 'rb') as file:
        content = file.read()

    if mode == 'scramble':
        processed_content = scramble_binary(content, shift)
    elif mode == 'descramble':
        processed_content = descramble_binary(content, shift)
    else:
        raise ValueError("Mode should be either 'scramble' or 'descramble'")

    with open(file_path, 'wb') as file:
        file.write(processed_content)


# Example usage
file_path = 'ret1.zip'
shift = 3
mode = 'descramble'  # Change to 'descramble' to reverse
process_binary_file(file_path, shift, mode)