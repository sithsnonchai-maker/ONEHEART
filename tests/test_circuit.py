from oneheart.circuit import Circuit


def test_voltage_divider():
    # V_source -- R1 -- Vout -- R2 -- GND
    c = Circuit(ground="GND")
    c.add_voltage_source("V1", 10.0)  # source node tied to 10V
    c.add_resistor("V1", "out", 1000.0)  # R1
    c.add_resistor("out", "GND", 1000.0)  # R2
    sol = c.solve()
    assert abs(sol["out"] - 5.0) < 1e-6


def test_series_two_resistors_middle_voltage():
    # Vsource -- R1 -- mid -- R2 -- GND
    c = Circuit(ground="0")
    c.add_voltage_source("Vs", 12.0)
    c.add_resistor("Vs", "mid", 2000.0)
    c.add_resistor("mid", "0", 1000.0)
    sol = c.solve()
    # Voltage at mid = Vs * R2 / (R1 + R2) = 12 * 1000 / 3000 = 4
    assert abs(sol["mid"] - 4.0) < 1e-6


def test_node_to_ground_resistor_only():
    # Node connected to ground through a resistor, and to a fixed voltage through resistor
    c = Circuit(ground="GND")
    c.add_voltage_source("Vsrc", 5.0)
    c.add_resistor("Vsrc", "node", 100.0)
    c.add_resistor("node", "GND", 100.0)
    sol = c.solve()
    assert abs(sol["node"] - 2.5) < 1e-6
