import json
from pathlib import Path


def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def write_to_file(content, file_path: Path, json_dumps=False, indent=None):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, mode="w") as f:
        if json_dumps:
            return f.write(json.dumps(content, indent=indent, default=serialize_sets))
        return f.write(content)


def read_file(file_path, json_loads):
    with open(file_path, "r") as file:
        if json_loads:
            return json.loads(file.read())
        return file.read()
