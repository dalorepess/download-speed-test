import time
import requests

url = input("Введите URL адрес:\n").strip()

total_time = 0.0
total_bytes = 0

for i in range(10):
    start_time = time.perf_counter()

    response = requests.get(url)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    size_bytes = len(response.content)

    total_time += elapsed_time
    total_bytes += size_bytes

    print(f"Запрос {i + 1} из 10: {elapsed_time:.3f} с, {size_bytes} байт")

average_time = total_time / 10
speed_mbps = total_bytes * 8 / total_time / 1_000_000

print(f"\nСреднее время запроса: {average_time:.3f} с")
print(f"Общий объём: {total_bytes} байт")
print(f"Скорость скачивания: {speed_mbps:.2f} Мбит/с")
