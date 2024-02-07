def prefix_similarity(arr1, arr2):
    min_length = min(len(arr1), len(arr2))
    similarity_count = 0
    for i in range(min_length):
        if arr1[i] == arr2[i]:
            similarity_count += 1
        else:
            break

    return similarity_count

try:
    n: int = int(input("Введите кол-во массивов: "))
except ValueError:
    raise ValueError("Вы ввели не число")
arrays: list[list[int]] = []

i: int
for i in range(n):
    size: int = int(input(f"Размер массива {i}: "))
    elements: list[int] = list(map(int, input("Элементы массива (num1 num2 num3...numN): ").split()))
    if len(elements) != size:
        raise ValueError("Длина не совпадает!")
    arrays.append(elements)

total_similarity_sum: int = 0

i: int
j: int
for i in range(n):
    for j in range(i + 1, n):
        similarity = prefix_similarity(arrays[i], arrays[j])
        total_similarity_sum += similarity

print(total_similarity_sum)
