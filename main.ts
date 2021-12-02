input.onButtonPressed(Button.A, function () {
    kitronik_air_quality.clear()
    kitronik_air_quality.measureData()
    kitronik_air_quality.show("Angie's Meteo Board")
    kitronik_air_quality.show("Temperature - :" + kitronik_air_quality.readTemperature(kitronik_air_quality.TemperatureUnitList.C) + " C", 2)
    kitronik_air_quality.show("Pressure ---- :" + kitronik_air_quality.readPressure(kitronik_air_quality.PressureUnitList.Pa) + " Pa", 3)
    kitronik_air_quality.show("Humidity ---- :" + kitronik_air_quality.readHumidity() + " %", 4)
    kitronik_air_quality.show("IAQ Score --> " + kitronik_air_quality.getAirQualityScore(), 6)
    kitronik_air_quality.show("IAQ %     --> " + kitronik_air_quality.getAirQualityPercent(), 7)
    kitronik_air_quality.show("eCo2      -->  " + kitronik_air_quality.readeCO2(), 8)
})
input.onButtonPressed(Button.AB, function () {
    kitronik_air_quality.clear()
    kitronik_air_quality.show(kitronik_air_quality.readDate(), 1)
    kitronik_air_quality.show(kitronik_air_quality.readTime(), 2)
})
kitronik_air_quality.setDate(2, 12, 21)
kitronik_air_quality.setTime(22, 30, 0)
kitronik_air_quality.setupGasSensor()
kitronik_air_quality.calcBaselines()
basic.forever(function () {
	
})
