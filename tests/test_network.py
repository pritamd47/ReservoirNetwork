def test_basic_resnet():
    import xarray as xr
    from reservoirnetwork.network import ReservoirNetwork

    resnet = ReservoirNetwork(
        ((0, 1, 2, 2), (0, 0, -1, 1)), 
        links=[(1, 0), (2, 1), (3, 1)]
    )
    assert type(resnet.ds) == xr.Dataset