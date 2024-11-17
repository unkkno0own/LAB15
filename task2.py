import pandas as pd
import matplotlib.pyplot as plt
import calendar

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

try:
    # Читання CSV файлу
    fixed_df = pd.read_csv('bicycle.csv',
                           sep=',', encoding='latin1',
                           parse_dates=['Date'],
                           dayfirst=True,
                           index_col='Date')

    # Додавання стовпця для місяця
    fixed_df['Month'] = pd.DatetimeIndex(fixed_df.index).month

    # Видалення спеціальних символів у назвах стовпців
    fixed_df.columns = fixed_df.columns.str.replace('[^\w\s]', '')

    # Заповнення пропущених значень нулями
    fixed_df = fixed_df.fillna(0)

    print(fixed_df.head(3))

    # Побудова графіку
    ax = fixed_df.plot()
    ax.legend(loc='upper left')
    plt.title('Використання велодоріжок по місяцях')
    plt.xlabel('Дата')
    plt.ylabel('Кількість велосипедистів')
    plt.show()

    # Групування по місяцях та підсумування значень
    monthly_counts = fixed_df.groupby('Month').sum()

    # Знаходимо найбільш популярний місяць
    most_popular_month = monthly_counts.sum(axis=1).idxmax()  # idxmax() для визначення місяця з найбільшим використанням
    print(f"Найпопулярніший місяць для велосипедистів: {calendar.month_name[most_popular_month]}")

except pd.errors.DtypeWarning as e:
    print(f"Виникла помилка: {e}")
