class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def testing_errors() -> None:
    print("=== Custom Garde Errors Demo ===\n")
    print("Testing PlantError....")
    try:
        raise_plant_error()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors...")
    for garden_error in (raise_plant_error, raise_water_error):
        try:
            garden_error()
        except GardenError as err:
            print(f"Caught GardenError: {err}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    testing_errors()
