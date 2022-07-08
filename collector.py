# run scripts to collect goofy quotes that will mix and match with an ending quote
# run scripts to compile images


from bing_image_downloader import downloader
from PIL import Image
import os

search_types = ['Sad photo', 'happy photo', 'rainy photo', 'clouds', 'earth', 'inspirational backgrounds no words']



if input('collect images?  (y/n)') == 'y':
    for search in search_types:
        downloader.download(search, limit=20, output_dir='images',
        adult_filter_off=False,force_replace=True ,timeout=60)
# i want die
elif input('resize images? (y/n)') == 'y':

    for directory in os.listdir(os.getcwd() + '\images'):
        for image in os.listdir(os.getcwd() + '\images\\' + directory):
            full_dir = f'{os.getcwd()}\images\\{directory}\\{image}'
            if full_dir.find('PNG') != -1 and full_dir.find('JPG') != -1:
                os.remove(full_dir)
                pass
            with Image.open(full_dir) as im:
                resized = im.resize((500, 500))
                try:
                    os.remove(full_dir)
                    resized.save(full_dir)
                except (PermissionError):
                    pass


