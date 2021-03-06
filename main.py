def on_button_pressed_a():
    basic.show_string("" + str(input.temperature()) + "C")
    kitronik_air_quality.clear()
    kitronik_air_quality.measure_data()
    kitronik_air_quality.show("Angie's Meteo Board")
    kitronik_air_quality.show("Temperature - :" + ("" + str(kitronik_air_quality.read_temperature(kitronik_air_quality.TemperatureUnitList.C))) + " C",
        2)
    kitronik_air_quality.show("Pressure ---- :" + ("" + str(kitronik_air_quality.read_pressure(kitronik_air_quality.PressureUnitList.PA))) + " Pa",
        3)
    kitronik_air_quality.show("Humidity ---- :" + ("" + str(kitronik_air_quality.read_humidity())) + " %",
        4)
    kitronik_air_quality.show("IAQ Score --> " + ("" + str(kitronik_air_quality.get_air_quality_score())),
        6)
    kitronik_air_quality.show("IAQ %     --> " + ("" + str(kitronik_air_quality.get_air_quality_percent())),
        7)
    kitronik_air_quality.show("eCo2      -->  " + ("" + str(kitronik_air_quality.reade_co2())),
        8)
    basic.pause(5000)
    kitronik_air_quality.clear()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    kitronik_air_quality.send_all_data()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    kitronik_air_quality.clear()
    kitronik_air_quality.show("Logging ...")
    # set to 1 time just for debugging
    for index in range(1):
        kitronik_air_quality.measure_data()
        kitronik_air_quality.log_data()
        basic.pause(5000)
    kitronik_air_quality.clear_line(1)
    kitronik_air_quality.show("Logging Complete !", 2)
    basic.pause(2000)
    kitronik_air_quality.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("WARNING!")
    kitronik_air_quality.show("Erasing Memory", 4)
    kitronik_air_quality.erase_data()
    kitronik_air_quality.clear_line(4)
    kitronik_air_quality.show("Erase Complete", 4)
    basic.pause(2000)
    kitronik_air_quality.clear()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

statusLEDs = kitronik_air_quality.create_air_quality_zip_display()
statusLEDs.set_brightness(10)
statusLEDs.set_zip_led_color(0, kitronik_air_quality.colors(ZipLedColors.BLUE))
statusLEDs.show()
basic.show_string("" + str((input.light_level())))
basic.clear_screen()
basic.show_string("Bonjour" + "Angie" + "il fait " + str(input.temperature()) + "C")
basic.clear_screen()
basic.show_string("A for Meteo")
basic.clear_screen()
basic.show_string("B for Logging Data")
basic.clear_screen()
basic.show_string("A+B for Sending Data")
basic.clear_screen()
# Date and Time are not really persistant and will be reseted to harcoded values on turn On
kitronik_air_quality.set_date(1, 1, 0)
kitronik_air_quality.set_time(0, 0, 0)
statusLEDs.set_zip_led_color(1, kitronik_air_quality.colors(ZipLedColors.WHITE))
statusLEDs.show()
kitronik_air_quality.add_project_info("Report", "Meteo-Nice")
kitronik_air_quality.setup_gas_sensor()
kitronik_air_quality.calc_baselines()
statusLEDs.set_zip_led_color(2, kitronik_air_quality.colors(ZipLedColors.VIOLET))
statusLEDs.show()