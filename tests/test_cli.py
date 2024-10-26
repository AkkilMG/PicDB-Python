# (c) 2024 Akkil MG (https://github.com/AkKiLMG)


import subprocess
import os

def run_command(command):
    """Run a command in the shell and return its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Command: {command}")
    print(f"Output: {result.stdout}")
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode

def test_help_command():
    """Test the 'picdb help' command."""
    print("Testing 'picdb help' command...")
    assert run_command("picdb help") == 0

def test_upload_file_command():
    """Test the 'picdb upload' command with a local file."""
    print("Testing 'picdb upload' with a local file...")
    # Make sure the test file exists
    test_file = "./tests/test.png"
    if not os.path.exists(test_file):
        print(f"Test file {test_file} does not exist.")
        return
    assert run_command(f"picdb upload -f {test_file}") == 0

def test_upload_link_command():
    """Test the 'picdb upload' command with a URL."""
    print("Testing 'picdb upload' with a URL...")
    test_link = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/640px-Google_2015_logo.svg.png"
    assert run_command(f"picdb upload -l {test_link}") == 0

def test_download_command():
    """Test the 'picdb download' command with a file ID."""
    print("Testing 'picdb download' command...")
    test_file_id = "HbN4fewfhc6wATS"  # Replace with a valid file ID for testing
    download_dir = "./downloads"
    os.makedirs(download_dir, exist_ok=True)
    assert run_command(f"picdb download {test_file_id} -f {download_dir}") == 0

def main():
    """Run all the tests."""
    print("Starting CLI tests...")
    test_help_command()
    test_upload_file_command()
    test_upload_link_command()
    test_download_command()
    print("CLI tests completed.")

if __name__ == "__main__":
    main()
