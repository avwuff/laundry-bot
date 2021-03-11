# ensure the laundry done flag is set.
service_data = {"entity_id": "input_boolean.laundrydone"}
hass.services.call("input_boolean", "turn_on", service_data, False)

# TODO: mark when it finished?
name = hass.states.get('input_text.laundryuser').state

startedat = hass.states.get('input_datetime.laundrystartedat').state
# calculate the time deltas
start = datetime.datetime.strptime(startedat, '%Y-%m-%d %H:%M:%S')
now = datetime.datetime.now()
delta = now - start
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
diff = '{:02}:{:02}'.format(int(hours), int(minutes))

# Send alerts here to the relevant people.
service_data = {"entity_id":"media_player.kitchen_display", "message": "Hey {}, the laundry is done!".format(name)}
hass.services.call("tts", "google_translate_say", service_data, False)

telegram_id = ""
if name == "You":
    telegram_id = "123456789" # Put your own Telegram ID here

service_data = {"target":telegram_id, "message": "Hey {}, the laundry finished.\nTime taken: {}!".format(name, diff)}
hass.services.call("telegram_bot", "send_message", service_data, False)

