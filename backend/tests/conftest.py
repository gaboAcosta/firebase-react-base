import pytest


class MockSession:
    def __init__(self, query_results=None):
        self.query_results = query_results or {}

    def query(self, model):
        return MockQuery(self.query_results)


class MockQuery:
    def __init__(self, query_results):
        self.query_results = query_results

    def all(self):
        return self.query_results


@pytest.fixture(scope='session')
def create_mock_session():
    def _create_mock_session(query_results):
        return MockSession(query_results)
    return _create_mock_session
