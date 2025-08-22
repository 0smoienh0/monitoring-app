from fastapi import FastAPI
import psutil, json
from pathlib import Path
import requests

app = FastAPI()

CONFIG_PATH = Path("/app/config/targets.json")

@app.get("/")
def root():
    return {"message": "Monitoring App Running!"}

@app.get("/system")
def system_info():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict(),
    }

@app.get("/check_services")
def check_services():
    if not CONFIG_PATH.exists():
        return {"error": "Config file not found"}
    targets = json.loads(CONFIG_PATH.read_text())
    results = {}
    for name, url in targets.items():
        try:
            res = requests.get(url, timeout=3)
            results[name] = {"status": res.status_code}
        except Exception as e:
            results[name] = {"status": "down", "error": str(e)}
    return results
