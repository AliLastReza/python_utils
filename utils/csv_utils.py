import csv
from pathlib import Path


def read_csv_file(file_path, parse_to_dict: bool = False):
    with open(file_path, "r", newline="") as csvfile:
        if parse_to_dict:
            return list(csv.DictReader(csvfile))
        else:
            return list(csv.reader(csvfile))


def write_to_csv_file(rows, file_path: Path, rows_type, fieldnames=None):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, mode="w", newline="") as csvfile:
        if rows_type is list:
            csv_writer = csv.writer(csvfile)
            return csv_writer.writerows(rows)
        elif rows_type is dict:
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
        else:
            raise Exception("rows_type value is invalid!")


def append_to_csv_file(rows, file_path: Path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, mode="a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        return csv_writer.writerows(rows)


def convert_config_to_key_val_dict(config: list):
    res = dict()
    for row in config:
        match row["value_type"]:
            case "int":
                value = int(row["value"])
            case _:
                raise Exception("Invalid value_type.")
        res[row["key"]] = value
    return res


def convert_config_dict_to_list_of_key_values(config: dict):
    result = list()
    for k, v in config.items():
        result.append({"key": k, "value": v, "value_type": type(v).__name__})
    return result
