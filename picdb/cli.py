# (c) 2024 Akkil MG (https://github.com/AkKiLMG)


import argparse
import sys
from picdb import download_file_id, upload_file, upload_link

def main():
    parser = argparse.ArgumentParser(
        description="PicDB Command-Line Interface"
    )
    subparsers = parser.add_subparsers(dest="command")

    # `picdb help` command
    subparsers.add_parser("help", help="Show help")

    # `picdb upload` command
    upload_parser = subparsers.add_parser("upload", help="Upload a file to PicDB")
    upload_parser.add_argument("-f", "--file_path", type=str, help="Path to the file")
    upload_parser.add_argument("-l", "--link", type=str, help="Link to the file")

    download_parser = subparsers.add_parser("download", help="Download a file from PicDB")
    download_parser.add_argument("file_id", type=str, help="File ID")
    download_parser.add_argument("-f", "--file_path", type=str, help="Path to save the file")

    args = parser.parse_args()

    if args.command == "help":
        parser.print_help()
    elif args.command == "upload":
        try:
            if args.link:
                result = upload_link(args.link)
            else:
                result = upload_file(args.file_path)
            print(f"File uploaded successfully: {result}")
        except Exception as e:
            print(f"Error uploading file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "download":
        if not args.file_id or not args.file_path:
            print("Both file ID and file path are required for downloading.", file=sys.stderr)
            sys.exit(1)
        try:
            download_file_id(args.file_id, args.file_path)
            print(f"File downloaded successfully to {args.file_path}")
        except Exception as e:
            print(f"Error downloading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
