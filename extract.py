import argparse
import json
import os
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from PIL import Image
import pytesseract
from colorama import Fore, Style

# Regular expressions for IOCs
ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
sha_pattern = r'\b[0-9a-fA-F]{40}\b'
md5_pattern = r'\b[0-9a-fA-F]{32}\b'
domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}\b'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

patterns = {
    "IPv4": ipv4_pattern,
    "IPv6": ipv6_pattern,
    "SHA": sha_pattern,
    "MD5": md5_pattern,
    "Domain": domain_pattern,
    "Email": email_pattern,
}

def download_page(url, user_agent):
    print(Fore.GREEN + f"Downloading page: {url}" + Style.RESET_ALL)
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(Fore.BLUE + "Page downloaded successfully." + Style.RESET_ALL)
    return response.text

def download_images(soup, base_url):
    print(Fore.GREEN + "Downloading images..." + Style.RESET_ALL)
    images = soup.find_all('img')
    image_paths = []
    for img in images:
        img_url = urljoin(base_url, img['src'])
        img_response = requests.get(img_url)
        img_name = img_url.split('/')[-1]
        with open(img_name, 'wb') as f:
            f.write(img_response.content)
        image_paths.append(img_name)
        print(Fore.YELLOW + f"Downloaded image: {img_name}" + Style.RESET_ALL)
    print(Fore.BLUE + "Image download completed." + Style.RESET_ALL)
    return image_paths

def ocr_image(image_path):
    print(Fore.GREEN + f"Performing OCR on image: {image_path}" + Style.RESET_ALL)
    text = pytesseract.image_to_string(Image.open(image_path))
    print(Fore.BLUE + "OCR completed." + Style.RESET_ALL)
    return text

def extract_iocs(text):
    print(Fore.GREEN + "Extracting IOCs..." + Style.RESET_ALL)
    iocs = []
    for ioc_type, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            iocs.append({
                "Indicator ID": len(iocs) + 1,
                "Indicator Type": ioc_type,
                "Indicator Content": match.group(),
                "Surrounding Context": text[max(0, match.start() - 50):min(len(text), match.end() + 50)],
            })
    print(Fore.BLUE + "IOC extraction completed." + Style.RESET_ALL)
    return iocs

def main(url, output_file, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"):
    print(Fore.CYAN + "Starting main process..." + Style.RESET_ALL)
    page_content = download_page(url, user_agent)
    soup = BeautifulSoup(page_content, 'html.parser')
    text_content = soup.get_text()
    iocs = extract_iocs(text_content)

    base_url = url
    image_paths = download_images(soup, base_url)
    for img_path in image_paths:
        img_text = ocr_image(img_path)
        iocs += extract_iocs(img_text)

    with open(output_file, 'w') as f:
        json.dump(iocs, f, indent=4)
    print(Fore.GREEN + f"Process completed. IOCs written to {output_file}" + Style.RESET_ALL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract IOCs from a webpage.')
    parser.add_argument('--url', required=True, help='The URL of the webpage to analyze')
    parser.add_argument('--output', required=True, help='The JSON file to output')
    args = parser.parse_args()

    main(args.url, args.output)
