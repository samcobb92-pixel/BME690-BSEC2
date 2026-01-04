import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_PRESSURE,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_HPA,
    UNIT_OHM
)

# Define your namespace
bme68x_ns = cg.esphome_ns.namespace('bme68x_bsec2_fd')
BME68xComponent = bme68x_ns.class_('BME68xComponent', cg.Component)

# YAML schema: allows only 'id' for now
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BME68xComponent),
}).extend(cv.COMPONENT_SCHEMA)

# Map C++ sensors to ESPHome
SENSOR_TYPES = {
    'temperature': (DEVICE_CLASS_TEMPERATURE, UNIT_CELSIUS),
    'humidity': (DEVICE_CLASS_HUMIDITY, UNIT_PERCENT),
    'pressure': (DEVICE_CLASS_PRESSURE, UNIT_HPA),
    'gas_resistance': (None, UNIT_OHM),
    'iaq': (None, None),
    'co2_equivalent': (None, UNIT_PERCENT),
    'breath_voc_equivalent': (None, UNIT_PERCENT),
}

async def to_code(config):
    # Create C++ object
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    # Add each sensor
    for sensor_name, (device_class, unit) in SENSOR_TYPES.items():
        s = cg.new_Pvariable(getattr(var, sensor_name))
        if device_class:
            sensor.setup_sensor(s, sensor_name, device_class=device_class, unit_of_measurement=unit)
        else:
            sensor.setup_sensor(s, sensor_name)
