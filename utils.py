import json
import re
from pathlib import PosixPath, WindowsPath
from typing import Any, Generator


def clean_split(
    text: str, 
    seps: str, 
    verbose: bool = False
) -> Generator[str | Any, None, None]:
    """Split string, strip and clean empty part
    
    text (str): string to split
    sep (str): separator"""

    if verbose is True:
        print(seps, re.split(seps, text))

    for part in re.split(seps, text):
        if (item := part.strip()):
            yield item


def load_text(
    file_path: str | PosixPath | WindowsPath, 
    is_list: bool = False
) -> Generator[str | Any, None, None] | str:
    with open(file_path, 'r', encoding='utf-8') as fr:
        fr_read = fr.read().strip()
        
    if is_list is True:
        return clean_split(fr_read, '\n')
    else:
        return fr_read
    

def write_json(data, file_path: str | PosixPath | WindowsPath):
    with open(file_path, 'w', encoding='utf-8', errors='surrogateescape') as fw:
        json.dump(data, fw, indent=4, ensure_ascii=False)