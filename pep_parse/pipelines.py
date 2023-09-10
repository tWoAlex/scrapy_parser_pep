import csv
from collections import Counter
from datetime import datetime

from pep_parse.settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counters = Counter()

    def process_item(self, item, spider):
        self.status_counters[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR.joinpath(RESULTS_DIR)
        results_dir.mkdir(exist_ok=True)
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')
        output_file = results_dir.joinpath(f'status_summary_{timestamp}.csv')
        with open(output_file, 'w') as file:
            writer = csv.writer(file, dialect=csv.unix_dialect(),
                                quoting=csv.QUOTE_NONE)
            writer.writerows(
                [
                    ('status', 'count'),
                    *sorted(list(self.status_counters.items())),
                    ('Total', sum(self.status_counters.values())),
                ]
            )
