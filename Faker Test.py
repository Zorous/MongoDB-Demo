from faker import Faker

faker = Faker()

print(f'a word: {faker.word()}')
print(f'six words: {faker.words(6)}')

words = ['forest', 'blue', 'cloud', 'sky', 'wood', 'falcon']

print(f'customized unique words: {faker.words(3, words, True)}')