from datasette import hookimpl
from urllib.parse import unquote

MAPPING = (
    ("X-Sandstorm-Username", "username"),
    ("X-Sandstorm-User-Id", "id"),
    ("X-Sandstorm-Permissions", "permissions"),
    ("X-Sandstorm-Preferred-Handle", "preferred_handle"),
    ("X-Sandstorm-User-Picture", "picture"),
    ("X-Sandstorm-User-Pronouns", "pronouns"),
)
PERCENT_DECODE = {"X-Sandstorm-Username"}


@hookimpl
def actor_from_request(request):
    actor = {}
    for header, key in MAPPING:
        value = request.headers.get(header.lower())
        if value:
            if header in PERCENT_DECODE:
                value = unquote(value)
            actor[key] = value
    return actor or None
