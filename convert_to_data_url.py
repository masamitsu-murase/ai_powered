import argparse
import base64
import sys


def main():
    parser = argparse.ArgumentParser(description="Convert file to data URL.")
    parser.add_argument('filename', help='Input file name')
    parser.add_argument(
        '--type',
        default='text/html',
        help='MIME type (e.g. text/html, audio/mpeg)'
    )
    args = parser.parse_args()

    mime_type = args.type
    filename = args.filename

    if mime_type == 'text/html':
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        encoded = base64.b64encode(content.encode('utf-8')).decode('ascii')
        data_url = f"data:text/html;charset=utf-8;base64,{encoded}"
        print(data_url)
    elif mime_type == 'audio/mpeg':
        with open(filename, 'rb') as f:
            content = f.read()
        encoded = base64.b64encode(content).decode('ascii')
        data_url = f"data:audio/mpeg;base64,{encoded}"
        print(data_url)
    else:
        print("Unsupported type. Only text/html and audio/mpeg are supported.")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
