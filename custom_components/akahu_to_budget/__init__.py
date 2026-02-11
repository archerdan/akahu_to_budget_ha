from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_interval

from .const import DOMAIN
from .coordinator import run_sync

PLATFORMS = []

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    async def scheduled_sync(now):
        await hass.async_add_executor_job(run_sync, hass, entry)

    entry.async_on_unload(
        async_track_time_interval(
            hass,
            scheduled_sync,
            timedelta(hours=1),  # change later if you want
        )
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data[DOMAIN].pop(entry.entry_id)
    return True