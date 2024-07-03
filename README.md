[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z8haBqsC)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15360594&assignment_repo_type=AssignmentRepo)

# Python Utility Functions

This repository contains a collection of Python utility functions designed to perform various mathematical and conversion operations. The functions are implemented in `sessions5.py` and thoroughly tested using `pytest` in `test_sessions5.py`.

## Functions

### 1. `time_it(fn, *args, repetitions=1, **kwargs)`

This function measures the average time taken to execute a given function a specified number of times.

**Parameters:**
- `fn`: The function to be timed.
- `*args`: Positional arguments to be passed to the function.
- `repetitions`: The number of times the function should be executed (default is 1).
- `**kwargs`: Keyword arguments to be passed to the function.

**Returns:**
- The average time taken to execute the function.

**Example:**
```python
def sample_function(x):
    return x * x

average_time = time_it(sample_function, 5, repetitions=100)
print(f"Average time taken: {average_time}")
```

### 2. `squared_power_list(number, start=0, end=5)`

This function returns a list of the given number raised to the power of integers from `start` to `end`.

**Parameters:**
- `number`: The base number to be raised to the power.
- `start`: The starting power (default is 0).
- `end`: The ending power (default is 5).

**Returns:**
- A list of the number raised to the power of integers from `start` to `end`.

**Example:**
```python
result = squared_power_list(2, start=1, end=4)
print(result) # Output: [2, 4, 8]
```

### 3. `polygon_area(length, sides=3)`

This function calculates the area of a regular polygon with the specified number of sides.

**Parameters:**
- `length`: The length of each side of the polygon.
- `sides`: The number of sides of the polygon (default is 3). Valid values are 3, 4, 5, and 6.

**Returns:**
- The area of the polygon.

**Example:**
```python
area = polygon_area(10, sides=4)
print(area) # Output: 100
```

### 4. `temp_converter(temp, temp_given_in='f')`

This function converts temperature between Celsius and Fahrenheit.

**Parameters:**
- `temp`: The temperature value to be converted.
- `temp_given_in`: The unit of the given temperature ('f' for Fahrenheit, 'c' for Celsius).

**Returns:**
- The converted temperature value.

**Example:**
```python
celsius = temp_converter(32, temp_given_in='f')
print(celsius) # Output: 0.0
```

### 5. `speed_converter(speed, dist='km', time='min')`

This function converts speed from km/h to different units.

**Parameters:**
- `speed`: The speed value to be converted.
- `dist`: The unit of distance ('km', 'm', 'ft', 'yrd').
- `time`: The unit of time ('ms', 's', 'min', 'hr', 'day').

**Returns:**
- The converted speed value.

**Example:**
```python
converted_speed = speed_converter(100, dist='km', time='hr')
print(converted_speed) # Output: 100.0
```

## Running Tests

To run the tests, use the following command:

```bash
pytest test_sessions5.py
```

Make sure to have `pytest` installed in your environment.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgments

Thanks to all the contributors and open-source projects that inspired and helped in the development of these utility functions.

## Additional Details

### General Usage Instructions

These functions are intended to simplify various tasks such as measuring the execution time of functions, generating lists of numbers raised to specific powers, calculating areas of regular polygons, converting temperatures, and converting speeds. They can be used in educational projects, scientific calculations, and any other applications requiring these functionalities.

### Performance Considerations

The `time_it` function is particularly useful for performance testing and optimization. By measuring the execution time of a function over multiple repetitions, it helps identify bottlenecks and optimize code efficiency.

### Mathematical Functions

Functions like `squared_power_list` and `polygon_area` provide easy-to-use tools for mathematical calculations. They ensure input validation and handle edge cases to prevent errors during execution.

### Conversion Functions

The `temp_converter` and `speed_converter` functions facilitate unit conversions, making it easy to switch between different measurement systems. These functions handle various units and ensure accurate conversions based on standard formulas.

### Installation

To use these functions, clone the repository and import the required functions into your project:

```bash
git clone https://github.com/yourusername/python-utility-functions.git
```

### Example Projects

Here are a few example projects where these functions can be applied:

- **Scientific Research**: Use `squared_power_list` and `polygon_area` for mathematical modeling and simulations.
- **Weather Analysis**: Utilize `temp_converter` to process and analyze temperature data from different sources.
- **Speed Tracking**: Apply `speed_converter` in applications tracking and analyzing movement speeds in various units.

By following these instructions and utilizing the provided functions, you can enhance your projects with reliable and efficient utility functions.
