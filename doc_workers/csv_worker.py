from .document_worker import DocumentWorker
import csv
from typing import Dict


class CSVWorker(DocumentWorker):
    def write_to_file_numb_of_airlines(self, data: Dict[int, int], file_path: str):
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(self.HEADER_NUMB_OF_AIRLINES)
            for year, num_airlines in data.items():
                csv_writer.writerow([year, num_airlines])

    def write_to_file_passenger_traffic(self, data: Dict[int, Dict[str, int]], file_path: str):
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(self.HEADER_PASSENGER_TRAFFIC)

            for year, months_data in data.items():
                for month, passengers in months_data.items():
                    csv_writer.writerow([year, month, passengers])
