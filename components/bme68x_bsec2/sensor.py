from esphome.components.bme68x_bsec2_fd import sensor as base
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_PRESSURE,
)

PLATFORM_SCHEMA = base.PLATFORM_SCHEMA.extend(
    {
        # no changes — reuse everything
    }
)

async def to_code(config):
    await base.to_code(config)
