hex_input = "1c0111001f010100061a024b53535009181c"

key = "686974207468652062756c6c277320657965"

int_input = int(hex_input, 16) 

int_key = int(key, 16)

result = hex(int_input ^ int_key)

print (result[2:])

