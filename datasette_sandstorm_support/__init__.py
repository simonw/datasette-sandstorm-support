from datasette import hookimpl

MAPPING = (
    ("X-Sandstorm-Username", "username"),
    ("X-Sandstorm-User-Id", "id"),
    ("X-Sandstorm-Permissions", "permissions"),
    ("X-Sandstorm-Preferred-Handle", "preferred_handle"),
    ("X-Sandstorm-User-Picture", "picture"),
    ("X-Sandstorm-User-Pronouns", "pronouns"),
)


@hookimpl
def actor_from_request(request):
    actor = {}
    for header, key in MAPPING:
        value = request.headers.get(header.lower())
        if value:
            actor[key] = value
    return actor or None
