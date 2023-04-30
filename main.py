from utils import load_text, write_json


def main():
    stats = dict()
    for line in load_text('mobile_specific.txt', is_list=True):
        if line.startswith('!'):
            continue

        domains = set((line_split := line.split('##'))[0].split(','))
        for filter in line_split[1].split(','):
            if filter in stats:
                domains.union(set(stats[filter]['domain'].split(',')))

            stats[filter] = {
                'number': len(domains),
                'domain': ','.join(sorted(domains))
            }

    stats = dict(sorted(stats.items(), key=lambda item: item[1]['number'], reverse=True))
    write_json(stats, 'stats.json')


if __name__ == "__main__":
    main()