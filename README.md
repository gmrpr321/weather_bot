# Weather Bot

Weather Bot is a Python module that utilizes the OpenAI text Model and OpenWeather API to provide weather information. It can fetch current weather conditions, temperature, humidity, and other relevant data for a specified location.

## Files

### API_Parser.py

#### APIParser

This class is responsible for parsing data retrieved from APIs and returning the data in the appropriate format.

##### Methods

- `parse_bool(self, string_bool: str) -> bool`: Given a string value that contains either "true" or "false", this method returns its equivalent boolean value.

- `format_str_list(self, string_list: str) -> list`: This method formats a string that contains a list of values into a Python list.

- `add_newline(self, input_str: str, weight: int) -> str`: Used to add newline characters at the beginning and end of the given string for the specified weight value.

### openAI_calls.py

#### OpenAICalls

This class handles API calls with the OpenAI text model and is used for interacting with users and generating values for making further API calls.

##### Methods

- `__init__(self)`: Initializes the OpenAICalls class and sets up the OpenAI API key and model.

- `decide_prompt_validity(self, input: str) -> str`: This method decides if the input prompt is a valid prompt for a weather bot by making API calls to the OpenAI model. It returns a boolean value in string format.

- `generate_false_input_prompt(self, input_str: str) -> str`: Generates an output message for the user when they ask an invalid question. It provides a prompt informing the user that the operation cannot be done by the Weather Bot.

- `generate_user_response(self, input_str: str, metaData: str) -> str`: Generates the user's response using the input prompt and metadata from the OpenWeather API. It returns a response prompt as a string.

- `generate_greeting(self) -> str`: Provides a greeting message at the launch of the chatbot to instruct the user to type their question about weather conditions.

- `extract_city_data(self, input_str: str) -> str`: Extracts city name, state code, and country code from the user's prompt and returns them as a string in a specific format.

### weather_API_calls.py

#### WeatherAPICalls

This class is responsible for making API calls to the OpenWeather API and Geocoding API.

##### Methods

- `__init__(self)`: Initializes the WeatherAPICalls class and sets up the API key and base URL for the OpenWeather API.

- `make_weather_API_call(self, city_name: str) -> dict`: Fetches weather data for a specified city by making an API call to the OpenWeather API. It returns the weather data as a dictionary. If the API call fails, it returns an empty dictionary.

### operate.py

This script contains the main logic for running the Weather Bot chatbot.

- `begin_chatbot()`: Starts the Weather Bot chatbot. It initializes the necessary classes, displays a greeting message, and continuously prompts the user for input. It validates the user's prompt, extracts relevant city data, makes API calls to retrieve weather information, and generates appropriate responses.
