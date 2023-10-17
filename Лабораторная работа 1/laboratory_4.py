users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
len_users = len(users)  #Общее количество
set_users = set(users)  #Уникальные посещения
len_set_users = len(set_users)

describe = {
    "Общее количество": len_users,
    "Уникальные посещения": len_set_users,
}
print(describe)
