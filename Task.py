import csv

try:
    # Відкриваємо CSV файл для зчитування
    with open('ЛР_11.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Ініціалізуємо змінні для збереження року з найменшою та найбільшою популяцією
        min_year = None
        min_population = float('inf')
        max_year = None
        max_population = float('-inf')

        # Зчитуємо дані з файлу та знаходимо рік з найменшою та найбільшою популяцією
        for row in reader:
            population = int(row['Value'])
            year = row['Time']
            if population < min_population:
                min_population = population
                min_year = year
            if population > max_population:
                max_population = population
                max_year = year

        # Виводимо результати
        min_result = f"Year: {min_year} Min Population: {min_population};"
        max_result = f"Year: {max_year} Max Population: {max_population};"
        print(min_result)
        print(max_result)

        # Записуємо результати у новий .csv файл
        with open('population_min_max_years.csv', mode='w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow([min_result])
            writer.writerow([max_result])

except FileNotFoundError:
    print("Файл не знайдено.")

except Exception as e:
    print("Сталася помилка:", e)
