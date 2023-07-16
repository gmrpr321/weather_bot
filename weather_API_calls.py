import requests


class WeatherAPICalls:
    """
    class for making Openweather and Geocoding API calls
    """

    def __init__(self):
        self.api_key = "294db704158a02e99fcbe4959848bf52"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def make_weather_API_call(self, city_name: str) -> dict:
        """
        used to return weather data of a city
        args:
            city_name : Stirng value consisting of the city's name

            output:
                weather data of the given city as a dictionary,returns empty dictionary if API call fails
        """
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city_name
        response = requests.get(complete_url)
        response_data = response.json()
        if int(response_data["cod"]) // 100 != 4:
            return response_data

        else:
            return {}
