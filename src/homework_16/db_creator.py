# shom41k
# homework 16

"""
Create database for homework #16
"""


from models import Base, Brand, Car

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker

# Block constants for DATABASE parameters
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_NAME = "test"
DB_ECHO = False

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}', echo=DB_ECHO)

if not database_exists(engine.url):
    print(f"Database {DB_NAME} do not exists!")
    create_database(engine.url)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":

    def create_data():
        brands, cars = [], []

        opel = Brand(name="Opel")
        brands.append(opel)

        vw = Brand(name="Volkswagen")
        brands.append(vw)

        audi = Brand(name="Audi")
        brands.append(audi)

        bmw = Brand(name="BMW")
        brands.append(bmw)

        toyota = Brand(name="Toyota")
        brands.append(toyota)

        skoda = Brand(name="Skoda")
        brands.append(skoda)

        nissan = Brand(name="Nissan")
        brands.append(nissan)

        corsa = Car(model="Corsa", release_year=1998, brand=opel)
        cars.append(corsa)

        rapid = Car(model="Rapid", release_year=2017, brand=skoda)
        cars.append(rapid)

        a6 = Car(model="A6", release_year=2014, brand=audi)
        cars.append(a6)

        almera = Car(model="Almera", release_year=2006, brand=nissan)
        cars.append(almera)

        passat4 = Car(model="Passat B4", release_year=1991, brand=vw)
        cars.append(passat4)

        passat3 = Car(model="Passat B3", release_year=1995, brand=vw)
        cars.append(passat3)

        print(brands)
        print(cars)

        session.add_all(brands)
        session.add_all(cars)

        octavia = Car(model="Octavia", release_year=2014, brand=skoda)
        session.add(octavia)
        session.commit()

    # create_data()
