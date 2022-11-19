import swapi

def orgonize() -> dict[str, list[str]]:
    planets = swapi.get_all('planets')
    out = {}
    for planet in planets:
        key = planet.climate
        if key not in out.keys():
            out[key] = []
        out[key].append(planet.name)
    return out