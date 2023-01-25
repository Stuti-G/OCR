import easyocr

reader = easyocr.Reader(['en'])

results = reader.readtext('test_image.jpg')

text = ''
for result in results:
    text += result[1] + ' '
    
print(text)