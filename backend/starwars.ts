const API_URL = 'https://swapi.dev/api/planets';

export default async function getPlanets(): Promise<Object> {
    const res = await fetch(API_URL);
    return await res.json()
}