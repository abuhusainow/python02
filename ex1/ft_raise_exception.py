def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp} is too hot for plants (max 40°C)")
    elif temp < 0:
        raise Exception(f"{temp} is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===", end="\n\n")
    str_int: list[str] = ["25", "abc", "100", "-50"]

    for item in str_int:
        print(f"Input data is {item}")
        # führt den Code aus um schaut, ob es einen Fehler gibt. ->
        # input_temperature() wird uns einen Fehler für "abc" geben.
        try:
            print(f"Temperature is now {input_temperature(item)}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print()


if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didn't crash!")
