import collections
from datetime import date
from dateutil.relativedelta import *
from faker import Faker
from collections import namedtuple, Counter
from time import perf_counter
from functools import wraps

Faker.seed(1)
fake = Faker()


def get_fake_profiles(type, count):
    fake_profiles = []
    if type == 'namedtuple':
        profile = namedtuple('Profile', ['job', 'company', 'ssn', 'residence', 'current_location',
                                         'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate'])
        for _ in range(count):
            fake_profiles.append(profile(**fake.profile()))
    elif type == 'dict':
        for _ in range(count):
            fake_profiles.append(fake.profile())
    return fake_profiles


def get_largest_blood_group(collection, type):
    bg_counts = None
    if type == 'namedtuple':
        bg_counts = Counter(p.blood_group for p in collection)
    elif type == 'dict':
        bg_counts = Counter(p['blood_group'] for p in collection)
    return bg_counts.most_common()[0]


def get_oldest_birthdate(collection, type):
    oldest_birthdate = None
    if type == 'namedtuple':
        oldest_birthdate = min(
            collection, key=lambda a: a.birthdate).birthdate
    elif type == 'dict':
        oldest_birthdate = min(
            collection, key=lambda a: a['birthdate'])['birthdate']
    return oldest_birthdate


def get_average_age(collection, type):
    if type == 'namedtuple':
        return sum([relativedelta(date.today(), a.birthdate).years for a in collection])/len(collection)
    elif type == 'dict':
        return sum([relativedelta(date.today(), a['birthdate']).years for a in collection])/len(collection)


fake_profiles = get_fake_profiles('namedtuple', 10)
fake_profiles_dict = get_fake_profiles('dict', 2)


def get_average_time(n, func, *args, **kwargs):
    start = perf_counter()
    for _ in range(n):
        value = func(*args, **kwargs)
    avg_run_time = (perf_counter() - start)/n
    return avg_run_time


N = 1000000
for f in [get_largest_blood_group, get_oldest_birthdate, get_average_age]:
    print('testing:', f.__name__)
    t1 = get_average_time(N, f, fake_profiles, 'namedtuple')
    t2 = get_average_time(N, f, fake_profiles_dict, 'dict')

    if t1 < t2:
        print('dict is faster')
    else:
        print('named tuple is faster')
