from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, CONF_AKAHU_TOKEN, CONF_ACTUAL_BUDGET_URL

class AkahuToBudgetConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # You can add validation later
            return self.async_create_entry(
                title="Akahu to Actual Budget",
                data=user_input,
            )

        schema = vol.Schema({
            vol.Required(CONF_AKAHU_TOKEN): str,
            vol.Required(CONF_ACTUAL_BUDGET_URL): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )