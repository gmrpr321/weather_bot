class APIParser:
    """
    Class to Parse the data from api and return the data
    in appropriate format
    """

    def parse_bool(self, string_bool: str) -> bool:
        """
        given is a stirng value that contains either "true" or "false"
        returns its equivalent boolean value

        args:
            string_bool : string value that contains either "true" / "false"

        output:
            equivalent boolean value
        """
        if "true" in string_bool:
            return True
        return False

    def format_str_list(self, string_list: str) -> list:
        """
        formats the string that contains a list of values into a list

        args:
            string_list : stirng that contains list values

        output:
            A list of values that is resembles the string_lsit
        """
        result = string_list.strip()
        result = result.removeprefix("[")
        result = result.removesuffix("]")
        result = result.replace('"', "")
        result = result.replace("'", "")
        result_list = result.split(",")
        return result_list

    def add_newline(self, input_str: str, weigth: int) -> str:
        """
        Used to add newLine character at the beginning and end of the given string for the given
        weight value

        agrs:
            input_str : given string to concatenate newline character
            weight : specifies the amount of newline characters to add at the beginning
                        and end of the string
        """
        return (weigth * "\n") + input_str + (weigth * "\n")
