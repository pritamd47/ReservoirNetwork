def test_reservoir_component():
    import numpy as np
    from landlab import NetworkModelGrid

    y_of_node = (0, 1)
    x_of_node = (0, 0)

    nodes_at_link=( # a simple 2 reservoir network
        (1, 0)
    )
    grid = NetworkModelGrid((y_of_node, x_of_node), nodes_at_link)

    grid.add_field(
        "reservoir__total_inflow",
        np.full_like(grid.x_of_node, np.nan),
        at='node',
        units='m3/d' ,
        clobber=True
    )
    grid.add_field(
        "reservoir__storage_change",
        np.full_like(grid.x_of_node, np.nan),
        at='node',
        units='m3/d' ,
        clobber=True
    )
    grid.add_field(
        "reservoir__release",
        np.full_like(grid.x_of_node, np.nan),
        at='node',
        units='m3/d' ,
        clobber=True
    )
    grid.add_field(
        "reservoir__regulated_inflow",
        np.full_like(grid.x_of_node, np.nan),
        at='node',
        units='m3/d' ,
        clobber=True
    )
    grid.add_field(
        "reservoir__unregulated_inflow",
        np.full_like(grid.x_of_node, np.nan),
        at='node',
        units='m3/d' ,
        clobber=True
    )
    grid.add_field(
        "reservoir__abstract_elevation",
        (1.0, 0.0),
        at='node',
        units='m3/d' ,
        clobber=True
    )
    
    from reservoirnetwork.reservoir_component import StreamflowRegulation
    
    # define input data
    time = [ 1, 2, 3, 4, 5]

    r_A_inflow = [ 120, 130, 90, 60, 30]
    r_A_storage_change = [ 30, 30, 10, 0, 0]
    r_B_inflow = [162, 178, 134, 96, 48]
    r_B_storage_change = [ 35, 30, 30, 10, 0]
    last_release = [90, 127]

    # store outputs
    reservoir__release = []
    reservoir__regulated_inflow = []
    reservoir__unregulated_inflow = []

    grid.at_node['reservoir__release'] = last_release

    sr = StreamflowRegulation(grid)


    for t, inflow, storage_change in zip(
        time, 
        zip(r_A_inflow, r_B_inflow), 
        zip(r_A_storage_change, r_B_storage_change)
    ):
        sr.run_one_step(t, inflow, storage_change)
        
        reservoir__release.append(grid.at_node['reservoir__release'])
        reservoir__unregulated_inflow.append(grid.at_node['reservoir__unregulated_inflow'])
        reservoir__regulated_inflow.append(grid.at_node['reservoir__regulated_inflow'])

    calculated_reservoir__release = [
        [90, 127]
        [100, 148]
        [80, 104]
        [60, 86]
        [30, 48]
    ]
    calculated_reservoir__unregulated_inflow = [
        [120, 72],
        [130, 78],
        [90, 54],
        [60, 36],
        [30, 18]
    ]
    calculated_reservoir__regulated_inflow = [
        [0, 90],
        [0, 100],
        [0, 80],
        [0, 60],
        [0, 30]
    ]

    assert calculated_reservoir__release == reservoir__release
    assert calculated_reservoir__unregulated_inflow == reservoir__unregulated_inflow
    assert calculated_reservoir__regulated_inflow == reservoir__regulated_inflow