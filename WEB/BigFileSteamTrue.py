import requests

# Reseach paper on a new locally linear embedding scheme in light of Hessian eigenmap
large_file_url = "https://arxiv.org/pdf/2112.09086.pdf"


# settings stream to true to enable downloading of large contents
response = requests.get(large_file_url, stream=True)

with open("large_file.pdf", "wb") as pdf:
    # The chunk size is the number of bytes it should read into memory.
    for chunk in response.iter_content(chunk_size=1024):
        # writing one chunk at a time to pdf file
        if chunk:
            pdf.write(chunk)
