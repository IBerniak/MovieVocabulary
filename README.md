# MovieVocabulary
The web application for analyzing a vocabulary of different movies

Researching and developing under the order of the English language school

With a user request (title of a movie) the application searchs for subtitles and analyzes them to find unique vocabulary in the base word form (lemma),
shows that vocabulary to the user in checkboxes where he or she can mark known words (such words is writing down into the user's profile),
after this operation the application gives a list of unknown words of the movie, so the user can learn them to watch a movie with a comfortable knowledge.

The basic operations:
1. searching subtitle for a requested movie (first in the application database (ready-to-use vocabulary), further in opensubtitles.org)
2. downloading .srt files through API of opensubtitles.org
3. extracting text from the file
4. analyzing the text to make a complete vocabulary
5. comparing with a saved in a profile vocabulary to reduce known words
6. showing remaining vocabulary
7. saving checked known words
8. showing (giving) the list of unknown words
9. saving the vocabulary of movie for the future using

Technologies, frameworks and external libraries:
1. Python 3.x
2. Django 2.2
3. pysrt -- to parse .srt file
4. nltk -- to analyze text
5. opensubtitles.org API


Author Iliia Berniak
