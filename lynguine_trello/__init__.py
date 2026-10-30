"""Trello as a lynguine IO type.

Importing this module is enough: it registers ``type: trello`` and the
``trello_api`` credential validator. lynguine fetches the secret named in
``credential:``; this package only reads ``credential_value``.
"""

from __future__ import annotations

import pandas as pd

from lynguine.access.io import register_io_type
from lynguine.security.credentials import get_credential_manager


def validate_trello_api(credential) -> bool:
    """Accept a Trello api_key + token stored as the CIP-0005 value."""
    value = credential.get("value", credential) if isinstance(credential, dict) else credential
    if isinstance(value, dict):
        return bool(value.get("api_key")) and bool(value.get("token"))
    return False


get_credential_manager().register_validator("trello_api", validate_trello_api)


def read_trello(details: dict) -> pd.DataFrame:
    """Read cards from a Trello board.

    Required YAML:

    * ``credential:`` — CIP-0005 key (lynguine binds ``credential_value``)
    * ``board:`` — Trello board id

    The REST fetch is not implemented yet; the registration form is.
    """
    creds = details.get("credential_value")
    if not isinstance(creds, dict):
        raise ValueError("Trello read expected credential_value from lynguine")
    board = details.get("board")
    if not isinstance(board, str) or not board.strip():
        raise ValueError('Type "trello" requires board: <board id>')
    raise NotImplementedError(
        "lynguine-trello registers type: trello; the Trello REST reader is next"
    )


register_io_type(
    "trello",
    read=read_trello,
    credential_type="trello_api",
)
