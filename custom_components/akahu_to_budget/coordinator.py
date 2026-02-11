import os
import subprocess
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import CONF_AKAHU_TOKEN, CONF_ACTUAL_BUDGET_URL

def run_sync(hass: HomeAssistant, entry: ConfigEntry):
    base_path = Path(__file__).parent
    upstream = base_path / "vendor" / "akahu_to_budget"

    env = os.environ.copy()
    env.update({
        "AKAHU_TOKEN": entry.data[CONF_AKAHU_TOKEN],
        "ACTUAL_BUDGET_URL": entry.data[CONF_ACTUAL_BUDGET_URL],
    })

    subprocess.run(
        ["python3", "flask_app.py", "--sync"],
        cwd=upstream,
        env=env,
        check=False,
    )