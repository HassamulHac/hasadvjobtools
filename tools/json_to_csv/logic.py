import pandas as pd
from io import BytesIO

def flatten_json(y, parent_key='', sep='.'):
    """
    Recursively flattens a nested dictionary.
    """
    items = {}
    for k, v in y.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        elif isinstance(v, list):
            # Optionally, flatten lists too (just join values as string)
            items[new_key] = ', '.join(map(str, v)) if all(isinstance(i, (str, int, float, bool)) for i in v) else str(v)
        else:
            items[new_key] = v
    return items

def convert_json_to_excel(json_data) -> BytesIO:
    """
    Convert nested JSON (dict or list of dicts) to Excel (flattened).
    """
    if isinstance(json_data, dict):
        json_data = [json_data]  # Wrap single object in list

    flattened_data = [flatten_json(item) for item in json_data]

    df = pd.DataFrame(flattened_data)

    output = BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)
    return output
