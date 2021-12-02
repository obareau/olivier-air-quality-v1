def on_button_pressed_a():
    kitronik_air_quality.clear()
    kitronik_air_quality.measure_data()
    kitronik_air_quality.show("Angie's Meteo Board")
    kitronik_air_quality.show("Temperature - :" + str(kitronik_air_quality.read_temperature(kitronik_air_quality.TemperatureUnitList.C)) + " C",
        2)
    kitronik_air_quality.show("Pressure ---- :" + str(kitronik_air_quality.read_pressure(kitronik_air_quality.PressureUnitList.PA)) + " Pa",
        3)
    kitronik_air_quality.show("Humidity ---- :" + str(kitronik_air_quality.read_humidity()) + " %",
        4)
    kitronik_air_quality.show("IAQ Score --> " + str(kitronik_air_quality.get_air_quality_score()),
        6)
    kitronik_air_quality.show("IAQ %     --> " + str(kitronik_air_quality.get_air_quality_percent()),
        7)
    kitronik_air_quality.show("eCo2      -->  " + str(kitronik_air_quality.reade_co2()), 8)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    kitronik_air_quality.clear()
    kitronik_air_quality.show(kitronik_air_quality.read_date(), 1)
    kitronik_air_quality.show(kitronik_air_quality.read_time(), 2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

kitronik_air_quality.set_date(2, 12, 21)
kitronik_air_quality.set_time(22, 30, 0)
kitronik_air_quality.setup_gas_sensor()
kitronik_air_quality.calc_baselines()

def on_forever():
    pass
basic.forever(on_forever)
