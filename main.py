import requests

def get_all_heroes():
    base_url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(f'{base_url}/all.json')
    res = response.json()
    return res

def get_hero(id_hero):
    base_url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(f'{base_url}/id/{id_hero}.json')
    res = response.json()
    return res

def get_intel(id_hero):
    base_url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(f'{base_url}/powerstats/{id_hero}.json')
    res = response.json()
    return res

def find_hero(names):
    res = get_all_heroes()
    heroes = []
    for hero in res:
        if hero['name'] in names:
            heroes.append({'name' : hero['name'], 'id' : hero['id'], 'intel' : 0})

    for hero in heroes:
        res = get_intel(hero['id'])
        hero['intel'] = res['intelligence']

    return heroes

def smartest_hero(names):
    heroes = find_hero(names)
    heroes.sort(key=lambda hero: hero['intel'], reverse=True)
    print(f'Среди героев: {", ".join(names)}, умнейшим является {heroes[0]["name"]}. Его интеллект составляет {heroes[0]["intel"]} единиц.')



if __name__ == '__main__':
    smartest_hero(['Captain America', 'Hulk', 'Thanos'])