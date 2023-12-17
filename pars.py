from bs4 import BeautifulSoup
from typing import Dict


class Parser:
    def __init__(self, page_data: str):
        self.soup = BeautifulSoup(page_data, "html.parser")
        self.allTabs = self.soup.findAll(class_='grath_tab')

    # Пассажиропоток аэропорта
    def extract_passenger_traffic(self) -> Dict[int, Dict[str, int]]:
        init_year = 2019
        response = {}

        for i in range(8):
            months = self.allTabs[i].findAll(class_='grath_c_val c_top')
            traffic = self.allTabs[i].findAll(class_='n')

            month_traffic_dict = {}
            for j in range(12):
                month_traffic_dict[months[j].text] = int(traffic[j].text.replace(' ', ''))

            response[init_year] = month_traffic_dict
            init_year -= 1

        return response

    # Количество авиакомпаний
    def extract_numb_of_airlines(self) -> Dict[int, int]:
        airlines_per_year = {}

        years_amount_list = self.allTabs[12].findAll(class_='grath_c_val')
        for i in range(0, len(years_amount_list), 2):
            airlines_per_year[int(years_amount_list[i].text)] = int(years_amount_list[i + 1].text)

        return airlines_per_year
