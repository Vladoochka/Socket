SINGLE_USER = {
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

SINGLE_RESOURCE = {
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"},
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}

DELAYED_RESPONSE = {
    "properties": {
        "page": {"type": "number", "enum": [1, 2]},
        "per_page": {"type": "number", "enum": [6]},
        "total": {"type": "number", "enum": [12]},
        "total_pages": {"type": "number", "enum": [2]},
        "data": {
            "type": "array",
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}
