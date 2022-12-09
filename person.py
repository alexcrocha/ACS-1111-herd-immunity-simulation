import random

# random.seed(11)
from virus import Virus


class Person(object):
    is_alive = True

    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infection = infection

    def did_survive_infection(self):
        """This method randomly determines whether this person survives the infection or not,
        based on the mortality rate of the virus.
        """
        if random.random() < self.infection.mortality_rate:
            self.is_alive = False
            self.is_vaccinated = False
            self.infection = None
            return False
        else:
            self.is_vaccinated = True
            self.infection = None
            return True


if __name__ == "__main__":
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    virus = Virus("Dysentery", 0.7, 0.2)

    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    people = []
    for i in range(1, 100):
        infected_person = Person(i, False, virus)
        people.append(infected_person)

    did_survived = 0
    did_not_survive = 0
    for person in people:
        if person.did_survive_infection() is True:
            did_survived += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survived}\nDid not survive: {did_not_survive}")

    uninfected_people = []
    infected_people = []

    for i in range(1, 1000):
        person = Person(i, False)
        if random.random() < virus.repro_rate:
            person.infection = virus
            infected_people.append(person)
        else:
            uninfected_people.append(person)

    print(f"Infected: {len(infected_people)}\nUninfected: {len(uninfected_people)}")
