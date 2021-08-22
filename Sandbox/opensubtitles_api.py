import requests

api_key = '71oaN2tPBlfq1uDPl643IzjVU2wAJHLd'
url = 'https://api.opensubtitles.com'
login_url = url + '/api/v1/login'
headers = {'Content-Type': 'multipart/form-data', 'Api-Key': api_key, 'Accept': 'application/json'}
response = requests.post(login_url, headers=headers, data={"username": "iberniak", "password": "Vamjik-wejwig-makko7"})

print(response.json()['token'])



search_url = url + '/api/v1/subtitles'
search_response = requests.get(search_url, headers=headers, data={'imdb_id': 'tt2543164', 'language': 'en'})


print(search_response.text)
