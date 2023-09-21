
def encode(msg, shift):
    ascii = convert_to_ascii(msg)
    result = []
    for n in ascii:
        if n != 32:
            result.append(chr(n + shift))
        else:
            result.append(chr(n))

    return "".join(result)


def convert_to_ascii(msg):
    ascii_list = []
    for letter in msg:
        ascii_list.append(ord(letter))
    return ascii_list


message = input("Enter your message: ")
shift_num = int(input("Enter the shift number: "))

print(encode(message, shift_num))
