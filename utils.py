# utils.py
import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def save_user_message(user_id: int, message: str) -> None:
    user_file = DATA_DIR / f"{user_id}.json"
    try:
        data = json.loads(user_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "message": message
    }
    data.append(entry)
    user_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")