import codecs

input_str = input("Enter string: ")
base64 = codecs.encode(codecs.decode(input_str, 'hex'), 'base64').decode()
print (base64)
