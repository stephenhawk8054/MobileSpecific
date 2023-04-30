from collections import Counter

from utils import load_text, write_json


def main():
    text_file = 'mobile_specific.txt'
    ubo_filters = []
    for line in load_text(text_file, is_list=True):
        if line.startswith('!'):
            continue

        ubo_filters.append(line.split('##')[1])

    write_json(dict(Counter(ubo_filters).most_common()), 'stats.json')


if __name__ == "__main__":
    main()