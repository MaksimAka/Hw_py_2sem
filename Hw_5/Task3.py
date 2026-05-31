import random

team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(team1[i], team2[i]) for i in range(20)]

print(f"Первая команда: {team1}")
print(f"Вторая команда: {team2}")
print(f"Победители тура: {winners}")