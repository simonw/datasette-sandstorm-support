from datasette import hookimpl
from urllib.parse import unquote

ACTOR_MAPPING = (
    ("X-Sandstorm-Username", "username"),
    ("X-Sandstorm-User-Id", "id"),
    ("X-Sandstorm-Preferred-Handle", "preferred_handle"),
    ("X-Sandstorm-User-Picture", "picture"),
    ("X-Sandstorm-User-Pronouns", "pronouns"),
)
PERCENT_DECODE = {"X-Sandstorm-Username"}

PERMISSIONS_MAPPING = {
    # Datasette permessions -> required Sandstorm permission
    "upload-csvs": "edit",
    "upload-dbs": "edit",
}


@hookimpl
def actor_from_request(request):
    actor = {}
    for header, key in ACTOR_MAPPING:
        value = request.headers.get(header.lower())
        if value:
            if header in PERCENT_DECODE:
                value = unquote(value)
            actor[key] = value
    if actor:
        # Handle permissions
        x_permissions = request.headers.get("x-sandstorm-permissions") or ""
        permissions = [p.strip() for p in x_permissions.split(",") if p.strip()]
        actor["permissions"] = permissions
    return actor or None


@hookimpl
def permission_allowed(action, actor):
    if actor and "permissions" in actor and action in PERMISSIONS_MAPPING:
        return PERMISSIONS_MAPPING[action] in actor["permissions"]
