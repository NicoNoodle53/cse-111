#importa libraries and functions
from pytest import approx
import pytest

from water_flow import (water_column_height, pressure_gain_from_water_height
    ,pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction)

def test_water_column_height():
    assert water_column_height(0,0) == 0
    assert water_column_height(0,10) == approx(7.5)
    assert water_column_height(25,0) == 25
    assert water_column_height(48.3, 12.8) == approx (57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0)
    assert pressure_gain_from_water_height(30.2) == approx(295.628)
    assert pressure_gain_from_water_height(50) == approx(489.450)

def test_pressure_loss_from_pipe():
    pipe_diameter = [.048692, .048692, .048692 , .048692, .048692
        , .28687, .28687 ]
    pipe_length = [0, 200, 200, 200, 200, 1000, 1800.75]
    friction_factor = [.018, 0, .018, .018, .018, .013, .013]
    fluid_velocity = [1.75, 1.75, 0, 1.75, 1.65, 1.65, 1.65]
    expected_pressure_loss = [0, 0, 0, -113.008, -100.462, -61.576, -110.884]

    for i in range(7):
        assert pressure_loss_from_pipe(pipe_diameter[i], pipe_length[i], friction_factor[i],
                                       fluid_velocity[i]) == approx(expected_pressure_loss[i])

def test_pressure_loss_from_fittings():
    fluid_velocity = [0, 1.65, 1.65, 1.75, 1.75]
    quantity_fittings = [3, 0, 2, 2, 5]
    pressure_loss = [0, 0, -0.109, -0.122, -0.306]

    for i in range(5):
        assert pressure_loss_from_fittings(fluid_velocity[i], quantity_fittings[i]) == approx(pressure_loss[i])

def test_reynolds_number():
    hydraulic_diameter = [0.048692, 0.048692, 0.048692, 0.28687, 0.28687]
    fluid_velocity = [0, 1.65, 1.75, 1.65, 1.75]
    expected_number = [0, 80069, 84922, 471729, 500318]

    for i in range(5):
        assert reynolds_number(hydraulic_diameter[i], fluid_velocity[i]) == approx(expected_number[i])

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182)

pytest.main(["-v", "--tb=line", "-rN", __file__])
