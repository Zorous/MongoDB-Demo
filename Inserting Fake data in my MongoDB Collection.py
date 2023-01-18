# importing module
from pymongo import MongoClient
import faker
from faker import Faker
import time

f=faker.Faker(['fr_FR'])

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient('localhost', 27017)

# Access database
mydatabase = client['Players']

# Access collection of the database
mycollection = mydatabase['PlayersData']
words = [
        ['football','True'],
        ['Muay Thai','False'],
        ['Baseball','False'],
        ['Basket-ball','True'],
        ['Handball','True'],
        ['Athletisme','True'],
        ['box','True'],
        ['Cyclisme','True'],
        ['Judo','True'],
        ['Natation','True'],
        ['Tenis','False']]
genre=['homme','femme']
while True:
    data = []
    start = time.time()
    for i in range(1,100000):
        #while True:
        v=f.words(1,words,True)
        s=f.words(1,genre,True)
        values={
            "nom":f.first_name(),
            "prenom":f.last_name(),
            "genre":s[0],
            "nbMedailles": f.pyint(0,10),
            "sport": {
                "description":v[0][0],
                "olympique":v[0][0]
            }
        }
        data.insert(0,values)
        #record = mydatabase.PlayersData.insert_one(values)
    start1 = time.time()
    record = mydatabase.x   .insert_many(data)
    end1 = time.time()
    end = time.time()
    elapsed = (end - start)
    elapsed1 = (end1 - start1)
    print(f'Temps d\'exécution_1 : {elapsed:.6f}s')
    print(f'Temps d\'exécution_2 : {elapsed1:.6f}s')