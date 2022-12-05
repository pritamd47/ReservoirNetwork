from landlab import NetworkModelGrid

class ReservoirNetwork(NetworkModelGrid):
    def __init__(self, yx_of_node, links, xy_axis_name=..., xy_axis_units="-", xy_of_reference=...):
        super().__init__(yx_of_node, links, xy_axis_name, xy_axis_units, xy_of_reference)
    