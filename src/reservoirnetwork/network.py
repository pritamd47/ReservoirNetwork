from landlab import NetworkModelGrid

class ReservoirNetwork(NetworkModelGrid):
    def __init__(self, yx_of_node, links, xy_of_reference=None, xy_axis_name=('lon', 'lat'), xy_axis_units=('deg', 'deg')):
        if xy_of_reference is not None:
            super().__init__(yx_of_node, links, xy_axis_name, xy_axis_units, xy_of_reference)
        else:
            super().__init__(yx_of_node, links, xy_axis_name, xy_axis_units, xy_of_reference=(yx_of_node[1], yx_of_node[0]))