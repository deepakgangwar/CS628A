# Reading the qr code directly
# hex_raw = """
# 10111001011100101
# 1010001011100100101
# 011101110000011101010
# 01111010111001000010011
# 0011010001110001110000010
# 001010011010000001100100101
# 00010011001100110100110101011
# 0011011000010000001010000010011
# 0111011000101100100100000011000
# 00011000010101010010001100110
# 011000000110101010101011000
# 1001101000001011011101000
# 10100110011010000011001
# 100110010100010101110
# 1010101110110011001
# 10011001000000110
# """.replace('\n','')

hex_raw = """
01011010100011000
0001101100011011010
100010010001101011000
10011001001010110111011
1011001111010100000011001
000100010001101000001011001
10011010110100001000101010111
0100110011000100100110000011001
0011000000011000000101000001101
11101100101011101101010010011
001110010101010110010101010
1010001000000010101001001
00111001110001010001100
100010101000101011000
0101110110010111010
10101010010011001
""".replace('\n','')
# hex_raw_value = 0b101110010111001011010001011100100101011101110000011101010011110101110010000100110011010001110001110000010001010011010000001100100101000100110011001101001101010110011011000010000001010000010011011101100010110010010000001100000011000010101010010001100110011000000110101010101011000100110100000101101110100010100110011010000011001100110010100010101110101010111011001100110011001000000110
# hex_raw_str = '101110010111001011010001011100100101011101110000011101010011110101110010000100110011010001110001110000010001010011010000001100100101000100110011001101001101010110011011000010000001010000010011011101100010110010010000001100000011000010101010010001100110011000000110101010101011000100110100000101101110100010100110011010000011001100110010100010101110101010111011001100110011001000000110'
# xor_value     = 0b101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
# convert the hex_code to a binary value
# hex_raw = hex_raw[::-1]
# hex_raw_value = int(hex_raw,2)

# # print(len(hex_raw_str))
# # print(bin(hex_raw_value))

# # create a string of the same length to xor with
# xor_value = int(('10'*int(len(hex_raw)/2)),2)
# # print(xor_value)
# # # print(hex_raw_value,xor_value)
# # print(bin(hex_raw_value))
# print(bin(xor_value))
# # # perform XOR and convert back to binary string
# hex_code = str(bin(hex_raw_value ^ xor_value))[2:]
# # print(bin(hex_raw_value ^ xor_value))

# # hex_code = '000'+str(bin(hex_raw_value ^ xor_value))[2:]
# print(hex_code)
# out_string = ""
# i = 2 # skip the 2 bit header

# # add the first character (guessing that bit 6 is set)
# bit6IsSet = True
# out_string = out_string + chr(int(hex_code[i:i + (7 if bit6IsSet else 6)], 2))
# print(bin(hex_raw_value ^ xor_value)[i:i + (7 if bit6IsSet else 6)])
# print(out_string)
# bit6IsSet = False
# out_string = out_string + chr(int(hex_code[i:i + (7 if bit6IsSet else 6)], 2))
# print(bin(hex_raw_value ^ xor_value)[i:i + (7 if bit6IsSet else 6)])
# print(out_string)
# i = i + (7 if bit6IsSet else 6)

# # the rest of the characters are 8 bit
# while i < len(hex_code)-8:
#     out_string = out_string + chr(int(hex_code[i:i+8], 2))
#     i = i + 8

# print(out_string)


# convert the hex_code to a binary value
hex_raw_value = int(hex_raw,2)

# create a string of the same length to xor with
xor_value = int(('10'*int(len(hex_raw)/2))[0:len(hex_raw)],2)

# perform XOR and convert back to binary string
hex_code = str(bin(hex_raw_value ^ xor_value))[2:]
print((bin(hex_raw_value ^ xor_value)))
out_string = ""
out_string_2 = ""
i = 2 # skip the 2 bit header

# add the first character (guessing that bit 6 is set)
bit6IsSet = False
char = hex_code[i:i + (7 if bit6IsSet else 6)]
out_string = out_string + chr(int(char[::-1], 2))
out_string_2 = out_string_2 + chr(int(char, 2))
i = i + (7 if bit6IsSet else 6)

# the rest of the characters are 8 bit
# while i < len(hex_code)-8:
#     char = hex_code[i:i+8]
#     out_string = out_string + chr(int(char[::-1], 2))
#     out_string_2 = out_string_2 + chr(int(char, 2))
#     i = i + 8

# print(out_string)
# print(out_string_2)

i = len(hex_code) -1
print(i)
out_string = ""
out_string_2 = ""
while i > 8:
    char = hex_code[i-7:i]
    out_string = out_string + chr(int(char[::-1], 2))
    out_string_2 = out_string_2 + chr(int(char, 2))
    i = i - 8



print (i)

char = hex_code[0:i]
out_string = out_string + chr(int(char[::-1], 2))
out_string_2 = out_string_2 + chr(int(char, 2))

print(out_string[::-1])
print("2nd")
print(out_string_2)