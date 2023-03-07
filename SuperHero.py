import requests

def heroes_list(needed_heroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    heroes = response.json()
    stats_dict = {}
    int_points = []
    for row in heroes:
        stats = row['powerstats']['intelligence']
        name_hero = row['name']
        if name_hero in needed_heroes:
            int_points.append(stats)
            if stats not in stats_dict:
                stats_dict.setdefault(stats, [name_hero])
            else:    
                stats_dict[stats].append(name_hero)

    smart_hero = ', '.join(stats_dict[max(int_points)])
    return print(f'Самый умный герой с интелектом {max(int_points)} - {smart_hero}')


if __name__ == '__main__':
    heroes_list(['Hulk', 'Captain America', 'Thanos'])