import matplotlib.pyplot as plt
import pandas as pd


# График зависимости пассажиров от месяца по годам
def gen_grafic_passengers_per_month(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    for year in df['Year'].unique():
        subset = df[df['Year'] == year]
        plt.plot(subset['Month'], subset['Passenger Count'], label=str(year))

    plt.xlabel('Месяц')
    plt.ylabel('Количество пассажиров')
    plt.title('Зависимость пассажиров от месяца по годам')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.savefig('grafics_imgs/passengers_per_month.png')


# График среднего значения пассажиров для каждого месяца
def gen_grafic_monthly_average_passengers(df: pd.DataFrame):

    monthly_avg = df.groupby('Month')['Passenger Count'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(monthly_avg.index, monthly_avg.values, color='skyblue')
    plt.xlabel('Месяц')
    plt.ylabel('Среднее количество пассажиров')
    plt.title('Среднее значение пассажиров для каждого месяца')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('grafics_imgs/monthly_average_passengers.png')


# График количества авиакомпаний для каждого года
def gen_grafic_numb_of_airlines_per_year(df: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    plt.plot(df['Year'], df['Number of Airlines'], marker='o', linestyle='-')
    plt.xlabel('Год')
    plt.ylabel('Количество авиакомпаний')
    plt.title('Количество авиакомпаний для каждого года')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('grafics_imgs/airlines_per_year.png')
