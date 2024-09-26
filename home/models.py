from django.db import models

# Create your models here.



class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='books_photos/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Readers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Borrowed_books(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    reader = models.ForeignKey(Readers, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} - {self.reader}"