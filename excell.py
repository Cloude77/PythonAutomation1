import re

#text = "(еда), счастье, победа"
#match = re.findall(r"\(еда\)", text)

# ------------------------------------

#text = "Еда, счастье, победа, -5 55 Америка"
#match = re.findall(r"[еЕ]д[ау]", text)
#match = re.findall(r"[0-9]", text) # 5
#match = re.findall(r"[-0-9][0-9]", text) # 55 if in text 55 -5
#match = re.findall(r"[^0-9]", text) # ['Е', 'д', 'а', ',', list
#match = re.findall(r"[а-яА-Я]", text)
#match = re.findall(r"[а-яА-Я0-9]", text)

#--------------------------------------------

#text = "Еда, счастье, победа, -5 55 Америка"
#match = re.findall(r"\d", text) # ['5', '5', '5']
#match = re.findall(r".", text) #['Е', 'д', 'а', ',', ' ', 'с' all symbol
#match = re.findall(r"\w", text) # ч', 'а', 'с',
#match = re.findall(r"\w", text, re.ASCII) #['5', '5', '5']

#--------------------------------------------

text = "0xf, 0xa, 0x5"
match = re.findall(r"0x[\da-fA-f]", text) #['0xf', '0xa', '0x5']

print(match)
