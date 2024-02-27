text = 'cdedd4b9428d465a3024bcbe909d677ffffffffxx2020202020202020202020'
print(len(text))
data = [text[i:i+32] for i in range(0, len(text) - 31, 32)]
print(data)