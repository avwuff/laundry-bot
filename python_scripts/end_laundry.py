service_data = {"entity_id": "input_boolean.laundryinuse"}
hass.services.call("input_boolean", "turn_off", service_data, False)

service_data = {"entity_id": "input_boolean.laundrydone"}
hass.services.call("input_boolean", "turn_off", service_data, False)

# only turn this relay off if it is reading 0 watts
wattage = hass.states.get('sensor.avwasher_wattage').state
if float(wattage) < 2.1:
    service_data = {"entity_id": "switch.avwasher_relay"}
    hass.services.call("switch", "turn_off", service_data, False)

service_data = {"entity_id": "switch.lcd_backlight"}
hass.services.call("switch", "turn_off", service_data, False)
