import time
import math

def time_it(fn, *args, repetitions=1, **kwargs):
    if repetitions < 0:
        raise ValueError("Repetition should be positive number")
    start_time = time.time()
    for _ in range(repetitions):
        fn(*args, **kwargs)
    end_time = time.time()
    return (end_time - start_time) / repetitions if repetitions > 0 else 0



def squared_power_list(number, *args, start=0, end=5, **kwargs):
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")
    if number > 10:
        raise ValueError("Value of number should be less than 10")
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")
    if start > end:
        raise ValueError("Value of start should be less than end")

    # Raise an error if there's any unwanted positional argument
    if args:
        raise TypeError("squared_power_list function takes maximum 1 positional arguments, more provided")

    # Raise an error if there's any unwanted keyword argument
    if any(k not in ['start', 'end'] for k in kwargs):
        raise TypeError("squared_power_list function takes maximum 2 keyword/named arguments, more provided")

    return [number ** i for i in range(start, end)]




def polygon_area(length, sides=3):
    if not isinstance(length, (int, float)) or isinstance(length, bool):
        raise TypeError("Length should be a positive number")
    if length <= 0:
        raise ValueError("Length should be greater than 0")
    if not isinstance(sides, int) or isinstance(sides, bool):
        raise TypeError("Sides should be an integer")
    if sides not in [3, 4, 5, 6]:
        raise ValueError("Sides should be between 3 and 6")

    if sides == 3:
        return (math.sqrt(3) / 4) * (length ** 2)
    elif sides == 4:
        return length ** 2
    elif sides == 5:
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * length ** 2
    elif sides == 6:
        return ((3 * math.sqrt(3)) / 2) * length ** 2



def temp_converter(temp, *args, temp_given_in='f', **kwargs):
    # Check for unwanted positional and keyword arguments
    if len(args) > 0:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 1:
        raise TypeError("temp_converter function takes maximum 1 keyword/named arguments, more provided")

    # Type checks for temp
    if not isinstance(temp, (int, float)) or isinstance(temp, bool):
        raise TypeError("Temperature should be a number")

    # Check for valid temp_given_in value
    if not isinstance(temp_given_in, str):
        raise TypeError("Charcater string expected")
    if temp_given_in.lower() not in ['f', 'c']:
        raise ValueError("Only f or c is allowed")

    temp_given_in = temp_given_in.lower()

    # Conversion logic
    if temp_given_in == 'f':
        if temp < -459.67:
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
        return (temp - 32) * 5.0 / 9.0
    elif temp_given_in == 'c':
        if temp < -273.15:
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
        return (temp * 9.0 / 5.0) + 32




def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    # Check for unwanted positional and keyword arguments
    if len(args) > 0:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 2:
        raise TypeError("speed_converter function takes maximum 2 keyword/named arguments, more provided")

    # Type checks for speed
    if not isinstance(speed, (int, float)) or isinstance(speed, bool):
        raise TypeError("Speed can be int or float type only")

    # Value checks for speed
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")

    # Type checks for dist and time
    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError("Charcater string expected")

    # Define valid units and conversions
    distance_units = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yrd': 1093.61}
    time_units = {'ms': 3600000, 's': 3600, 'min': 60, 'hr': 1, 'day': 1 / 24}

    # Convert units to lowercase for case insensitivity
    dist = dist.lower()
    time = time.lower()

    # Check for valid units
    if dist not in distance_units:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if time not in time_units:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")

    # Perform conversion
    distance_conversion = distance_units[dist]
    time_conversion = time_units[time]
    converted_speed = (speed * distance_conversion) / time_conversion

    return converted_speed








