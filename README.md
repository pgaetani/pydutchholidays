# Dutch Holidays

This project provides a Python library to retrieve Dutch holidays.

## Installation

To install the Dutch Holidays library, you can use pip:

```bash
pip install pydutchholidays
```

## Usage

Here is an example of how to use the library to calculate Dutch holidays:

```python
from dutch_holidays import get_dutch_holidays

# Get all holidays for the current year
all_holidays = get_dutch_holidays()

# Print all holidays
for holiday_name, holiday_dates in all_holidays.items():
    print(f"{holiday_name}: {holiday_dates}")
```

## Features

- Calculate Dutch holidays for a specified year and province.
- Support for all provinces in the Netherlands.
- Easy to use and integrate into your projects.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.