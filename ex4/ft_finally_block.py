class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def running_water(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing waternig system")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    running_water(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    running_water(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()