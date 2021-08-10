import requests


response = requests.get("https://api.opensubtitles.com/api/v1/subtitles", headers={"Api-Key": ""},
 params={
  "user": {
    "allowed_downloads": 100,
    "level": "Sub leecher",
    "user_id": 66,
    "ext_installed": False,
    "vip": False
  },
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEOU5aaWUyVjhWOU1hTnJVZWVvcEEwWUNoWEt6Wkx3NiIsImV4cCI6MTYwNDM1ODAwMH0.sMibjAFnkcs-HJ4zhdCwBeGrZ_UvzMbgl5NxYV2uALM",
  "status": 200
})

data = response.json()

print(data)

# The requiered information here: https://opensubtitles.stoplight.io/docs/opensubtitles-api/open_api.json/paths/~1api~1v1~1subtitles/get and https://trac.opensubtitles.org/projects/opensubtitles/wiki/DevReadFirst
