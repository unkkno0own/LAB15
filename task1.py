import pandas as pd

def main():
    my_list = []

    n = int(input("Введіть кількість елементів у списку: "))
    for i in range(n):
        element = input("Введіть елемент списку: ")
        my_list.append(element)

    print("Початковий список:", my_list)

    left_element = input("Введіть елемент для додавання зліва: ")
    right_element = input("Введіть елемент для додавання справа: ")

    my_list.insert(0, left_element)
    my_list.append(right_element)

    print("Список після додавання елементів з обох кінців:", my_list)

    # Створення словника з даними
    data = {'Елементи': my_list}

    # Створення датафрейму
    df = pd.DataFrame(data)

    # Виведення датафрейму на екран
    print("\nДатафрейм:")
    print(df)

    # Агрегація та групування даних
    grouped_data = df.groupby('Елементи').size().reset_index(name='Кількість')

    # Виведення результатів групування
    print("\nРезультати групування:")
    print(grouped_data)

if __name__ == "__main__":
    main()

