import pandas as pd


class DocumentWorker:
    def __init__(self):
        self.HEADER_NUMB_OF_AIRLINES = ['Year', 'Number of Airlines']
        self.HEADER_PASSENGER_TRAFFIC = ['Year', 'Month', 'Passenger Count']

    def file_to_df(self, file_path: str) -> pd.DataFrame:
        if '.csv' in file_path:
            return self._create_df_from_csv(file_path)
        if '.xlsx' in file_path:
            return self._create_df_from_xlsx(file_path)

    def _create_df_from_csv(self, csv_file: str) -> pd.DataFrame:
        df = pd.read_csv(csv_file)
        return df

    def _create_df_from_xlsx(self, xlsx_file: str) -> pd.DataFrame:
        df = pd.read_excel(xlsx_file)
        return df
