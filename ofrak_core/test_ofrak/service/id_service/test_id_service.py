import pytest

from ofrak.service.id_service_i import IDServiceInterface
from ofrak.service.id_service_sequential import SequentialIDService
from ofrak.service.id_service_uuid import UUIDService


@pytest.fixture
def sequential_id_service():
    return SequentialIDService()


@pytest.fixture
def uuid_service():
    return UUIDService()


@pytest.mark.parametrize("id_service", ["sequential_id_service", "uuid_service"])
def test_get_id(id_service, request):
    id1 = request.getfixturevalue(id_service).generate_id()
    id2 = request.getfixturevalue(id_service).generate_id()

    assert id1 != id2


@pytest.mark.parametrize("id_service", ["sequential_id_service", "uuid_service"])
def test_generate_id_from_base(id_service, request):
    ids = request.getfixturevalue(id_service)
    base_id = ids.generate_id()
    key1 = "alpha"
    key2 = "beta"

    id1 = ids.generate_id_from_base(base_id, key1)
    id2 = ids.generate_id_from_base(base_id, key2)

    assert id1 != id2

    _id1 = ids.generate_id_from_base(base_id, key1)
    assert _id1 == id1

    _id2 = ids.generate_id_from_base(base_id, key2)
    assert _id2 == id2

    id3 = ids.generate_id_from_base(id1, key2)
    assert id3 != id1
    assert id3 != id2
