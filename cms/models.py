from django.db import models


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()
    def getWithImpressionCount(self):
      books = Book.objects.all().order_by('id')
      for book in books:
        book.impressionCount = Impression.objects.filter(book_id=book.id).count()
      return books

class Book(models.Model):
  """書籍"""
  objects = BookManager()
  name = models.CharField('書籍名', max_length=255)
  publisher = models.CharField('出版社', max_length=255, blank=True)
  page = models.IntegerField('ページ数', blank=True, default=0)
  impressionCount = 0

  def __str__(self):
    return self.name


class Impression(models.Model):
  """感想"""
  book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
  comment = models.TextField('コメント', blank=True)

  def __str__(self):
    return self.comment
