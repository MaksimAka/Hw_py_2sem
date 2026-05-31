films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо']

count = int(input("Сколько фильмов хотите добавить? "))
fav_films = []

for _ in range(count):
    film = input("Введите название фильма: ")
    if film in films:
        fav_films.append(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

print("Ваш список любимых фильмов:", ", ".join(fav_films))