from faker import Faker
import random
from database import SessionLocal
from models import Movie

fake=Faker(['zh_TW'])
def seed_movies(count=10):
    with SessionLocal() as session:
        for _ in range(20):
            word_count=random.randint(1,6)
            random_words="".join(fake.words(nb=word_count))
            sentence_count=random.randint(10,15)
            random_sentence="".join(fake.sentence(nb_words=sentence_count))
            random_rate=random.randint(1,10)
            new_movie=Movie(name=random_words, intro=random_sentence, rating=random_rate)
            session.add(new_movie)
            session.commit()
if __name__=="__main__":
    seed_movies(20)
