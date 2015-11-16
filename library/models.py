from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID=models.AutoField(primary_key = True)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Country=models.CharField(max_length=20)
    class Meta:
        db_table = 'Author'
class Book(models.Model):
    ISBN=models.BigIntegerField(primary_key = True)
    Title=models.CharField(max_length=20)
    AuthorID = models.ForeignKey(Author, null=True)
    Publisher=models.CharField(max_length=20)
    PublishDate=models.DateField()
    Price=models.IntegerField()
    class Meta:
        db_table = 'Book'
 
