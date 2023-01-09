const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';
const API_KEY = '141467b3afe32bf42206016b8de79bda';
const UNITS = 'metric';

export default async function getWeather(lat: Number, lon: Number): Promise<Object> {
    const res = await fetch(`${BASE_URL}?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=${UNITS}`);
    return await res.json()['main'];
}