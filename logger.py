class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(
        self,
        pop_size,
        vacc_percentage,
        virus_name,
        mortality_rate,
        basic_repro_num,
        initial_infected,
    ):
        """This method writes the simulation metadata to the logger file."""
        with open(self.file_name, "w", encoding="utf-8") as f:
            f.write("## Simulation Metadata\n")
            f.write('\n---\n\n\n')
            f.write(f"- Virus: {virus_name}\n")
            f.write(f"- Mortality Rate: {int(mortality_rate*100)}%\n")
            f.write(f"- Basic Reproduction: {int(basic_repro_num*100)}%\n")
            f.write(f"- Population Size: {pop_size}\n")
            f.write(f"- Vaccination Percentage: {int(vacc_percentage*100)}%\n")
            f.write(f"- Initial Infected: {int(initial_infected)}\n")
            f.write("## Simulation Log\n")
            f.write('---\n')

    def log_time_step(
        self,
        time_step_number,
        num_vaccinated,
        num_infected,
        num_dead,
        num_alive,
        saved_by_immunity,
    ):
        """This method logs the current state of the simulation to the logger file."""
        with open(self.file_name, "a", encoding="utf-8") as f:
            f.write("```diff\n")
            f.write(
                f"@@ Step {time_step_number} @@\n"
            ) if time_step_number != 0 else f.write(f"@@ Simulation Initial State @@\n")
            f.write(f"+ Alive: {num_alive}\n")
            f.write(f"+ Vaccinated: {int(num_vaccinated)}\n")
            f.write(f"+ Saved by Immunity: {saved_by_immunity}\n")
            f.write(f"! Infected: {num_infected}\n")
            f.write(f"- Dead: {num_dead}\n")
            f.write("```\n")

    def log_end_of_simulation(
        self,
        num_vaccinated,
        num_dead,
        num_alive,
        total_saved_by_immunity,
        total_interactions,
    ):
        """This method logs the end of the simulation to the logger file."""
        with open(self.file_name, "a", encoding="utf-8") as f:
            f.write("```diff\n")
            f.write(f"@@ Simulation End State @@\n")
            f.write(f"! Total Interactions: {total_interactions}\n")
            f.write(f"+ Alive: {num_alive}\n")
            f.write(f"+ Vaccinated: {int(num_vaccinated)}\n")
            f.write(f"+ Saved by Immunity: {total_saved_by_immunity}\n")
            f.write(f"- Dead: {num_dead}\n")
            f.write("```\n")
