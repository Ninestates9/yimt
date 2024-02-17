import easyocr

# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('./examples/chinese.jpg')
# print(result)

# reader = easyocr.Reader(['ja','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('./examples/japanese.jpg')
# print(result)

# reader = easyocr.Reader(['ko','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('./examples/korean.png')
# print(result)

# reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
# result = reader.readtext('./examples/english.png')
# print(result)

# reader = easyocr.Reader(['th', 'en']) # this needs to run only once to load the model into memory
# result = reader.readtext('./examples/thai.jpg')
# print(result)

reader = easyocr.Reader(['ar', 'en']) # this needs to run only once to load the model into memory
result = reader.readtext('./examples/arab.png')
print(result)