# ioc-ocr-extractor
Python3 based Indicator of Compromise extraction tool that uses Tesseract-OCR and regex patterns.
Built as a comparison/basline for comparing to an approach using LLMs (see [***AIOCRIOC***](https://github.com/referefref/aiocrioc))

## Setup (tested on Ubuntu 22.04 with python3-venv)
```bash
# Download and install requirements
apt install tesseract-ocr python3 python3-venv git -y
# Clone git repo
git clone https://github.com/referefref/ioc-ocr-extractor.git
cd ioc-ocr-extractor
# Setup python3 virtual environment
python3 -m venv env
source env/bin/activate
# Install python requirements with pip
pip install -r requirements.txt
```

## Usage
```bash
./extractor.py --url "url" --output "outputfile.json"
```

## Example
```bash
extract.py --url "https://thedfirreport.com/2024/01/29/buzzing-on-christmas-eve-trigona-ransomware-in-3-hours/" --output "test.json"
```

## Leaving venv
```deactivate```
