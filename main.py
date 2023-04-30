from collections import Counter

from utils import load_text, write_json


def main():
    text_file = 'mobile_specific.txt'
    ubo_stats = dict()
    for line in load_text(text_file, is_list=True):
        if line.startswith('!'):
            continue

        ubo_filters = (line_split := line.split('##'))[1].split(',')
        domains: list[str] = line_split[0].split(',')
        
        for ubo_filter in ubo_filters:
            if ubo_filter not in ubo_stats:
                ubo_stats[ubo_filter] = {
                    'number': len(domains),
                    'domain': ','.join(sorted(domains))
                }
            else:
                current_domain = ubo_stats[ubo_filter]['domain'].split(',')
                domains.extend(current_domain)

                ubo_stats[ubo_filter]['domain'] = ','.join(sorted(domains))
                ubo_stats[ubo_filter]['number'] = len(domains)

    ubo_stats = dict(sorted(ubo_stats.items(), key=lambda item: item[1]['number'], reverse=True))
    write_json(ubo_stats, 'stats.json')


if __name__ == "__main__":
    main()