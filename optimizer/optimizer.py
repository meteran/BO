__author__ = 'lis'


class BeesAlgorithm:
    """
    Class implementing bees algorithm for our problem.
    Solutions are represented by table of tuples with x,y indices in cost_array.
    """

    def __init__(self, data, iterations=5000, bees_amount=50, elite_patches=1, best_patches=4):
        self.bees_amount = bees_amount
        self.elite_patches = elite_patches
        self.best_patches = best_patches
        self.iterations = iterations
        self.data = data
        self.solution = None

    def get_next_solution(self, solution):  # TODO
        """
        :param solution: None or solution
        :return: neighed solution if solution, random solution otherwise
        """
        if solution:
            return 1

    def initialize_population(self):
        """
        :return: initial solutions table
        """
        solutions = []
        for bee in range(0, self.bees_amount):
            solution = self.get_next_solution(solution=None)
            solutions[bee] = (solution, self.calculate_objective_function(solution))
        return solutions

    def calculate_objective_function(self, solution):  # TODO
        """
        :param solution: compulsory
        :return: objective function value for given solution
        """
        if solution:
            return 1

    def sort_solutions(self, solutions):
        """
        :param solutions: current table of solutions
        :return: sorted solutions if solutions, else None
        """
        if solutions:
            return sorted(solutions, key=lambda solution: solution[1])

    def get_problem(self):
        """
        :return: result
        """

        # get random solutions for start
        # solutions = self.sort_solutions(self.initialize_population())

        it = self.iterations*100
        for i in range(it):
            yield i * 100 / it  # this line is to control the algorithm
            # result of algorithm should be saved into self.solution variable
            # TODO
