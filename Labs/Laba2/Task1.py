import os


# 1. Чтение файла с данными с помощью open()
def read_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for item in line.strip().split():
                try:
                    data.append(float(item))
                except ValueError:
                    continue
    return data


def custom_sort(arr):
    sorted_arr = list(arr)
    n = 0
    for _ in sorted_arr:
        n += 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


# 2. Функция расчета статистических показателей с нуля
def calculate_statistics(data):
    if not data:
        return {'mean': 0, 'max': 0, 'min': 0, 'median': 0}

    total_sum = 0
    count = 0
    current_max = data[0]
    current_min = data[0]

    for val in data:
        total_sum += val
        count += 1
        if val > current_max:
            current_max = val
        if val < current_min:
            current_min = val

    mean_val = total_sum / count

    sorted_data = custom_sort(data)
    if count % 2 != 0:
        median_val = sorted_data[count // 2]
    else:
        median_val = (sorted_data[count // 2 - 1] + sorted_data[count // 2]) / 2

    return {
        'mean': mean_val,
        'max': current_max,
        'min': current_min,
        'median': median_val
    }


# 3. Запись файла с результатами через open() и write()
def write_results(original_filename, stats, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(f"{original_filename}\n")
        file.write(f"mean: {stats['mean']}\n")
        file.write(f"max: {stats['max']}\n")
        file.write(f"min: {stats['min']}\n")
        file.write(f"median: {stats['median']}\n")


# 4. Выполнить обработку всех файлов и получить список всех файлов в папке
if __name__ == "__main__":
    directory = 'data'
    if os.path.exists(directory):
        for file in os.listdir(directory):
            if file.startswith("yc-") and file.endswith(".dat"):
                input_path = os.path.join(directory, file)
                data = read_data(input_path)

                if data:
                    stats = calculate_statistics(data)
                    out_filename = f"out_{file}"
                    out_path = os.path.join(directory, out_filename)
                    write_results(file, stats, out_path)




# if __name__ == "__main__":
#     directory = 'data'
#     if os.path.exists(directory):
#         print(f"Поиск файлов в папке: '{directory}'...")
#         for file in os.listdir(directory):
#             if file.startswith("yc-") and file.endswith(".dat"):
#                 input_path = os.path.join(directory, file)
#                 data = read_data(input_path)
#
#                 if data:
#                     stats = calculate_statistics(data)
#                     out_filename = f"out_{file}"
#                     out_path = os.path.join(directory, out_filename)
#                     write_results(file, stats, out_path)
#
#                     # Вывод данных в консоль
#                     print(f"\nОбработан файл: {file}")
#                     print(f"Среднее: {stats['mean']}")
#                     print(f"Максимум: {stats['max']}")
#                     print(f"Минимум: {stats['min']}")
#                     print(f"Медиана: {stats['median']}")
#                     print(f"Результат сохранен в: {out_filename}")
#     else:
#         print(f"Папка '{directory}' не найдена. Создайте ее и добавьте файлы данных.")