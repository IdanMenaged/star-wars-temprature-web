const DescriptionToTemp: Array<[string, number]> = [
    ['arid', 30],
    ['temperate', 7.5],
    ['frozen', -11],
    ['murky', 20]
];

export function getDescByTemp(targetTemp: number) {
    const [initialDesc, initialTemp] = DescriptionToTemp[0];
    let closestDiff: number = Math.abs(targetTemp - initialTemp);
    let closestDesc: string = initialDesc;
    DescriptionToTemp.forEach(([desc, temp]) => {
        const difference = Math.abs(targetTemp - temp);
        if (difference < closestDiff) {
            closestDiff = difference;
            closestDesc = desc;
        }
    });
    return closestDesc;
}