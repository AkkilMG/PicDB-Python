# (c) 2024 Akkil MG (https://github.com/AkKiLMG)


from picdb import download_file_id, upload_link, upload_file

# Upload a local file
response = upload_file("./tests/test.png")
print("Upload response:", response)

# Upload a file from a link
response = upload_link("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/640px-Google_2015_logo.svg.png")
print("Upload response:", response)

# Download a file using its file ID
download_file_id("HbN4fewfhc6wATS", "./downloads")
print("Download completed!")

