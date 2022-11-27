import random, sys

# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    newly_infected = []

    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("loggymclogface.txt")

        # Store the virus in an attribute
        self.virus = virus
        # Store pop_size in an attribute
        self.pop_size = pop_size
        # Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        # Store initial_infected in a variable
        self.initial_infected = initial_infected
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not.
        # Use the _create_population() method to create the list and
        # return it storing it in an attribute here.
        # TODO: Call self._create_population() and pass in the correct parameters.
        self.population = self._create_population()

    def _create_population(self):
        # Create a list of people (Person instances). This list
        # should have a total number of people equal to the pop_size.
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        population = []
        infected = 0
        for _id in range(self.pop_size):
            population.append(
                Person(
                    _id,
                    False
                    if _id < self.initial_infected
                    and _id
                    < self.pop_size * self.vacc_percentage + self.initial_infected
                    else True,
                    None if infected >= self.initial_infected else self.virus,
                )
            )
            if infected < self.initial_infected:
                infected += 1
        # Return the list of people
        return population

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation
        # should continue.
        # The simulation should not continue if all of the people are dead,
        # or if all of the living people have been vaccinated.
        # Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        for person in self.population:
            if person.is_alive is True:
                if person.is_vaccinated is False:
                    return True
        return False

    def run(self):
        # This method starts the simulation. It should track the number of
        # steps the simulation has run and check if the simulation should
        # continue at the end of each step.

        time_step_counter = 0
        should_continue = True

        while should_continue:
            # Increment the time_step_counter
            time_step_counter += 1
            # for every iteration of this loop, call self.time_step()
            self.time_step()
            # Call the _simulation_should_continue method to determine if
            # the simulation should continue
            should_continue = self._simulation_should_continue()

        # Write meta data to the logger. This should be starting
        # statistics for the simulation. It should include the initial
        # population size and the virus.
        self.logger.write_metadata(
            self.pop_size,
            self.vacc_percentage,
            self.virus.virus_name,
            self.virus.mortality_rate,
            self.virus.basic_repro_num,
        )

        # TODO: When the simulation completes you should conclude this with
        # the logger. Send the final data to the logger.

    def time_step(self):
        # This method will simulate interactions between people, calulate
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other
        # people in the population
        # Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for person in self.population:
            if person.is_alive is True and person.infection is not None:
                for _ in range(100):
                    self.interaction(
                        person,
                        random.choice(
                            filter(lambda p: p.is_alive is True, self.population)
                        ),
                    )

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0.0 and 1.0.  If that number is smaller
        #     than repro_rate, add that person to the newly infected array
        #     Simulation object's newly_infected array, so that their infected
        #     attribute can be changed to True at the end of the time step.
        if random_person.is_vaccinated is True or random_person.infection is not None:
            pass
        elif random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person)
        # TODO: Call logger method during this method.

    def _infect_newly_infected(self):
        # Call this method at the end of every time step and infect each Person.
        # Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    bad_virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    population_size = 1000
    vaccination_percentage = 0.1
    initial_infected_num = 10

    # Make a new instance of the imulation
    # virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    # sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
    sim = Simulation(bad_virus, population_size, vaccination_percentage, initial_infected_num)

    # sim.run()
