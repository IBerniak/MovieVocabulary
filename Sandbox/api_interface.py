import requests
import xml_parser
import base64
import gzip
import io
from vocabulary_class import VocabularyOfMovie

xml_login = '''
<methodCall>
 <methodName>LogIn</methodName>
 <params>
  <param>
   <value><string>iberniak</string></value>
  </param>
  <param>
   <value><string>#1dno54uab</string></value>
  </param>
  <param>
   <value><string>en</string></value>
  </param>
  <param>
   <value><string>Movie Vocabulary v1</string></value>
  </param>
 </params>
</methodCall>
'''
headers = {'Content-Type': 'application/xml', 'Accept': 'application/json', 'useragent': 'Movie Vocabulary v1'}

response = requests.post("http://api.opensubtitles.org/xml-rpc", data=xml_login, headers=headers)
parsed_response = xml_parser.XmlParser(response.text)
parsed_response.print()

token = parsed_response.find('token')

movie = 'Arrival'

xml_search = '''
 <methodCall>
 <methodName>SearchSubtitles</methodName>
  <params>
   <param>
    <value><string>{a}</string></value>
   </param>
   <param>
    <struct>
    <struct>
    <member>
    <name>sublanguageid</name>
    <value><string>eng</string></value>
    </member>
    <member>
    <name>query</name>
    <value><string>{b}</string></value>
    </member>
    </struct>
    </struct>
   </param>
   <param>
     <struct>
     <member>
     <name>limit</name>
     <value><int>1</int></value>
     </member>
     </struct>
   </param>
  </params>
 </methodCall>
'''.format(a = token, b = movie)

# array SearchSubtitles( $token, array(array('sublanguageid' => $sublanguageid, 'moviehash' => $moviehash, 'moviebytesize' => $moviesize, imdbid => $imdbid, query => 'movie name', "season" => 'season number', "episode" => 'episode number', 'tag' => tag ),array(...)), array('limit' => 500))

response = requests.post("http://api.opensubtitles.org/xml-rpc", data=xml_search, headers=headers)
search_response = xml_parser.XmlParser(response.text)
search_response.print()
imdb = 2543164
movie_id = search_response.find('IDSubtitleFile')

download_request = '''
<methodCall>
 <methodName>DownloadSubtitles</methodName>
 <params>
  <param>
   <value><string>{a}</string></value>
  </param>
  <param>
  <struct>
  <member>
  <name>IDSubtitleFile</name>
  <value><int>{b}</int></value>
  </member>
  </struct>
  </param>
 </params>
</methodCall>
'''.format(a = token, b = movie_id)
response = requests.post("http://api.opensubtitles.org/xml-rpc", data=download_request, headers=headers)
download_response = xml_parser.XmlParser(response.text)
download_response.print()

data = download_response.result_dict['params'][1]['struct']['data']
data = base64.b64decode(data)
data = gzip.decompress(data)
data = str(data)
# file = io.StringIO(data)
vocabulary = VocabularyOfMovie(movie, 2016, data)
print(vocabulary)



# The requiered information here: https://opensubtitles.stoplight.io/docs/opensubtitles-api/open_api.json/paths/~1api~1v1~1subtitles/get and https://trac.opensubtitles.org/projects/opensubtitles/wiki/DevReadFirst


# The requiered information here: https://opensubtitles.stoplight.io/docs/opensubtitles-api/open_api.json/paths/~1api~1v1~1subtitles/get and https://trac.opensubtitles.org/projects/opensubtitles/wiki/DevReadFirst
