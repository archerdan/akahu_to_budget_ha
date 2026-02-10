import asyncio
from datetime import timedelta
from homeassistant.helpers.event import async_track_time_interval

from .const import DOMAIN
from .coordinator import run_sync

async def async_setup(hass, config):
    async def scheduled_sync(now):
        await hass.async_add_executor_job(run_sync, hass)

    async_track_time_interval(
        hass,
        scheduled_sync,
        timedelta(hours=1),  # change later
    )

    return True