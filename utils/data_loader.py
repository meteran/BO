class DataLoader:
    """
    Class used to load demand, supply and cost information from file. Example file contents:
    1, 2, 3, 4, 5
    2, 3, 4
    1, 2, 3, 4, 5
    1, 2, 3, 4, 5
    1, 2, 3, 4 ,5
    """

    @staticmethod
    def load_data_from_file(file_name):
        text_file = open(file_name, "r")
        loaded_lines = text_file.readlines()
        demand_list = list(map(int, loaded_lines[0].split(',')))
        supply_list = list(map(int, loaded_lines[1].split(',')))
        cost_array = [[0 for x in range(len(demand_list))] for x in range(len(supply_list))]
        for i in range(len(supply_list)):
            values = list(map(int, loaded_lines[2 + i].split(',')))
            for j in range(len(demand_list)):
                cost_array[i][j] = values[j]
        return Data(supply_list, demand_list, cost_array)


class Data:
    def __init__(self, supply_list, demand_list, cost_array):
        self.supply_list = supply_list
        self.demand_list = demand_list
        self.cost_array = cost_array
