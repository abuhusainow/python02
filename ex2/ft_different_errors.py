def garden_operations(operation_number: int) -> None:
    faulty_args: list["str"] = ["abc", "0", "/non/existent/file", "42"]
    if operation_number == 0:
        int(faulty_args[0])
    elif operation_number == 1:
        _ = int(faulty_args[3]) / int(faulty_args[1])
    elif operation_number == 2:
        open(faulty_args[2])
    elif operation_number == 3:
        _ = faulty_args[0] + int(faulty_args[3])  # type: ignore[operator]
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation in range(5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
