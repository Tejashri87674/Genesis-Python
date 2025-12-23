import re
 
text = "Hello World"
pattern = r"Hello"
match = re.match(pattern, text)
if match:
    print("Match found at the beginning!") #Output: Match found at the beginning!
else:
    print("No match at the beginning.")
 
text = "apple,banana,orange"
pattern = r","
fruits = re.split(pattern, text)
print(fruits)  # Output: ['apple', 'banana', 'orange']
 
text = "The quick brown fox."
pattern = r"Fox"
match = re.search(pattern, text)
if match:
    print("Found 'fox' in the string!") #Output: Found 'fox' in the string!
else:
    print("'fox' not found.")
 
text = "abc123def456ghi"
pattern = r"\d+"  # One or more digits
numbers = re.findall(pattern, text)
print(numbers)  # Output: ['123', '456']
 
vin_prefix = "WMI"
vin = "WMI1234567890123"
pattern = r"^WMI"  # Matches if the string *starts* with "WMI"
match = re.match(pattern, vin)
if match:
    print("VIN starts with WMI")  # Output: VIN starts with WMI
else:
    print("VIN does not start with WMI")
 
 
part_numbers = "12345-67890,98765-43210,55555-11111"
pattern = r"[, -]"  # Split on comma, space, or hyphen
parts = re.split(pattern, part_numbers)
print(parts)  # Output: ['12345', '67890', '98765', '43210', '55555', '11111']
 
 
 
vin = "WMI12345678901237"
pattern = r"^[A-Z0-9]{17}$"  # VINs are typically 17 characters, alphanumeric
# This checks if the VIN has the correct length and contains only alphanumeric characters.
match = re.match(pattern, vin)
if match:
    print("Valid VIN format.")
else:
    print("Invalid VIN format.")
 
 
 
 
license_plate = "ABC1234"
pattern = r"^[A-Z]{3}\d{4}$"  # Example: 3 letters followed by 4 digits (e.g., California)
match = re.match(pattern, license_plate)
if match:
    print("License plate matches the pattern.")
else:
    print("License plate does not match the pattern.")
 
 
part_number = "1234567890"  # Example part number
pattern = r"^\d{10}$"  # Example: 10 digits
match = re.match(pattern, part_number)
if match:
    print("Valid part number format.")
else:
    print("Invalid part number format.")
 
error_log = "P0300, P0301, P0302, P0300, P34, p567"  # Multiple DTCs
pattern = r"P\d{4}"  # Matches DTCs (P followed by 4 digits)
dtcs = re.findall(pattern, error_log)
print(dtcs)  # Output: ['P0300', 'P0301', 'P0302', 'P0300']
 
 
result = re.search(r'analytics','AV analytics Vidhya aa AV')
print(result.start())
print(result.end())
 





  
import re
 
# Q1. Check if VIN is valid in length (17 characters)
vin = "1FVCP1U56XYZ123456"
if len(vin) == 17:
    print("VIN is valid in length")
else:
    print("VIN is invalid in length")
 
# Extract all license plates (MH 12 AB 1234 format) from this text.
text = "The vehicle's license plate is MH 12 AB 1234"
pattern = r"\b[A-Z]{2}\s\d{2}\s[A-Z]{2}\s\d{4}\b"
match = re.search(pattern, text)
if match:
    print("License Plate:", match.group(0))
 
# Is this string a valid date (YYYY-MM-DD)?
date_string = "2023-10-27"
pattern = r"^\d{4}-\d{2}-\d{2}$"
if re.match(pattern, date_string):
    print("Valid date format")
else:
    print("Invalid date format")
 
# Extract all Diagnostic Trouble Codes (DTCs) from this log.
log_text = "Detected DTCs: U0100, C1234, B0500, P0301"
pattern = r"\b[PUBC]\d{4}\b"  # Matches P, U, B, or C followed by 4 digits
dtcs = re.findall(pattern, log_text)
print("DTCs:", dtcs)
 
# Find Email Addresses in a Log File
log_content = "Report sent to user@example.com and support@kpit.com."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, log_content)
print("Email Addresses:", emails)
 
