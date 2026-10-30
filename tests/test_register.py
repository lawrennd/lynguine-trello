"""The package must declare type trello and credential_type trello_api on import."""

from lynguine.access.io_types import get_io_type


def test_import_registers_trello():
    import lynguine_trello  # noqa: F401

    spec = get_io_type("trello")
    assert spec is not None
    assert spec.name == "trello"
    assert spec.credential_type == "trello_api"
    assert spec.write is None
    assert spec.read is lynguine_trello.read_trello


def test_read_requires_board():
    import lynguine_trello

    try:
        lynguine_trello.read_trello(
            {"credential_value": {"api_key": "k", "token": "t"}}
        )
    except ValueError as exc:
        assert "board" in str(exc)
    else:
        raise AssertionError("expected ValueError for missing board")
