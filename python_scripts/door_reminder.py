# ensure the laundry done flag is set.
name = hass.states.get('input_text.laundryuser').state

telegram_id = ""
if name == "You":
    telegram_id = "123456789"

service_data = {"target":telegram_id, "message": "Whoops, don't forget to leave the washer door open!"}
hass.services.call("telegram_bot", "send_message", service_data, False)

