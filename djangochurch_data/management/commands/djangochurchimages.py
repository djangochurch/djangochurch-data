import os.path

from blanc_basic_assets.models import Image
from django.apps import apps
from django.core.files import File
from django.core.management.base import BaseCommand


IMAGE_LIST = [
    (1, 'remember.jpg'),
    (2, 'sample-image-1.jpg'),
    (3, 'sample-image-2.jpg'),
    (4, 'sample-image-3.jpg'),
    (5, 'sample-image-4.jpg'),
]


class Command(BaseCommand):
    help = 'Load Django Church images'

    def handle(self, directory=None, *args, **options):
        data_app = apps.get_app_config('djangochurch_data')
        image_dir = os.path.join(data_app.path, 'images')

        for image_id, image_name in IMAGE_LIST:
            self.stdout.write('Importing: %s' % (image_name,))
            image = Image.objects.get(id=image_id)

            image_file = os.path.join(image_dir, image_name)

            with open(image_file, 'rb') as f:
                image.file.save(image_name, File(f), save=False)
