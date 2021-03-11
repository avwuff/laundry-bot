name = data.get("name", "Missing")

# Indicate who started the laundry process.
service_data = {"entity_id": "input_text.laundryuser", "value": name}
hass.services.call("input_text", "set_value", service_data, False)

# Reset the zero count
service_data = {"entity_id": "input_number.laundryzerocount", "value": 0}
hass.services.call("input_number", "set_value", service_data, False)

# Set the start time of the laundry
now = datetime.datetime.now()
# %Y-%m-%d %H:%M:%S
service_data = {"entity_id": "input_datetime.laundrystartedat", "datetime": "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)  }
hass.services.call("input_datetime", "set_datetime", service_data, False)

service_data = {"entity_id": "input_boolean.laundrydone"}
hass.services.call("input_boolean", "turn_off", service_data, False)

service_data = {"entity_id": "input_boolean.laundryinuse"}
hass.services.call("input_boolean", "turn_on", service_data, False)

service_data = {"entity_id": "switch.avwasher_relay"}
hass.services.call("switch", "turn_on", service_data, False)

service_data = {"entity_id": "switch.lcd_backlight"}
hass.services.call("switch", "turn_on", service_data, False)



