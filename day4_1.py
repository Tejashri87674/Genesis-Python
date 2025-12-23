class InvalidDataTypeError(Exception):
    """Custom exception for invalid data types in a list."""

    def __init__(self, invalid_item, expected_type):
        self.invalid_item = invalid_item
        self.expected_type = expected_type
        super().__init__(f"Invalid item '{invalid_item}'. Expected type: {expected_type.__name__}")
 
    # Custom method to suggest correction
    def suggest_fix(self):
        return f"Please replace '{self.invalid_item}' with a {self.expected_type.__name__} value."


# Function to validate list elements
def validate_integer_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")

    for item in data:
        if not isinstance(item, int):
            # Raise custom exception with details
            raise InvalidDataTypeError(item, int)

    return "Validation successful! All elements are integers."


# Test the function
try:
    numbers = [10, 20, 'thirty', 40]
    print(validate_integer_list(numbers))
except TypeError as te:
        # Handles the case where the input is not a list.
        print(f"TypeError: {te}")
except InvalidDataTypeError as e:
    print(e)  # Default error message
    print(e.suggest_fix())  # Using custom method
except Exception as e:
    # Catch‑all for any other unexpected errors.
    print(f"An unexpected error occurred: {e}")












'''
Design a system to monitor environmental conditions using different types of sensors.

Base Class: Sensor
• Attributes: 
o sensor_id (string)
o location (string)
o reading (float)
o unit (string)
o alerts (list of strings): e.g., ["Low Battery", "Signal Lost"]
o metadata (dict): e.g.{"manufacturer": "ABC Corp", "model": "X100", "warranty_years": 2}
• Methods: 
o Initialize attributes.
o Getters and setters.
o __repr__() for readable representation.
o status_message(): Default message: "Sensor operational" (to be overridden).

Derived Class 1: TemperatureSensor
• Additional Attributes: 
o historical_readings (list of floats): e.g., [22.5, 23.0, 21.8]
o calibration_values (dict): e.g.{"offset": 0.5, "scale": 1.02}
• Methods: 
o Override status_message(): "Temperature Sensor: Normal" if reading between 15°C and 35°C else "Temperature Sensor: Alert".
o average_temperature(): Compute average from historical_readings.
o apply_calibration(): Adjust reading using calibration_values.

Derived Class 2: HumiditySensor
• Additional Attributes: 
o sensor_age_years (int)
o maintenance_log (list of strings): e.g., ["Filter replaced", "Firmware updated"]
o performance_metrics (dict): e.g.{"accuracy": 98.5, "response_time_ms": 120}
• Methods: 
o Override status_message(): "Humidity Sensor: Optimal" if reading between 30% and 60% else "Humidity Sensor: Alert".
o predict_remaining_life(): Remaining life = max(0, 10 - sensor_age_years).
o last_maintenance(): Return last entry from maintenance_log.

Create Objects
• Create at least 3 TemperatureSensor objects and 2 HumiditySensor objects.
• Store all objects in a single list called sensors.

Function 1: filter_sensors_with_alerts(sensors)
• Input: sensors (list of Sensor objects)
• Task: Return all sensors that have at least one alert.
• Output: List of Sensor objects with non-empty alerts.

Function 2: sort_sensors_by_reading(sensors)
• Input: sensors (list of Sensor objects)
• Task: Sort sensors in ascending order of their reading.
• Output: Sorted list of Sensor objects.

Function 3: extract_sensor_ids(sensors)
• Input: sensors (list of Sensor objects)
• Task: Extract all sensor IDs into a list.
• Output: List of strings (sensor IDs).

Function 4: compute_average_reading(sensors)
• Input: sensors (list of Sensor objects)
• Task: Compute the average of all sensor readings.
• Output: Float (average reading).

Function 5: add_alert_to_sensor(sensor, alert)
• Input: 
o sensor → A single Sensor object (or derived class object).
o alert → String representing the alert message (e.g., "Low Battery").
• Task: 
o Add the given alert to the sensor’s alerts list only if it is not already present.
• Output: 
o Updated Sensor object with the new alert added.
• Constraints: 
o Must handle: 
 Duplicate prevention.
 Empty alert string (ignore if blank).

Function 6: display_all_sensors
• Name: display_all_sensors(sensors)
• Input: 
o sensors → List of Sensor objects (including derived classes).
• Task: 
o Print details of each sensor in the list 
o Include sensor type (TemperatureSensor or HumiditySensor).
• Output: 
o Printed representation of all sensor objects.
'''
 
 # --------------------------------------------------------------