# Validate VIN with complex check (example: alphanumeric only, length 17)
vin = "1FVCP1U56XYZ123456"
pattern = r"^[A-HJ-NPR-Z0-9]{17}$"  # Excludes I, O, Q
if re.match(pattern, vin):
    print("VIN is valid format")
else:
    print("VIN is invalid format")
 
# Extract vehicle speed and RPM from CAN bus message.
can_message = "Speed: 65.2 km/h, RPM: 2500"
pattern = r"Speed:\s([\d.]+)\skm/h,\sRPM:\s(\d+)"
match = re.search(pattern, can_message)
if match:
    speed = float(match.group(1))
    rpm = int(match.group(2))
    print("Speed:", speed, "km/h")
    print("RPM:", rpm)
 
# Extract all part numbers (10 digits + 3 letters) from this list.
text = "Ordered part number 1234567890ABC and another part 9876543210DEF."
pattern = r"\b\d{10}[A-Z]{3}\b"
part_numbers = re.findall(pattern, text)
print("Part Numbers:", part_numbers)
 
# How many times does error code E123 appear in this log data?
log_data = "Error code E123 encountered.  Another E123 found later. No other errors."
pattern = r"\bE123\b"
matches = re.findall(pattern, log_data)
print("Number of E123 errors:", len(matches))
 
# Parse key-value pairs from the data string
data_string = "EngineTemp=90.5,OilPressure=50,VehicleSpeed=80.2"
pattern = r"(\w+)=(\d+(?:\.\d+)?)"
matches = re.findall(pattern, data_string)
data = dict(matches)
print("Parsed Data:", data)
 
# Sanitize input string by removing special characters.
input_string = "Vehicle Data: !@#$%^&*()_+=-`~[]\\{}|;':\",./<>?"
pattern = r"[^a-zA-Z0-9\s]"
sanitized_string = re.sub(pattern, "", input_string)
print("Sanitized String:", sanitized_string)
 
# Does this string contain the word "ABS"?
text = "The car has an ABS system."
pattern = r"\bABS\b"
if re.search(pattern, text):
    print("ABS found")
else:
    print("ABS not found")
 
# Find all URLs in this text.
text = "Check out our website at https://www.kpit.com and more info at http://example.com/docs"
pattern = r"https?://[^\s]+"
urls = re.findall(pattern, text)
print("URLs:", urls)
 
# Replace multiple spaces with single spaces in this string.
text = "This   string  has   too  many   spaces."
pattern = r"\s+"
cleaned_text = re.sub(pattern, " ", text)
print("Cleaned Text:", cleaned_text)
 
# Does this string contain only numbers?
string1 = "12345"
pattern = r"^\d+$"
if re.match(pattern, string1):
    print(f"{string1} contains only numbers")
else:
    print(f"{string1} contains non-numeric characters")
 
# Extract all numbers from this text.
text = "The car's speed is 60 km/h and the engine RPM is 2500."
pattern = r"\d+(?:\.\d+)?"
numbers = re.findall(pattern, text)
print("Numbers found:", numbers)
 
 
 
 
Operators  - Description
 
.         Matches with any single character except newline ‘\n’.
 
?        match 0 or 1 occurrence of the pattern to its left
 
+        1 or more occurrences of the pattern to its left
 
*        0 or more occurrences of the pattern to its left
 
\w       Matches with a alphanumeric characters only
 
\W       matches non alphanumeric character.
 
\d       Matches with digits [0-9]
 
\D       matches with non-digits
 
 
[..]    Matches any single character in a square bracket
 
 
[^..]   matches any single character not in square bracket
 
 
 

 import re
from typing import List
 
# Return all words that match the supplied regex pattern.
def find_pattern_words(text: str, pattern: str) -> List[str]:
    if not text or not pattern:
        return []
    return re.findall(pattern, text)
 
# Replace every word that ends with a digit (…\d) with the symbol #
def replace_ending_digit_words(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'\b\w*\d\b', '#', text)
 
#  Count how many words contain at least three digits anywhere.
def count_words_with_3plus_digits(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(r'\b\w*(?:\d\w*){3,}\b', text))
 
