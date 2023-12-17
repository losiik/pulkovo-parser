from .document_worker import DocumentWorker
from openpyxl import Workbook
from typing import Dict


class XLSXWorker(DocumentWorker):
    def write_to_file_numb_of_airlines(self, data: Dict[int, int], file_path: str):
        wb = Workbook()
        ws = wb.active
        ws.append(self.HEADER_NUMB_OF_AIRLINES)

        for year, num_airlines in data.items():
            ws.append([year, num_airlines])

        wb.save(file_path)

    def write_to_file_passenger_traffic(self, data: Dict[int, Dict[str, int]], file_path: str):
        wb = Workbook()
        ws = wb.active
        ws.append(self.HEADER_PASSENGER_TRAFFIC)

        for year, months_data in data.items():
            for month, passengers in months_data.items():
                ws.append([year, month, passengers])

        wb.save(file_path)
