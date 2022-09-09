from datasette.app import Datasette
import pytest


@pytest.fixture
def ds():
    return Datasette(memory=True)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "headers,expected",
    (
        ({}, None),
        (
            {"X-Sandstorm-User-Id": "1", "X-Sandstorm-Username": "ab%20c"},
            {"id": "1", "username": "ab c", "permissions": []},
        ),
        (
            {
                "X-Sandstorm-Permissions": "a,b",
                "X-Sandstorm-Preferred-Handle": "preferred_handle",
                "X-Sandstorm-User-Picture": "picture",
                "X-Sandstorm-User-Pronouns": "pronouns",
            },
            {
                "permissions": ["a", "b"],
                "preferred_handle": "preferred_handle",
                "picture": "picture",
                "pronouns": "pronouns",
            },
        ),
    ),
)
async def test_actor_from_headers(ds, headers, expected):
    response = await ds.client.get("/-/actor.json", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"actor": expected}
