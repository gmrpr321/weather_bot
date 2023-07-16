from API_parser import APIParser
from openAI_calls import OpenAICalls
from weather_API_calls import WeatherAPICalls


def begin_chatbot():
    """
    Calling this function will start the chatBot
    """
    parser = APIParser()
    openai_api = OpenAICalls()
    weather_api = WeatherAPICalls()
    # Display Greeting Message
    print(parser.add_newline(openai_api.generate_greeting(), 2))
    while True:
        # Get the input prompt from user
        input_str = input("Enter Response : ")
        # Validate the user prompt
        if parser.parse_bool(openai_api.decide_prompt_validity(input_str)):
            # extract the city data of interest
            city_data = parser.format_str_list(openai_api.extract_city_data(input_str))
            city_name = city_data[0]
            # Call opwnweather API to retrive city's weather condition
            city_weather_data = str(weather_api.make_weather_API_call(city_name))
            if len(city_weather_data) > 0:
                # Generate and print user response
                print(
                    parser.add_newline(
                        openai_api.generate_user_response(input_str, city_weather_data),
                        1,
                    )
                )
            else:
                print(
                    parser.add_newline(
                        openai_api.generate_false_input_prompt(input_str), 3
                    )
                )

        else:
            # Display wrong prompt message
            print(
                parser.add_newline(openai_api.generate_false_input_prompt(input_str), 3)
            )


if __name__ == "__main__":
    begin_chatbot()
