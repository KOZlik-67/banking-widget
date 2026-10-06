
import json
import os
from typing import Any, Dict, List


def get_transactions_data(file_path: str) -> List[Dict[str, Any]]:

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []
