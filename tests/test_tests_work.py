import pytest

@pytest.xfail('pytest is working.')
def test_something(self):
    self.assertEqual(True, False)