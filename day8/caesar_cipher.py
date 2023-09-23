
def caesar(msg, shift, mode="encode"):
    ascii = convert_to_ascii(msg)
    result = []
    for n in ascii:
        if n != 32:
            if mode == "encode":
                result.append(chr(n + shift))
            else:
                result.append(chr(n - shift))
        else:
            result.append(chr(n))

    return "".join(result)


def encode(msg, shift):
    ascii = convert_to_ascii(msg)
    result = []
    for n in ascii:
        if n != 32:
            result.append(chr(n + shift))
        else:
            result.append(chr(n))

    return "".join(result)


def decode(msg, shift):
    ascii = convert_to_ascii(msg)
    result = []
    for n in ascii:
        if n != 32:
            result.append(chr(n - shift))
        else:
            result.append(chr(n))

    return "".join(result)


def convert_to_ascii(msg):
    ascii_list = []
    for letter in msg:
        ascii_list.append(ord(letter))
    return ascii_list


run = True

while run:
    keep_playing = input("Type 'c' to continue, 'e' to exit: ")
    if keep_playing == "e":
        print("Finished")
        break
    else:
        mode = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
        message = input("Enter your message: ")
        shift_num = int(input("Enter the shift number: "))

        print(caesar(message, shift_num, mode))
