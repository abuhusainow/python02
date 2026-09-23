# 1. THE BLUEPRINT (Subclass)
class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self.problem_time = "12:00 PM"


def check_soil_moisture(moisture_level: int) -> None:
    if moisture_level < 10:
        # Step A: Instantiate the error object
        # error_object = PlantError("Soil is dangerously dry!")

        # Step B: Sound the alarm
        raise PlantError("Soil is dangerously dry!")


try:
    check_soil_moisture(5)
except PlantError as e:
    print(e)
