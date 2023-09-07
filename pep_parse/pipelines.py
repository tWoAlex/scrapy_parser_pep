import csv
from pathlib import Path
from collections import Counter

from datetime import datetime


BASE_DIR = Path(__file__).parent.parent.joinpath('results')


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counters = Counter()

    def process_item(self, item, spider):
        self.status_counters.update((item['status'],))
        return item

    def close_spider(self, spider):

        timestamp = datetime.utcnow()
        timestamp = timestamp.isoformat().replace(':', '-')
        timestamp = timestamp[:timestamp.index('.')]

        output_file = BASE_DIR.joinpath(f'status_summary_{timestamp}.csv')

        with open(output_file, 'w') as file:
            writer = csv.writer(file, dialect='unix')

            writer.writerow(('status', 'count'))
            writer.writerows(sorted(list(self.status_counters.items())))
            writer.writerow(('Total', sum(self.status_counters.values())))
