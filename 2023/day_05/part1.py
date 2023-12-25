from pathlib import Path
from math import inf

from dataclasses import dataclass


@dataclass
class Range:
    src_start: int
    dst_start: int
    length: int

    def is_in_src_range(self, n: int) -> bool:
        return self.src_start <= n < self.src_start + self.length

    def get_dst(self, __src: int) -> int:
        return self.dst_start + __src - self.src_start


@dataclass
class RangeContainer:
    mappings: list[Range]

    def get(self, __key: int, __default: int) -> int:
        for mapping in self.mappings:
            if mapping.is_in_src_range(__key):
                return mapping.get_dst(__key)

        return __default


# Define type aliases
Seeds = list[int]
SeedToSoilMap = RangeContainer
SoilToFertilizerMap = RangeContainer
FertilizerTowWaterMap = RangeContainer
WaterToLightMap = RangeContainer
LightToTemperatureMap = RangeContainer
TemperatureToHumidityMap = RangeContainer
HumidityToLocationMap = RangeContainer


def lowest_location(
    seeds: Seeds,
    seed_to_soil: SeedToSoilMap,
    soil_to_fertilizer: SoilToFertilizerMap,
    fertilizer_to_water: FertilizerTowWaterMap,
    water_to_light: WaterToLightMap,
    light_to_temperature: LightToTemperatureMap,
    temperature_to_humidity: TemperatureToHumidityMap,
    humidity_to_location: HumidityToLocationMap,
) -> int:
    lowest_location = inf

    for seed in seeds:
        soil = seed_to_soil.get(seed, seed)
        fertilizer = soil_to_fertilizer.get(soil, soil)
        water = fertilizer_to_water.get(fertilizer, fertilizer)
        light = water_to_light.get(water, water)
        temperature = light_to_temperature.get(light, light)
        humidity = temperature_to_humidity.get(temperature, temperature)
        location = humidity_to_location.get(humidity, humidity)

        lowest_location = min(location, lowest_location)

    return lowest_location


def runner(input: Path) -> None:
    seeds: list[int] = []
    seed_to_soil: SeedToSoilMap = RangeContainer(mappings=[])
    soil_to_fertilizer: SoilToFertilizerMap = RangeContainer(mappings=[])
    fertilizer_to_water: FertilizerTowWaterMap = RangeContainer(mappings=[])
    water_to_light: WaterToLightMap = RangeContainer(mappings=[])
    light_to_temperature: LightToTemperatureMap = RangeContainer(mappings=[])
    temperature_to_humidity: TemperatureToHumidityMap = RangeContainer(mappings=[])
    humidity_to_location: HumidityToLocationMap = RangeContainer(mappings=[])

    def read_map(map: RangeContainer, file) -> None:
        file.readline()  # read title

        ranges: list[Range] = []

        while range_line := file.readline():
            if range_line in ["\n", ""]:
                break

            [destination_start, source_start, length] = [
                int(x.strip()) for x in range_line.strip().split()
            ]

            ranges.append(
                Range(
                    src_start=source_start, dst_start=destination_start, length=length
                )
            )

        map.mappings = ranges

    with input.open("r") as file:
        # Read the seeds
        seeds = [int(s) for s in file.readline().strip().split(":")[1].strip().split()]
        file.readline()  # read whitespace line

        # Read the maps
        read_map(seed_to_soil, file)
        read_map(soil_to_fertilizer, file)
        read_map(fertilizer_to_water, file)
        read_map(water_to_light, file)
        read_map(light_to_temperature, file)
        read_map(temperature_to_humidity, file)
        read_map(humidity_to_location, file)

    return lowest_location(
        seeds=seeds,
        seed_to_soil=seed_to_soil,
        soil_to_fertilizer=soil_to_fertilizer,
        fertilizer_to_water=fertilizer_to_water,
        water_to_light=water_to_light,
        light_to_temperature=light_to_temperature,
        temperature_to_humidity=temperature_to_humidity,
        humidity_to_location=humidity_to_location,
    )
