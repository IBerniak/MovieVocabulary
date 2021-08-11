from vocabulary_class import VocabularyOfMovie

movie = VocabularyOfMovie('Friends', 2005, '/Users/iliia.berniak/Desktop/friends./friends_s01e01_720p_bluray_x264-sujaidr.srt')


print(movie.all_words)

print(movie.all_words['hammer'].forms)