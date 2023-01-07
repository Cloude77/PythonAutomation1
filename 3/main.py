import re

text = "lat = 5, lon = 7, a=5"
#match = re.findall(r"((lat|lon)\s*=\s*\d+)", text)
match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text) # key:values
print(match)


text1 = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
#match1 = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text1) # ['bg.jpg']
#match1 = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text1) # [("'", 'bg.jpg')]
match1 = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text1) # [("'", 'bg.jpg')] without number

print(match1)