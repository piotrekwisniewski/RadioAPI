from django.core.management.base import BaseCommand
from radio.models import Artist, Hit
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed the database with initial artists and hits'

    def handle(self, *args, **kwargs):
        Hit.objects.all().delete()
        Artist.objects.all().delete()

        # Creating sample artits
        artists = [
            Artist.objects.create(first_name="Foo", last_name="Fighters"),
            Artist.objects.create(first_name="Sam", last_name="Fender"),
            Artist.objects.create(first_name="Coma",),
        ]

        # Creating 20 sample tracks
        for i in range(1, 21):
            title = f"Track {i}"
            artist = artists[i % 3]
            Hit.objects.create(
                title=title,
                artist=artist,
                title_url=slugify(title),
            )
        self.stdout.write(self.style.SUCCESS('Database populated!'))
