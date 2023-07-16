import openai


class OpenAICalls:
    """
    Class to make API calls with OpenAI text model,
    used for interacting with user and generating values for making further API calls
    """

    def __init__(self):
        openai.api_key = "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"
        self.ai_model = "gpt-3.5-turbo"

    def decide_prompt_validity(self, input: str) -> str:
        """Used to decide if the input prompt is a valid prompt for a weather bot

        args:
            input : input prompt from the user
        output:
            a boolean value in string format
        """
        Response = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "system",
                    "content": """you are a weather bot, decide if the user prompts belong to a 
                    weather bot, and it has a city name for further processing, even with typos, 
                    its fine as long as it contains the city name return "true" if that's the case or 
                    "false"  Output shout only contain either "true" or "false" and nothing else.
                    If just the city is present, return false
                    ignore grammer, if you think this is a question that can be answered by a 
                    weather bot,return true
                    example input : "I like cats"
                    example output : "false"
                    example input : "current weather of mumbai"
                    example output : "true"
                    example input : "tell me the weather conditions of mumbai"
                    example output : "true"

                            """,
                },
                {"role": "user", "content": "london is a beautiful city"},
                {"role": "assistant", "content": "false"},
                {"role": "user", "content": f"{input}"},
            ],
            temperature=0.6,
            max_tokens=200,
            model=self.ai_model,
        )
        data = Response["choices"][0]["message"]["content"]
        return data

    def generate_false_input_prompt(self, input_str: str) -> str:
        """
        Used to generate output for user if the user asks an invalid question

        args:
            input_str : prompt from the user

        output:
            prompt as a string value
        """
        Response = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "system",
                    "content": """you are a weather bot and the user has 
                                    given a false prompt that is irrelevant to 
                                    this application.provide a meesage to the user that this 
                                    operation cannot be done by this application. 
                                    Be funny and lively with only using  characters from 
                                    english alphabet and special characters .
                                    also consider the user prompt that is present in the real question and not the
                                    given question ("I love chocolate")
                                    keep it short and simple.If just the city name is present without 
                                    relevant contect, treat it as a invalid and/or incomplete request.
                                    only separete words with one space character
                                  DO NOT INCLUE EMOJI IN YOUR OUTPUT
                                  DO NOT USE LINE BREAKING CHARACTERS, OUPUT MUST BE A SINGLE LINE
                                """,
                },
                {"role": "user", "content": "I love chocolate"},
                {
                    "role": "assistant",
                    "content": """Oops! Looks like you're in the wrong place to express your love for chocolate. This weather bot is dedicated to 
                                  forecasting the skies, not indulging in sweet treats.So, let's focus on weather-related queries. 
                                  Ask away, and I'll be happy to assist you!""",
                },
                {"role": "user", "content": f"{input_str}"},
            ],
            temperature=0.6,
            max_tokens=400,
            model=self.ai_model,
        )
        data = Response["choices"][0]["message"]["content"]
        return data

    def generate_user_response(self, input_str: str, metaData: str) -> str:
        """
        Generates user output data using input prompt and metaData from OpenWeater API

        args:
            input_str : prompt from user
            metaData : string that contains a dictionary constructed from Openweater API response
        output:
            returns the response prompt as a string
        """
        Response = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "system",
                    "content": """given is an input for a 
                    weather application for a location and the 
                    corresponding metadata from the Openweather API,
                    You are a weather chatbot that is supposed to use this 
                    information to provide appropriate answers.
                    Dont use emogis in the output.only behave like a chatbot
                    that provides relevant info.
                    please provide the sunrise and sunset time in 12 hour format so include AM or PM.
                    please have a funny personality that makes you
                    lively and interactive.
                    """,
                },
                {
                    "role": "user",
                    "content": "tell me the hourly weather for cochin"
                    + "output from API"
                    + """
                "hourly":[
                    {
                        "dt":1684926000,
                        "temp":292.01,
                        "feels_like":292.33,
                        "pressure":1014,
                        "humidity":91,
                        "dew_point":290.51,
                        "uvi":0,
                        "clouds":54,
                        "visibility":10000,
                        "wind_speed":2.58,
                        "wind_deg":86,
                        "wind_gust":5.88,
                        "weather":[
                            {
                            "id":803,
                            "main":"Clouds",
                            "description":"broken clouds",
                            "icon":"04n"
                            }
                        ],
                        "pop":0.15
                    },
                    ...
                ]
                """,
                },
                {
                    "role": "assistant",
                    "content": """Sure, I'd be happy to help! Let me check the hourly weather for Cochin.
                    According to the Openweather API, the current weather in Cochin is as follows:
                    - Temperature: 40.34 celsius
                    - Feels like: 37.34 celsius
                    - Pressure: 1014 hPa (hectopascal)
                    - Humidity: 91%
                    - Dew point: 36.63 celsius
                    - Clouds: 54% (broken clouds)
                    - Visibility: 10000 meters
                    - Wind Speed: 2.58 meters per second
                    - Wind Degree: 86 degrees
                    - Wind Gust: 5.88 meters per second
                    - Probability of Precipitation (POP): 15%
                    - Sunrise time: 6:11 AM
                    - Sunset time: 6:13 PM
                    Please let me know if there's anything specific you'd like to know about 
                    weather conditions of a particular place!""",
                },
                {
                    "role": "user",
                    "content": f"{input_str+'output from API : '+metaData}",
                },
            ],
            temperature=0.6,
            max_tokens=500,
            model=self.ai_model,
        )
        data = Response["choices"][0]["message"]["content"]
        return data

    def generate_greeting(self) -> str:
        """
        Provides greeting message at the launch of the chatbot
        output:
            A string that contains a greeting message
        """
        Response = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "system",
                    "content": """You are a weather bot, give a greeting message
                      to tell user to type their question about the weather conditions.
                      Be funny and interactive, must use less than 20 words.
                      DO NOT INCLUE EMOJI IN YOUR OUTPUT
                            """,
                },
                {
                    "role": "user",
                    "content": """You are a weather bot, give a greeting message
                      to tell user to type their question about the weather conditions.
                      Be funny and interactive, must use less than 20 words.
                      DO NOT INCLUE EMOJI IN YOUR OUTPUT""",
                },
                {
                    "role": "assistant",
                    "content": """Hello there! The weather fairy is ready to answer 
                 all your weather curiosities. Ask away!""",
                },
                {
                    "role": "user",
                    "content": """You are a weather bot, give a greeting message
                      to tell user to type their question about the weather conditions.
                      Be funny and interactive, must use less than 20 words.
                      DO NOT INCLUE EMOJI IN YOUR OUTPUT""",
                },
            ],
            temperature=0.6,
            max_tokens=500,
            model=self.ai_model,
        )
        data = Response["choices"][0]["message"]["content"]
        return data

    def extract_city_data(self, input_str: str) -> str:
        """
        Takes in user prompt as input and provides city name,state code
        and country code as output

        args:
            input_str : prompt from user
        output:
            A string that contains a list of strings that resembles this format
            [city,state_code,country_code]
        """
        Response = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "system",
                    "content": """extract the city name and give me city
                                    name, state code and country code from this data. only give
                                    me those three things and nothing else. dont leave anything blank.
                                    Please use ISO 3166 country codes.If multiple state
                                    or country codes can be given in the answer,
                                    please select the most appropriate one.
                                    Remember to exactly give 3 items in the list.
                                    only give me the data and nothing else
                                    """,
                },
                {
                    "role": "user",
                    "content": "what's today's hourly and minutely weather for Mumbai",
                },
                {
                    "role": "assistant",
                    "content": """["London","JR","+44"]""",
                },
                {"role": "user", "content": f"{input_str}"},
            ],
            temperature=0.6,
            max_tokens=500,
            model=self.ai_model,
        )
        data = Response["choices"][0]["message"]["content"]
        return data
