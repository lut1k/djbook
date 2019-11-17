from django.db import models
from django.urls import reverse


# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name


class Person(models.Model):
    SHIRT_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("S", "Large")
    )
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    birth_date = models.DateField()

    def __str__(self):
        return "{}, {}".format(self.name, self.last_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('news-persons', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        if self.name == "Yolo":
            return
        else:
            super(Person, self).save(*args, **kwargs)

    def baby_boomer_status(self):
        """
        Returns the person's baby-boomer status
        """
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    def _get_full_name(self):
        """Returns the person's full name
        """
        return "{} {}".format(self.name, self.last_name)
    full_name = property(_get_full_name)


class OrderedPerson(Person):
    """
    Прокси-модель для сортировки класса Person.
    """
    class Meta:
        proxy = True
        ordering = ["last_name"]


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    """Промежуточная модель. Эту промежуточную модель можно указать в поле
    ManyToManyField используя аргумент through,
    который указывает на промежуточную модель."""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return "{}, {}".format(self.person, self.group)


class MyFiles(models.Model):
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.upload