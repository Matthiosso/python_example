import pytest

from example.common.smart_door import SmartDoor


@pytest.fixture
def my_test_smart_door():
    return SmartDoor('Ma porte de test')


def test_open(my_test_smart_door):
    assert my_test_smart_door.open() == "Ma porte de test s'ouvre."


def test_close(my_test_smart_door):
    assert my_test_smart_door.close() == "Ma porte de test se ferme."
