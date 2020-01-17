import pytest

from app.utils.database import Database


def pytest_namespace():
    return {"_id": None}


@pytest.mark.incremental
class TestDatabase:
    db = Database()
    test_doc = {
        "author": "Dmitriy Diachkov",
        "text": "Sample text",
    }

    def test_connection(self):
        assert self.db.healthcheck() is True

    def test_insert(self):
        pytest._id = self.db.insert(self.test_doc)
        assert len(pytest._id) == 24

    def test_get(self):
        assert self.db.get(pytest._id) == self.test_doc

    def test_update(self):
        updated = self.db.update(pytest._id, {"text": "Updated sample text"})
        assert updated is True

    def test_delete(self):
        deleted = self.db.delete(pytest._id)
        assert deleted is True
