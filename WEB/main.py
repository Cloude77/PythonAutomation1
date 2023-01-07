import requests

# URL of the page to download HTML
web_page = "https://en.wikipedia.org/wiki/Python/_(programming_language)"

# create HTTP response odject
# send a HTTP request to the server and save
# the HTTP response in a response object
response = requests.get(web_page) # download from internet

# wb mode is for writing the binary contents to file
with open("python.html", 'wb') as file: # binary file
    # Saving received content
    file.write(response.content)



