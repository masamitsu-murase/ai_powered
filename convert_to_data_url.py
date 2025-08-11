import sys
import base64


def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_to_data_url.py <html_file>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()
    # Base64エンコード
    encoded = base64.b64encode(html_content.encode('utf-8')).decode('ascii')
    data_url = f"data:text/html;charset=utf-8;base64,{encoded}"
    print(data_url)


if __name__ == "__main__":
    main()
