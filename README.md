# libfinal - IoT Notification System Library

## Overview

This library, `libfinal`, is designed for an IoT-based platform to monitor pig health through wearable sensors. It provides tools for sending notifications, processing data, and interacting with MQTT brokers for real-time updates. The goal is to assist farmers in monitoring the vitals of pigs, such as temperature and activity levels, to detect swine fever early.

## Features

- **Real-time notifications**: Sends alerts based on sensor data.
- **MQTT Broker integration**: Supports communication with MQTT for IoT applications.
- **Device scalability**: Allows monitoring of multiple devices in a single system.
- **Customizable**: Extendable for additional functionalities.

## Installation

To install the library, clone the repository and use `pip` to install it locally:

```bash
pip install .
```

## Usage

Import the necessary modules from the library to use its features. Below is an example of how to use the library:

```python
from libfinal.iot_notification_system import send_notification

# Example usage
send_notification("Temperature exceeds threshold!", recipient="frank@gmail.com")
```

## Package Structure

```
libfinal/
|-- libfinal/                # Package directory
|   |-- __init__.py          # Marks this directory as a Python package
|   |-- iot_notification_system.py  # Core library module
|-- setup.py                 # Packaging and installation configuration
|-- README.md                # Project documentation
|-- test_library.py          # Example and test cases
```

## Requirements

Ensure the following dependencies are installed:

- Python 3.6 or higher
- Paho MQTT library: `paho-mqtt`

Dependencies are automatically handled if you install the package using `pip`.

## Development

To contribute or modify the library:

1. Clone the repository:
   ```bash
   git clone https://github.com/kalemberi frank/libfinal.git
   ```
2. Install in editable mode:
   ```bash
   pip install -e .
   ```
3. Make changes to the library and test them using `test_library.py`.

## Testing

To ensure the library works as expected, run the `test_library.py` script:

```bash
python test_library.py
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to [DR. ADONES RUKUNDO] for guidance and support in this project.



