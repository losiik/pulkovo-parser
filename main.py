from doc_workers.csv_worker import CSVWorker
from doc_workers.xlsx_worker import XLSXWorker
from get_page_data import get_page_data
from gen_grafics import (gen_grafic_passengers_per_month, gen_grafic_monthly_average_passengers,
                         gen_grafic_numb_of_airlines_per_year)


from pars import Parser


if __name__ == '__main__':
    page_data = get_page_data()

    p = Parser(page_data=page_data)

    passenger_traffic = p.extract_passenger_traffic()
    numb_of_airlines = p.extract_numb_of_airlines()

    csv_worker = CSVWorker()
    csv_worker.write_to_file_numb_of_airlines(data=numb_of_airlines, file_path='csv_data/numb_of_airlines.csv')
    csv_worker.write_to_file_passenger_traffic(data=passenger_traffic, file_path='csv_data/passenger_traffic.csv')
    df1 = csv_worker.file_to_df(file_path='csv_data/passenger_traffic.csv')
    df2 = csv_worker.file_to_df(file_path='csv_data/numb_of_airlines.csv')

    # Алтернативное решение для работы с xlsx
    # xlsx_worker = XLSXWorker()
    # xlsx_worker.write_to_file_numb_of_airlines(data=numb_of_airlines, file_path='xlsx_data/numb_of_airlines.xlsx')
    # xlsx_worker.write_to_file_passenger_traffic(data=passenger_traffic, file_path='xlsx_data/passenger_traffic.xlsx')
    # df1 = xlsx_worker.file_to_df(file_path='xlsx_data/passenger_traffic.xlsx')
    # df2 = xlsx_worker.file_to_df(file_path='xlsx_data/numb_of_airlines.xlsx')

    gen_grafic_passengers_per_month(df1)
    gen_grafic_monthly_average_passengers(df1)
    gen_grafic_numb_of_airlines_per_year(df2)