# Return a list of substrings that look like email addresses.
def extract_emails(text: str) -> List[str]:
    if not text:
        return []
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
 
# Wrap dates of the form DD/MM/YYYY with ** (e.g., **12/05/2023**).
def highlight_dates(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'\b\d{2}/\d{2}/\d{4}\b', lambda m: f"**{m.group()}**", text)
 
#  Collapse consecutive whitespace characters into a single space.
def remove_extra_spaces(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()
 
 
# ---------------------------
# Sample Test Cases
# ---------------------------
if __name__ == "__main__":
    text = """User123 logged in at 12/05/2023.\nEmail: alice@example.com\nOrder #A00123"""
 
    # Test 1: Find words ≥ 5 characters
    pattern = r'\b\w{5,}\b'
    print("find_pattern_words:", find_pattern_words(text, pattern))
 
    # Test 2: Replace words ending with digit
    print("replace_ending_digit_words:", replace_ending_digit_words(text))
 
    # Test 3: Count words with ≥ 3 digits
    text2 = "ab12cd34 ef567 ghij12345 12345"
    print("count_words_with_3plus_digits:", count_words_with_3plus_digits(text2))
 
    # Test 4: Extract emails
    print("extract_emails:", extract_emails(text))
 
    # Test 5: Highlight dates
    print("highlight_dates:", highlight_dates(text))
 
    # Test 6: Remove extra spaces
    messy_text = "This   is   a    test\nwith   irregular   spaces."
    print("remove_extra_spaces:", remove_extra_spaces(messy_text))
 
'''
Design a class SensorStore that maintains a nested dictionary for sensor readings.
 Outer keys = sensor IDs (strings).
 Inner dictionary contains predefined fields: temperature, humidity, pressure, timestamp.
Functionalities to be created
#   Functionality   Description Edge‑Case handling
1️add_entry(sensor_id: str, data: dict) → None  Insert a new sensor reading. Raise DuplicateSensorError if the ID already exists.   Verify required fields, raise custom exception on duplicate.
2️  remove_entry(sensor_id: str) → None Delete an entry. Raise SensorNotFoundError if the ID does not exist.    Handled via try/except.
3️  first_n_entries(n: int) → dict  Return a new dictionary with the first n entries (in insertion order). If n > size, return all entries and emit a warning.  Validate n > 0; warn when n exceeds size.
4️  filter_by_condition(key: str, operator: Callable[[Any], bool]) → dict   Return inner dictionaries where key satisfies operator. Raise InvalidReadingKeyError if key missing; handle malformed operator.
5️  sort_by_reading(key: str, reverse: bool = False) → List[Tuple[str, dict]]   Return list of (sensor_id, data) sorted by the numeric value at key. Raise InvalidReadingKeyError if the key is absent or non‑numeric.  Check for numeric values, empty store, missing key.
All custom exceptions must inherit from Exception and provide meaningful messages. The class should return deep copies of internal structures to avoid external mutation.
 
'''
 
from typing import Any, Callable, Dict, List, Tuple
import copy
import warnings
 
class DuplicateSensorError(Exception):
    """Raised when a sensor ID already exists."""
    pass
 
class SensorNotFoundError(Exception):
    """Raised when a sensor ID is not found."""
    pass
 
class InvalidReadingKeyError(Exception):
    """Raised when an invalid reading key is used."""
    pass
 
class SensorStore:
    """
    Maintains a nested dictionary for sensor readings.
    Outer keys = sensor IDs (strings).
    Inner dictionary contains predefined fields: temperature, humidity, pressure, timestamp.
    """
 
    def __init__(self):
        self._sensor_data: Dict[str, Dict[str, Any]] = {}
        self._required_fields = ["temperature", "humidity", "pressure", "timestamp"]
 
    def add_entry(self, sensor_id: str, data: dict) -> None:
        """
        Insert a new sensor reading.
        Raise DuplicateSensorError if the ID already exists.
        Verify required fields, raise custom exception on duplicate.
        """
        if sensor_id in self._sensor_data:
            raise DuplicateSensorError(f"Sensor ID '{sensor_id}' already exists.")
 
        # Validate required fields
        for field in self._required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: '{field}'")
 
        self._sensor_data[sensor_id] = copy.deepcopy(data)  # Store a deep copy
 
    def remove_entry(self, sensor_id: str) -> None:
        """
        Delete an entry.
        Raise SensorNotFoundError if the ID does not exist.
        Handled via try/except.
        """
        try:
            del self._sensor_data[sensor_id]
        except KeyError:
            raise SensorNotFoundError(f"Sensor ID '{sensor_id}' not found.")
 
    def first_n_entries(self, n: int) -> dict:
        """
        Return a new dictionary with the first n entries (in insertion order).
        If n > size, return all entries and emit a warning.
        Validate n > 0; warn when n exceeds size.
        """
        if n <= 0:
            raise ValueError("n must be a positive integer.")
 
        size = len(self._sensor_data)
        if n > size:
            warnings.warn(f"n ({n}) is greater than the number of entries ({size}). Returning all entries.")
            n = size
 
        return copy.deepcopy(dict(list(self._sensor_data.items())[:n]))  # Deep copy and return
 
    def filter_by_condition(self, key: str, operator: Callable[[Any], bool]) -> dict:
        """
        Return inner dictionaries where key satisfies operator.
        Raise InvalidReadingKeyError if key missing; handle malformed operator.
        """
        filtered_data = {}
        for sensor_id, data in self._sensor_data.items():
            if key not in data:
                raise InvalidReadingKeyError(f"Key '{key}' not found in sensor data for ID '{sensor_id}'.")
            try:
                if operator(data[key]):
                    filtered_data[sensor_id] = copy.deepcopy(data)  # Deep copy
            except Exception as e:
                raise ValueError(f"Malformed operator: {e}")
 
        return filtered_data
 
    def sort_by_reading(self, key: str, reverse: bool = False) -> List[Tuple[str, dict]]:
        """
        Return list of (sensor_id, data) sorted by the numeric value at key.
        Raise InvalidReadingKeyError if the key is absent or non‑numeric.
        Check for numeric values, empty store, missing key.
        """
        if not self._sensor_data:
            return []
 
        try:
            sorted_entries = sorted(self._sensor_data.items(), key=lambda item: item[1][key], reverse=reverse)
        except KeyError:
            raise InvalidReadingKeyError(f"Key '{key}' not found in sensor data.")
        except TypeError:
            raise InvalidReadingKeyError(f"Key '{key}' contains non-numeric values.")
 
        return [(sensor_id, copy.deepcopy(data)) for sensor_id, data in sorted_entries] # Deep copy
 
# Example Usage:
if __name__ == '__main__':
    store = SensorStore()
 
    # Add entries
    store.add_entry("sensor1", {"temperature": 25.5, "humidity": 60, "pressure": 1012, "timestamp": 1678886400})
    store.add_entry("sensor2", {"temperature": 22.0, "humidity": 55, "pressure": 1015, "timestamp": 1678886460})
 
    # Remove entry
    store.remove_entry("sensor1")
 
    # First n entries
    print("First 1 entries:", store.first_n_entries(1))
 
    # Filter by condition
    def is_high_temp(temp: float) -> bool:
        return temp > 23
 
    print("Filtered by high temperature:", store.filter_by_condition("temperature", is_high_temp))
 
    # Sort by reading
    print("Sorted by temperature:", store.sort_by_reading("temperature"))
    print("Sorted by temperature (reverse):", store.sort_by_reading("temperature", reverse=True))
 
    # Edge Cases
    try:
        store.add_entry("sensor2", {"temperature": 23, "humidity": 50, "pressure": 1000}) # Duplicate
    except DuplicateSensorError as e:
        print(e)
 
    try:
        store.remove_entry("sensor3") # Non existent sensor
    except SensorNotFoundError as e:
        print(e)
 
    try:
        store.filter_by_condition("altitude", lambda x: True)
    except InvalidReadingKeyError as e:
        print(e)
 
Shriyansh Kesharwani (Unverified) left the chat.

 
Ashwin Mahajan (Unverified) left the chat.

 