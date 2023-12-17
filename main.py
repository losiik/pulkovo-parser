from doc_workers.csv_worker import CSVWorker
from doc_workers.xlsx_worker import XLSXWorker
from get_page_data import get_page_data


from pars import Parser


page_data = get_page_data()

p = Parser(page_data=page_data)

passenger_traffic = p.extract_passenger_traffic()
numb_of_airlines = p.extract_numb_of_airlines()

csv_worker = CSVWorker()
csv_worker.write_to_file_numb_of_airlines(data=numb_of_airlines, file_path='csv_data/numb_of_airlines.csv')
csv_worker.write_to_file_passenger_traffic(data=passenger_traffic, file_path='csv_data/passenger_traffic.csv')
# df = csv_worker.file_to_df(file_path='csv_data/passenger_traffic.csv')

xlsx_worker = XLSXWorker()
xlsx_worker.write_to_file_numb_of_airlines(data=numb_of_airlines, file_path='xlsx_data/numb_of_airlines.xlsx')
xlsx_worker.write_to_file_passenger_traffic(data=passenger_traffic, file_path='xlsx_data/passenger_traffic.xlsx')
df = xlsx_worker.file_to_df(file_path='xlsx_data/passenger_traffic.xlsx')
print(df)

