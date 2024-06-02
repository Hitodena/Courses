words = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
print(words)

wordsfilter = []

for element in words:
    if element[0::] == element[::-1]:
        wordsfilter.append(element)

print(wordsfilter)
