import random, sys
from person import Person
from logger import Logger
from virus import Virus

random.seed(11)


class Simulation(object):
    newly_infected = []
    saved_by_immunity = 0
    total_interactions = 0
    total_saved_by_immunity = 0

    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=10):
        self.logger = Logger("loggymclogface.md")
        self.virus = virus
        self.pop_size = int(pop_size)
        self.vacc_percentage = float(vacc_percentage)
        self.initial_infected = int(initial_infected)
        self.num_vaccinated = self.pop_size * self.vacc_percentage
        self.num_infected = self.initial_infected
        self.num_dead = 0
        self.num_alive = self.pop_size - self.num_dead

        self.population = self._create_population()

    def _create_population(self):
        """This method creates the initial population.
        It returns a list of Person objects equal in size to the pop_size.
        Some of these people will be infected and some will not based on the initial_infected attribute.
        """
        population = []
        infected = 0

        for _id in range(self.pop_size):
            population.append(
                Person(
                    _id,
                    False
                    if _id < self.initial_infected
                    or _id > (self.num_vaccinated + self.initial_infected)
                    else True,
                    None if infected >= self.initial_infected else self.virus,
                )
            )
            if infected < self.initial_infected:
                infected += 1
        return population

    def _simulation_should_continue(self):
        """This method returns a boolean value indicating whether or not the simulation should continue.
        The simulation should continue if there are still infected people in the population.
        """
        for person in self.population:
            if person.infection:
                return True
        return False

    def run(self):
        """This method runs the simulation until all requirements for ending the simulation are met."""
        self.logger.write_metadata(
            self.pop_size,
            self.vacc_percentage,
            self.virus.name,
            self.virus.mortality_rate,
            self.virus.repro_rate,
            self.initial_infected,
        )

        time_step_counter = 0
        self.logger.log_time_step(
            time_step_counter,
            self.num_vaccinated,
            self.num_infected,
            self.num_dead,
            self.pop_size - self.num_dead,
            self.saved_by_immunity,
        )
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.saved_by_immunity = 0

            self.time_step()
            self.num_infected = len(
                [person for person in self.population if person.infection is not None]
            )
            self.num_vaccinated = len(
                [person for person in self.population if person.is_vaccinated is True]
            )
            self.num_dead = len(
                [person for person in self.population if person.is_alive is False]
            )
            self.num_alive = self.pop_size - self.num_dead
            self.logger.log_time_step(
                time_step_counter,
                self.num_vaccinated,
                self.num_infected,
                self.num_dead,
                self.num_alive,
                self.saved_by_immunity,
            )

            should_continue = self._simulation_should_continue()

        self.logger.log_end_of_simulation(
            self.num_vaccinated,
            self.num_dead,
            self.num_alive,
            self.total_saved_by_immunity,
            self.total_interactions,
        )

    def time_step(self):
        """This method represents a single time step in the simulation.
        It simulates interactions between people,
        and determines if vaccinations and fatalities from infections occur.
        """

        infected_people = [
            person for person in self.population if person.infection is not None
        ]

        for person in infected_people:
            for _ in range(100) if self.num_alive > 100 else range(self.num_alive):
                self.interaction(
                    random.choice(
                        list(filter(lambda p: p.is_alive is True, self.population))
                    ),
                )
            person.did_survive_infection()
        self._infect_newly_infected()

    def interaction(self, random_person):
        """This method represents a single interaction between a random person and an infected person.
        It determines if the random person gets infected or not.
        """
        self.total_interactions += 1

        if random_person.is_vaccinated is True:
            self.saved_by_immunity += 1
            self.total_saved_by_immunity += 1

        elif (
            random_person.infection is None and random.random() < self.virus.repro_rate
        ):
            self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        """This method iterates through the list of newly infected people and infects them."""

        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # # Example of values to be used by the simulation
    # virus_name = "Sniffles"
    # repro_num = 0.5
    # mortality_rate = 0.12
    # population_size = 1000
    # vaccination_percentage = 0.1
    # initial_infected_num = 10
    (   population_size,
        vaccination_percentage,
        virus_name,
        mortality_rate,
        repro_num,
    ) = sys.argv[1:6]
    initial_infected_num = sys.argv[6] if len(sys.argv) > 6 else 10

    bad_virus = Virus(virus_name, float(repro_num), float(mortality_rate))

    sim = Simulation(
        bad_virus, population_size, vaccination_percentage, initial_infected_num
    )

    sim.run()
