// class Weather {
//     minTemp: Number;
//     maxTemp: Number;
//     pressure: Number;
//     humidity: Number;
    
//     constructor(minTemp: Number, maxTemp: Number, pressure: Number, humidity: Number) {
//         this.minTemp = minTemp;
//         this.maxTemp = maxTemp;
//         this.pressure = pressure;
//         this.humidity = humidity;
//     }
// }

interface Weather {
    minTemp: Number,
    maxTemp: Number,
    pressure: Number,
    humidity: Number
}

const DescriptionToWeather: Array<[string, Weather]> = [
    ['arid', { minTemp: -30, maxTemp: 130,  }]
]