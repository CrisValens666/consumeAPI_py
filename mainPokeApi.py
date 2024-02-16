
import requests, json

def get_pokemon(url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset': offset} if offset else {}

    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        # content = response.content 
        # print(content)
        
        payload = response.json()
        resulsts = payload.get('results',[])
        if resulsts:
            for pokemon in resulsts:
                name = pokemon['name']
                print(name)
                
        next = input("Continua? [Y/N]: ").lower()
        if next == 'y':
            get_pokemon(offset=offset+20)
        
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemon()
    