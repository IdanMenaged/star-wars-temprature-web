class Weather {
    minTemp: Number;
    maxTemp: Number;
    pressure: Number;
    humidity: Number;
    
    constructor(minTemp: Number, maxTemp: Number, pressure: Number, humidity: Number) {
        this.minTemp = minTemp;
        this.maxTemp = maxTemp;
        this.pressure = pressure;
        this.humidity = humidity;

    }
}

const DescriptionToWeather: Array<[string, Weather]> = [
    ['arid', new Weather()]
]