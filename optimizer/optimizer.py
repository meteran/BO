__author__ = 'lis'

class BeesAlgorithm:
    '''
    Class implementing bees algorithm for our problem.
    Solutions are represented by table of tuples with x,y indices in cost_array.
    '''

    ITERATIONS = 5000
    BEES_AMOUNT = 50
    ELITE_PATCHES = 1
    BEST_PATCHES = 4



    def __init__(self, data):
        self.data = data

    def get_next_solution(self, solution):  # TODO
        '''
        :param solution: None or solution
        :return: neighed solution if solution, random solution otherwise
        '''
        if solution:
            return 1
        else:
            return None

    def initialize_population(self):
        '''
        :return: initial solutions table
        '''
        solutions = []
        for bee in range(0, self.BEES_AMOUNT):
            solution = self.get_next_solution(solution=None)
            solutions[bee] = (solution, self.calculate_objective_function(solution))
        return solutions

    def calculate_objective_function(self, solution):  # TODO
        '''
        :param solution: compulsory
        :return: objective function value for given solution
        '''
        if solution:
            return 1

    def sort_solutions(self, solutions):
        '''
        :param solutions: current table of solutions
        :return: sorted solutions if solutions, else None
        '''
        if solutions:
            return sorted(solutions, key=lambda solution: solution[1])
        else:
            return None

    def bees_algorithm(self):
        '''
        :return: burza za oknem
        '''

        # get random solutions for start
        solutions = self.sort_solutions(self.initialize_population())

        for i in range(0, self.ITERATIONS):

            pass

        return "dupa"
