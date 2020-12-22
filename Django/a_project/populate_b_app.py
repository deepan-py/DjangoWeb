from faker import Faker
from b_app.models import AccessRecord, Topic, Webpage
import random
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_project.settings')
django.setup()

# !fake pop script


fakeGen = Faker()
topics = ['search', 'social', 'marketplace', 'news', 'games']


def add_topic():
    #  get_or_create() -- this will help to get or create models if not exist
    #  get_or_create() -- returns tuple the 1st element is refence the model instance
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    print(t)
    return t


def populate(N=5):
    for i in range(N):
        top = add_topic()
        fake_url = fakeGen.url()
        fake_date = fakeGen.date()
        fake_name = fakeGen.company()

        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating Script")
    populate()
    print("populate complete")
