import pytest


@pytest.mark.sk
def test_saikiran_hobby():
    print("hearing music")


@pytest.mark.skip
def test_saikiran_goal():
    print("get a job")


@pytest.mark.smoke
def test_saikiran_strength():
    print("time management")
