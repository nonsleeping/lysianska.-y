word1 = input("Введіть слово, яке хочете замінити:")
word2 = input("Введіть слово, на яке хочете замінити:")
with open('text.doc') as text_in:
    text = text_in.read()

print("Було:", text)
text = text.replace(word1, word2)

with open("text.doc", "w") as text_out:
    text_out.write(text)
print("Стало:", text)