def outer_function():
    """Outer function that contains a nonlocal variable."""
    nonlocal_var = "I am a nonlocal variable"

    def inner_function():
        """Inner function that modifies the nonlocal variable."""
        nonlocal nonlocal_var  # Declare nonlocal_var as nonlocal
        nonlocal_var = "Nonlocal variable modified"
        print("Inside inner_function:", nonlocal_var)

    inner_function()  # Call the inner function
    print("Inside outer_function:", nonlocal_var)

# Call the outer function
outer_function()
