# PicDB-Python

PicDB is a Python package that provides both a command-line tool and a library for interacting with the PicDB API. It allows you to upload files, upload from URLs, and download files using the API.

## Features

- Upload a local file to PicDB.
- Upload a file from a URL to PicDB.
- Download a file from PicDB using its file ID.
- Command-line tool to perform these operations from the terminal.

## Installation

To install the `picdb` package, you can use `pip`:

```bash
pip install picdb
```

This will install the package and make the `picdb` command-line tool available.

## Usage

### Command-Line Tool
The `picdb` command-line tool allows you to perform various operations directly from the terminal.

#### Help
To see available commands and options, use:

```bash
picdb help
```

#### Upload a Local File
To upload a file from your local machine:
```bash
picdb upload -f "path/to/your/file.png"
```

#### Upload a File from a URL
To upload a file from a URL:

```bash
picdb upload -l "https://example.com/image.png"
```

#### Download a File
To download a file from PicDB using its file ID:

```bash
picdb download <file_id> -f "path/to/save/directory"
```

### Library Usage
You can also use the `picdb` package as a library in your Python scripts.

#### Example Usage

```python
from picdb import upload_file, upload_link, download_file_id

# Upload a local file
response = upload_file("./tests/test.png")
print("Upload response:", response)

# Upload a file from a link
response = upload_link("https://example.com/image.png")
print("Upload response:", response)

# Download a file using its file ID
download_file_id("file_id_here", "./downloads")
print("Download completed!")
```

## Development

### Running Tests
A test script (`test_cli.py`) is provided to test the command-line interface:

```bash
python test_cli.py
```

Make sure the necessary test files are available (e.g., a test file for upload testing).

## Requirements

- Python 3.6 or higher
- `requests` library (automatically installed with the package)

## Installation from Source
To install the package from the source code:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/picdb.git
```

2. Navigate to the project directory:

```bash
cd picdb
```

3. Install the package:

```bash
pip install .
```