import os
import sys
from chardet.universaldetector import UniversalDetector

FOLDER = "submits (1)"

smth_to_find = ' '.join(sys.stdin.read().split())
for folder in os.listdir(FOLDER):
    for py_file in os.listdir(f"{FOLDER}/{folder}"):
        try:
            with open(f"{FOLDER}/{folder}/{py_file}", encoding='utf-8') as file:
                text = file.read()
        except UnicodeDecodeError:
            detector = UniversalDetector()
            with open(f"{FOLDER}/{folder}/{py_file}", 'rb') as fh:
                for line in fh:
                    detector.feed(line)
                    if detector.done:
                        break
                detector.close()
            try:
                with open(f"{FOLDER}/{folder}/{py_file}", encoding=detector.result['encoding']) as file:
                    text = file.read()
            except Exception as e:
                print(e.__class__.__name__, e)

        text = ' '.join(text.split())
        if smth_to_find in text:
            print(folder)
