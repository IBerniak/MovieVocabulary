from django.db import models


class VocabularyWord(models.Model):
    base_form = models.CharField(max_length=128, primary_key=True, unique=True)
    is_known = [('Kn', 'I know this word'), ('Un', 'A new word for me')]


class MovieVocabulary(models.Model):
    words = models.ManyToManyField(VocabularyWord)


class Movie(models.Model):
      title = models.CharField(
        max_length=128,
        primary_key=True,
        help_text='Put here the title of the movie you need to analize',
        )

      year = models.PositiveIntegerField(
        blank=True,
        help_text='Put here the year of that movie (optional)',
        )

      vocabulary = models.ForeignKey(MovieVocabulary, on_delete=models.CASCADE)

      def __str__(self):
          return self.title





# class Profile(models.Model):
#     name = models.CharField(max_length=128, primary_key=True, unique=True)
#     email = models.EmailField()
#
#

#

#
#

#
# class PersonVocabulary(models.Model):
#     words = models.ManyToManyField(VocabularyWord)
