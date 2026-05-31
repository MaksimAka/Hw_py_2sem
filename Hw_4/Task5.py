violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.24],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs = int(input("Сколько песен выбрать? "))
total_time = 0

for i in range(num_songs):
    song_name = input(f"Название {i + 1}-й песни: ")
    for song in violator_songs:
        if song[0] == song_name:
            total_time += song[1]
            break

print(f"Общее время звучания песен: {round(total_time, 2)} минуты")