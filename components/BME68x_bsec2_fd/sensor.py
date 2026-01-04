import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import CONF_ID, DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_PRESSURE

# This must match the C++ class name in your fd BSEC2 repo
bme68x_ns = cg.esphome_ns.namespace('bme68x_bsec2_fd')
BME68xComponent = bme68x_ns.class_('BME68xComponent', cg.Component)

# YAML configuration schema
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BME68xComponent),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    # Create an instance of the component
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
