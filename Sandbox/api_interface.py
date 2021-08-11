import requests

# xml_login = '''
# <methodCall>
#  <methodName>LogIn</methodName>
#  <params>
#   <param>
#    <value><string></string></value>
#   </param>
#   <param>
#    <value><string></string></value>
#   </param>
#   <param>
#    <value><string>en</string></value>
#   </param>
#   <param>
#    <value><string>TemporaryUserAgent</string></value>
#   </param>
#  </params>
# </methodCall>
# '''
headers = {'Content-Type': 'application/xml', 'useragent': 'TemporaryUserAgent'}

response = requests.post("http://api.opensubtitles.org/xml-rpc", data=xml_login, headers=headers)

print(response.text)

# The requiered information here: https://opensubtitles.stoplight.io/docs/opensubtitles-api/open_api.json/paths/~1api~1v1~1subtitles/get and https://trac.opensubtitles.org/projects/opensubtitles/wiki/DevReadFirst
