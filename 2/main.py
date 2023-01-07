import re

text = "Google, Gooogle, Goooooogle"
#match = re.findall(r"o{2,5}?",text) # ? - minor
match = re.findall(r"o{2,5}",text) # ? - minor
print(match)


match1 = re.findall(r"Go{2,}gle", text)
#match1 = re.findall(r"Go{,4}gle", text)
print(match1)

phone = "89123456789"
num = re.findall(r"8\d{10}", phone)
print(num)

text2 = "стеклянныйб стекляный"
txt = re.findall(r"стеклянн?ый", text2)
print(txt)

# key value

text3 = "author=Пушкин А.С.; title = Евгений Онегин; price = 200; year = 2001"
#txt1 = re.findall(r"\w+\s*=\s*[^;]+", text3)
txt1 = re.findall(r"(\w+)\s*=\s*([^;]+)", text3)

print(txt1)

# minor

text4 = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
#txt2 = re.findall(r"<img.*?>", text4) # [<img src='bg.jpg'>]
txt2 = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text4)
print(text4)