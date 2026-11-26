import importlib.util
from pathlib import Path

def test_calculator_file_exists():
    assert Path("calculator.py").is_file(), "calculator.py should exist"

def test_calculator_add_function():
    spec = importlib.util.spec_from_file_location("calculator", "calculator.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, "add"), "calculator module should have an 'add' function"
    add = module.add

    # integer addition
    assert add(0, 0) == 0
    assert add(1, 2) == 3
    assert add(-5, 5) == 0
    assert add(-3, -7) == -10

    # float addition
    assert add(1.5, 2.5) == 4.0
    assert add(-1.2, 3.4) == 2.2

    # mixed int and float
    assert add(2, 3.5) == 5.5
    assert add(3.5, 2) == 5.5

    # large numbers
    large = 10**12
    assert add(large, large) == large * 2

    # ensure it works with bools (since bool is subclass of int)
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, False) == 0

    # ensure it raises TypeError for unsupported types
    try:
        add("a", "b")
    except TypeError:
        pass
    else:
        raise AssertionError("add should raise TypeError when adding non-numeric types")