#   Sensor hierarchy demo with utility functions
# --------------------------------------------------------------
from typing import List, Dict
 
# Custom Exceptions
class SensorError(Exception):
    """Base class for all sensor‑related errors."""
 
 
class InvalidReadingError(SensorError):
    """Raised when an attempt is made to set a reading that is not numeric."""
    def __init__(self, reading, message: str = "Invalid sensor reading"):
        super().__init__(f"{message}: {reading}")
        self.reading = reading
 
 
class AlertError(SensorError):
    """Raised when an alert operation fails (e.g., duplicate alerts)."""
    pass

# ----------------------------------------------------------------------
# Base Class: Sensor
# ----------------------------------------------------------------------
class Sensor:
    """
    Basic sensor representation.

    Attributes
    ----------
    sensor_id : str
        Unique identifier of the sensor.
    location : str
        Physical location of the sensor.
    reading : float
        Current measurement value.
    unit : str
        Unit of the reading (e.g., "°C", "%").
    alerts : list
        List of active alerts.
    metadata : dict
        Arbitrary meta‑information (manufacturer, model, etc.).
    """

    def __init__(
        self,
        sensor_id: str,
        location: str,
        reading: float,
        unit: str,
        alerts: list = None,
        metadata: dict = None,
    ) -> None:
        self.sensor_id: str = sensor_id
        self.location: str = location
        self.reading: float = reading
        self.unit: str = unit
        self.alerts: list = alerts or []
        self.metadata: dict = metadata or {}

    def __repr__(self) -> str:
        """Return an informative string representation."""
        # return (
        #     f"{self.__class__.__name__}"
        #     f"(ID={self.sensor_id}, Location={self.location}, "
        #     f"Reading={self.reading}{self.unit})"
        # )
        return f"{self.__dict__}"

    def status_message(self) -> str:
        """Default status subclasses override this."""
        return "Sensor operational"

    # ------------------------------------------------------------------
    # Getters / Setters
    # ------------------------------------------------------------------
    def get_reading(self) -> float:
        """Return the current reading."""
        return self.reading

    def set_reading(self, value: float) -> None:
        """
        Update the reading.

        Raises
        ------
        InvalidReadingError
            If ``value`` is not a numeric type.
        """
        if not isinstance(value, (int, float)):
            raise InvalidReadingError(value, "Reading must be numeric")
        self.reading = float(value)


# ----------------------------------------------------------------------
# Derived Class: TemperatureSensor
# ----------------------------------------------------------------------
class TemperatureSensor(Sensor):
    """
    Temperature‑specific sensor.

    Additional Attributes
    ---------------------
    historical_readings : list
        Past temperature values used for analytics.
    calibration_values : dict
        Calibration parameters (e.g., offset, scale).
    """

    def __init__(
        self,
        sensor_id: str,
        location: str,
        reading: float,
        unit: str,
        alerts: list,
        metadata: dict,
        historical_readings: list = None,
        calibration_values: dict = None,
    ) -> None:
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.historical_readings: list = historical_readings or []
        self.calibration_values: dict = calibration_values or {"offset": 0.0, "scale": 1.0}

    # ------------------------------------------------------------------
    # Overridden behaviour
    # ------------------------------------------------------------------
    def status_message(self) -> str:
        """Temperature‑specific status based on a comfortable range."""
        if 15 <= self.reading <= 35:
            return "Temperature Sensor: Normal"
        return "Temperature Sensor: Alert"

    # ------------------------------------------------------------------
    # Temperature‑specific utilities
    # ------------------------------------------------------------------
    def average_temperature(self) -> float:
        """Return the average of ``historical_readings`` (0 if empty)."""
        if not self.historical_readings:
            return 0.0
        return sum(self.historical_readings) / len(self.historical_readings)

    def apply_calibration(self) -> None:
        """
        Adjust ``self.reading`` in‑place using calibration data.

        The formula: (reading + offset) * scale
        """
        offset = self.calibration_values.get("offset", 0.0)
        scale = self.calibration_values.get("scale", 1.0)
        self.reading = (self.reading + offset) * scale


