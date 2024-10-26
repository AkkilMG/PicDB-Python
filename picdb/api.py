# (c) 2024 Akkil MG (https://github.com/AkKiLMG)

import requests
import os

BASE_URL = "https://picdb.izaries.workers.dev/"

def upload_file(file_path):
    """Upload a file to PicDB."""
    if os.path.getsize(file_path) > 20 * 1024 * 1024:  # 20MB limit
        raise ValueError("File size exceeds 20MB limit")
    url = BASE_URL + "upload"
    with open(file_path, "rb") as file:
        files = {"file": file}
        response = requests.post(url, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def upload_link(link):
    """Upload a file from a link to PicDB."""
    url = BASE_URL + "upload"
    if BASE_URL in link:
        raise ValueError("Cannot upload links related to PicDB itself, cloning is unncecessary")
    response = requests.head(link)
    if int(response.headers.get('content-length', 0)) > 20 * 1024 * 1024:  # 20MB limit
        raise ValueError("File size exceeds 20MB limit")
    response = requests.get(link)
    response.raise_for_status()
    file_content = response.content
    file_name = link.split("/")[-1] or "uploaded_file"
    files = {"file": (file_name, file_content)}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def download_file_id(file_id, file_path):
    """Download a file from PicDB."""
    url = BASE_URL + f"d/{file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file_name = response.headers.get('content-disposition').split('filename=')[-1].strip('"') if 'content-disposition' in response.headers else file_id
        full_path = os.path.join(file_path, file_name)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as file:
            file.write(response.content)
    else:
        response.raise_for_status()
