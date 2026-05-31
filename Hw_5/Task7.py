nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]

flattened = [
    num for sublist in nice_list for inner_list in sublist for num in inner_list
]

print(f"Ответ: {flattened}")