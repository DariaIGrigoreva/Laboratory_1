
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
len_players = len(list_players)
print('Общее количество игроков в списке:',  len_players)

middle_index = len_players // 2

left_team = list_players[:middle_index]  # list_players[:2]
right_team = list_players[middle_index:]  # list_players[2:]

print(left_team)
print(right_team)
