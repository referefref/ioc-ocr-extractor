# ioc-ocr-extractor
Python3 based Indicator of Compromise extraction tool that uses Tesseract-OCR and regex patterns.
Built as a comparison/basline for comparing to an approach using LLMs (see [***AIOCRIOC***](https://github.com/referefref/aiocrioc))

## Note
This is a PoC only, if you want to use this for production purposes, consider the regex patterns used for domain names as there's obvious false positives with file extensions.
I'd considered an exclusion list but there exists some overlap between the set of domains and the set of filenames, for instance .com

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

## Example output
```json
[
    {
        "Indicator ID": 1,
        "Indicator Type": "IPv4",
        "Indicator Content": "77.83.36.6",
        "Surrounding Context": " here.\nTimeline\n\nDiamond Model\n\nIndicators\nAtomic\n77.83.36.6\r\n193.106.31.98\r\n\nComputed\nbuild_redacted.exe\r\n185"
    },
    {
        "Indicator ID": 2,
        "Indicator Type": "IPv4",
        "Indicator Content": "193.106.31.98",
        "Surrounding Context": "ine\n\nDiamond Model\n\nIndicators\nAtomic\n77.83.36.6\r\n193.106.31.98\r\n\nComputed\nbuild_redacted.exe\r\n1852be15aa8dcf6642"
    },
    {
        "Indicator ID": 3,
        "Indicator Type": "SHA",
        "Indicator Content": "eea811d2a304101cc0b0edebe6590ea0f3da0a27",
        "Surrounding Context": "d_redacted.exe\r\n1852be15aa8dcf664291b3849bd348e4\r\neea811d2a304101cc0b0edebe6590ea0f3da0a27\r\nd743daa22fdf4313a10da027b034c603eda255be037cb45b"
    },
    {
        "Indicator ID": 4,
        "Indicator Type": "SHA",
        "Indicator Content": "21b7460aa5f7eb7a064d2a7a6837da57719f9c2e",
        "Surrounding Context": "efenderOFF.bat\r\nc5d7ce243c1d735d9ca419cc916b87ec\r\n21b7460aa5f7eb7a064d2a7a6837da57719f9c2e\r\nd6d8302d8db7f17aaa45059b60eb8de33166c95d1d833ca4"
    },
    {
        "Indicator ID": 5,
        "Indicator Type": "SHA",
        "Indicator Content": "2f5991e67615763865b7e4c4c9558eb447ed7c0d",
        "Surrounding Context": "9\r\n\r\nipall.bat\r\nb2bb4d49c38f06a42f15b39744d425d0\r\n2f5991e67615763865b7e4c4c9558eb447ed7c0d\r\n12f838b54c6dac78f348828fe34f04ac355fa8cc24f8d7c7"
    },
    {
        "Indicator ID": 6,
        "Indicator Type": "SHA",
        "Indicator Content": "a73fbffe33ea82b20c4129e552fbc5b76891080e",
        "Surrounding Context": "DefenderON.bat\r\n718f68b24d1e331e60e1a10c92a81961\r\na73fbffe33ea82b20c4129e552fbc5b76891080e\r\n40fe2564e34168bf5470bbe0247bc614117334753a107b2b"
    },
    {
        "Indicator ID": 7,
        "Indicator Type": "SHA",
        "Indicator Content": "723baea0983b283eebd8331025a52eb13d5daaa7",
        "Surrounding Context": "\r\n\r\nipinfo.bat\r\n09dcedb5a6ad0ef5bbea4496486ba4e5\r\n723baea0983b283eebd8331025a52eb13d5daaa7\r\n277550c9d5771a13b65e90f5655150e365516215a714ffd3"
    },
    {
        "Indicator ID": 8,
        "Indicator Type": "SHA",
        "Indicator Content": "52f7e3437d83e964cb2fcc1175fad0611a12e26c",
        "Surrounding Context": "1\r\n\r\nipwho.bat\r\n0fd71d43c1f07d6a8fa73b0fa7beffa7\r\n52f7e3437d83e964cb2fcc1175fad0611a12e26c\r\n35ff76d763714812486a2f6ad656d124f3fcdfc4d16d49df"
    },
]
```

## Leaving venv
```deactivate```