# ----------------------------------------------------------------------
# Derived Class: HumiditySensor
# ----------------------------------------------------------------------
class HumiditySensor(Sensor):
    """
    Humidity‑specific sensor.

    Additional Attributes
    ---------------------
    sensor_age_years : int
        Age of the sensor in years.
    maintenance_log : list
        Record of maintenance activities.
    performance_metrics : dict
        Metrics such as accuracy and response time.
    """

    def __init__(
        self,
        sensor_id: str,
        location: str,
        reading: float,
        unit: str,
        alerts: list,
        metadata: dict,
        sensor_age_years: int,
        maintenance_log: list = None,
        performance_metrics: dict = None,
    ) -> None:
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.sensor_age_years: int = sensor_age_years
        self.maintenance_log: list = maintenance_log or []
        self.performance_metrics: dict = performance_metrics or {}

    # ------------------------------------------------------------------
    # Overridden behaviour
    # ------------------------------------------------------------------
    def status_message(self) -> str:
        """Humidity‑specific status based on an optimal range."""
        if 30 <= self.reading <= 60:
            return "Humidity Sensor: Optimal"
        return "Humidity Sensor: Alert"

    # ------------------------------------------------------------------
    # Humidity‑specific utilities
    # ------------------------------------------------------------------
    def predict_remaining_life(self) -> int:
        """
        Simple predictive model: assume a 10‑year design life.

        Returns
        -------
        int
            Remaining years (floor at 0).
        """
        return max(0, 10 - self.sensor_age_years)

    def last_maintenance(self):
        """Return the most recent maintenance entry, or ``None`` if log is empty."""
        return self.maintenance_log[-1] if self.maintenance_log else None

 
# ----------------------------------------------------------------------
# Helper Functions operating on a list of Sensor objects
# ----------------------------------------------------------------------
def filter_sensors_with_alerts(sensors: List[Sensor]) -> List[Sensor]:
    """
    Return only sensors that have at least one active alert.

    Parameters
    ----------
    sensors : list of Sensor

    Returns
    -------
    list of Sensor
    """
    return [sensor for sensor in sensors if sensor.alerts]


def sort_sensors_by_reading(sensors: List[Sensor]) -> List[Sensor]:
    """
    Sort sensors in ascending order of their current reading.

    Parameters
    ----------
    sensors : list of Sensor

    Returns
    -------
    list of Sensor
    """
    return sorted(sensors, key=lambda s: s.reading)


def extract_sensor_ids(sensors: List[Sensor]) -> List[str]:
    """
    Collect the ``sensor_id`` of each sensor in the supplied list
    """
    return [sensor.sensor_id for sensor in sensors]


def compute_average_reading(sensors: List[Sensor]) -> float:
    """
    Compute the arithmetic mean of all sensor readings.
    Returns 0.0 if the list is empty.
    """
    if not sensors:
        return 0.0
    total = sum(sensor.reading for sensor in sensors)
    return total / len(sensors)
 











 def main() -> None:
    """Main function."""
    inventory = []
    add_vehicle(inventory, "ABC123", "Car", "Toyota", 2020, "Red", "Gasoline")
    add_vehicle(inventory, "DEF456", "Truck", "Ford", 2015, "Blue", "Diesel")
    display_vehicle_info(inventory, "ABC123")
    record_sales(inventory, "ABC123", "2022-01-01", 20000, "John Doe")
    display_sales_history(inventory, "ABC123")
    record_maintenance(inventory, "DEF456", "2022-02-01", "Oil change", 100)
    display_maintenance_history(inventory, "DEF456")
    

if __name__ == "__main__":
    main()
 