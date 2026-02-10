import os
import subprocess
from pathlib import Path

def run_sync(hass):
    base_path = Path(__file__).parent
    upstream = base_path / "vendor" / "akahu_to_budget"

    env = os.environ.copy()
    env.update({
        "AKAHU_TOKEN": hass.config.as_dict().get("akahu_token", ""),
        "ACTUAL_BUDGET_URL": hass.config.as_dict().get("actual_budget_url", "")
    })

    subprocess.run(
        ["python3", "flask_app.py", "--sync"],
        cwd=upstream,
        env=env,
        check=False,
    )