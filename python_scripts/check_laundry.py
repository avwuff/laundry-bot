# see if the laundry is active.
line1 = ""
line2 = ""
line3 = ""
line4 = ""

active = hass.states.get('input_boolean.laundryinuse').state
done = hass.states.get('input_boolean.laundrydone').state
name = hass.states.get('input_text.laundryuser').state

if active == "on":

    if done == 'on':
        #        12345678901234567890
        line1 = " Laundry Finished!  "
        line2 = "For: {}".format(name)
        line3 = ""
        line4 = "Press Black to clear"

    else:
        # Check to see if the laundry is done.
        # what is the current wattage?
        wattage = hass.states.get('sensor.avwasher_wattage').state
        zerocount = float(hass.states.get('input_number.laundryzerocount').state)
        startedat = hass.states.get('input_datetime.laundrystartedat').state
        
        # calculate the time deltas
        start = datetime.datetime.strptime(startedat, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        
        delta = now - start
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        diff = '{:02}:{:02}'.format(int(hours), int(minutes))

        #        12345678901234567890
        line1 = "Washing for {}".format(name)
        line2 = "Duration {}".format(diff)

        line4 = "Wattage: {}".format(wattage)
        
        # If the wattage is zero for more than 5 counts, it means the wash is done.
        if float(wattage) < 2.1:
            
            zerocount = zerocount + 1.0
            if zerocount > 5:
                # Laundry must be done!
                service_data = {"entity_id": "input_boolean.laundrydone"}
                hass.services.call("input_boolean", "turn_on", service_data, False)
                
                hass.services.call("python_script", "washer_done", {}, False)
                
            else:
                service_data = {"entity_id": "input_number.laundryzerocount", "value": zerocount}
                hass.services.call("input_number", "set_value", service_data, False)
else:

    #        12345678901234567890
    line1 = "     AvLaundry      "
    line2 = "                    "
    line3 = "   Ready to wash?   "
    line4 = " Press your button! "


# display it.
service_data = {"entity_id": "input_text.laundryline1", "value": line1}
hass.services.call("input_text", "set_value", service_data, False)

service_data = {"entity_id": "input_text.laundryline2", "value": line2}
hass.services.call("input_text", "set_value", service_data, False)

service_data = {"entity_id": "input_text.laundryline3", "value": line3}
hass.services.call("input_text", "set_value", service_data, False)

service_data = {"entity_id": "input_text.laundryline4", "value": line4}
hass.services.call("input_text", "set_value", service_data, False)
