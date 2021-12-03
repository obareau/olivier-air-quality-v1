input.onButtonPressed(Button.A, function on_button_pressed_a() {
    kitronik_air_quality.clear()
    kitronik_air_quality.measureData()
    kitronik_air_quality.show("Angie's Meteo Board")
    kitronik_air_quality.show("Temperature - :" + ("" + kitronik_air_quality.readTemperature(kitronik_air_quality.TemperatureUnitList.C)) + " C", 2)
    kitronik_air_quality.show("Pressure ---- :" + ("" + kitronik_air_quality.readPressure(kitronik_air_quality.PressureUnitList.Pa)) + " Pa", 3)
    kitronik_air_quality.show("Humidity ---- :" + ("" + kitronik_air_quality.readHumidity()) + " %", 4)
    kitronik_air_quality.show("IAQ Score --> " + ("" + kitronik_air_quality.getAirQualityScore()), 6)
    kitronik_air_quality.show("IAQ %     --> " + ("" + kitronik_air_quality.getAirQualityPercent()), 7)
    kitronik_air_quality.show("eCo2      -->  " + ("" + kitronik_air_quality.readeCO2()), 8)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    kitronik_air_quality.sendAllData()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    kitronik_air_quality.clear()
    kitronik_air_quality.show("Logging ...")
    for (let index = 0; index < 25; index++) {
        kitronik_air_quality.measureData()
        kitronik_air_quality.logData()
        basic.pause(5000)
    }
    kitronik_air_quality.clearLine(1)
    kitronik_air_quality.show("Logging Complete !", 2)
    basic.pause(2000)
    kitronik_air_quality.clear()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    kitronik_air_quality.show("Erasing Memory", 4)
    kitronik_air_quality.eraseData()
    kitronik_air_quality.clearLine(4)
    kitronik_air_quality.show("Erase Complete", 4)
    basic.pause(2000)
    kitronik_air_quality.clear()
})
kitronik_air_quality.setDate(2, 12, 21)
kitronik_air_quality.setTime(22, 30, 0)
kitronik_air_quality.addProjectInfo("Report", "Meteo-Nice")
kitronik_air_quality.setupGasSensor()
kitronik_air_quality.calcBaselines()
basic.forever(function on_forever() {
    
})
