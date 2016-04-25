__author__ = 'lis'


class BeesAlgorithm:
    """
    Class implementing bees algorithm for our problem.
    Solutions are represented by (solution_table, solution_fitness) tuples
    """

    def __init__(self, data, iterations=5000, scout_bees=50, search_patches=5, elite_patches=1, elite_patch_bees=5,
                 search_patch_bees=3, initial_patch_size=5):
        self.data = data
        self.iterations = iterations
        self.scout_bees = scout_bees
        self.search_patches = search_patches
        self.elite_patches = elite_patches
        self.elite_patch_bees = elite_patch_bees
        self.search_patch_bees = search_patch_bees
        self.initial_patch_size = initial_patch_size
        self.random_scout_bees = elite_patches*elite_patch_bees + (search_patches-elite_patches)*search_patch_bees

    # -------------------------------------------------------------

    def evaluate_fitness(self, scout_bee):
        '''
        :param scout_bee: represents a single solution
        :return: objective function value for given scout_bee
        '''
        # TODO
        return scout_bee

    def get_random_scout_bee(self):
        '''
        :return: returns random (scout_bee, scout_bee_fitness)
        '''
        scout_bee = 1
        # TODO
        return scout_bee, self.evaluate_fitness(scout_bee)

    def get_neighed_scout_bee(self, scout_bee):
        '''
        :param scout_bee: scout_bee to search nearby
        :return: (scout_bee, scout_bee_fitness) neighed to scout_bee
        '''
        # TODO
        return scout_bee, self.evaluate_fitness(scout_bee)

    # -------------------------------------------------------------

    def initialize_population(self):
        '''
        :return: initial scout_bees table
        '''
        scout_bees = []
        for scout_bee in range(0, self.scout_bees):
            scout_bees[scout_bee] = self.get_random_scout_bee()
        return scout_bees

    def order_by_fitnesses(self, scout_bees):
        '''
        :param scout_bees: current table of scout_bees
        :return: sorted scout_bees
        '''
        return sorted(scout_bees, key=lambda solution: solution[1])

    # -------------------------------------------------------------

    def bees_algorithm(self):
        '''
        :return: burza za oknem
        '''

        # STEP 1 - place scout_bees in random solutions
        scout_bees = self.initialize_population()

        # STEP 2 - evaluate fitness of the population
        scout_bees = self.order_by_fitnesses(scout_bees)

        # STEP 3 - go until stop criterion is met
        for i in range(0, self.iterations):

            # STEP 4 - select elite and search patches
            scout_bees = scout_bees[:self.search_patches]
            elite_patches = scout_bees[:self.elite_patches]
            search_patches = scout_bees[self.search_patches:self.elite_patches]

            # STEP 5 - determine patch size
            # TODO

            # STEP 6 - recruit bees for selected sites and evaluate fitnesses for elite patches
            for elite_patch in elite_patches:
                elite_site = []
                for elite_patch_bee in range(0, self.elite_patch_bees):
                    elite_site[elite_patch_bee] = self.get_neighed_solution(elite_patch)

                # STEP 7 - select fittest bee from each site and abandon sites without new information
                if self.order_by_fitnesses(elite_site)[0][1] < elite_patch[1]:
                    scout_bees.extend(elite_site)

            # STEP 6 - recruit bees for selected sites and evaluate fitnesses for remaining patches
            for search_patch in search_patches:
                search_site = []
                for search_patch_bee in range(0, self.search_patch_bees):
                    search_site[search_patch_bee] = self.get_neighed_solution(search_patch)

                # STEP 7 - select fittest bee from each site and abandon sites without new information
                if self.order_by_fitnesses(search_site)[0][1] < search_patch[1]:
                    scout_bees.extend(search_site)

            # STEP 9 - assign remaining bees to search randomly and evaluate their fitnesses
            for scout_bee in range(0, self.random_scout_bees):
                scout_bees.append(self.get_random_solution())

            # STEP 10 - enter another iteration with ordered scout bees
            scout_bees = self.order_by_fitnesses(self.scout_bees)

        return scout_bees[0]
