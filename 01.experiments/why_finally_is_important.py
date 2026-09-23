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
        """
            if you remove the return it will execute finally block but also what follows.
            but with the return, we only execute finally block and everything else is ignored.
            The reason is that finally must be executed no matter what!
            Even after a return it will run that final block! This ensures that important things are closed up even after an error.
            The return statement ensures the cycle stops execution completely at the failure point. And Finally makes sure everything else is taken care even after an error.
        """
        return
    finally:
        print("Closing waternig system") 
    print("This will print too if we do not add return in except")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    running_water(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    running_water(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()