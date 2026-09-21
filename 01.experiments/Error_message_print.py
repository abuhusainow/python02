try:
    x = float("asdb")
except ValueError as e:
    # Read the specific message
    print(f"Error details: {e}")

    # Access the tuple of arguments passed to the exception
    print(f"Arguments: {e.args}")

    num = "Python"
