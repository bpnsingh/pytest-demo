from stuff.accum import Accumulator
import pytest

@pytest.fixture
def accum():
    yield Accumulator()
    print("Done with tests!!")

@pytest.fixture

def accum2():
    return Accumulator()