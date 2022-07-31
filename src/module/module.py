"""
This file implements module's main logic.
Data processing should happen here.
Edit this file to implement your module.
"""

import os
from logging import getLogger

log = getLogger("module")


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.
    Args:
        received_data (any): Data received by module and validated.
    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.
    """

    log.debug("Processing ...")

    try:
        # extract temperature data
        c_temp = received_data[os.getenv("TEMPERATURE_LABEL")]

        # convert units from Celsius to Fahrenheit
        f_temp = celsiusToFahrenheit(c_temp)

        # swap converted data
        received_data[os.getenv("TEMPERATURE_LABEL")] = f_temp

        return received_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"

def celsiusToFahrenheit(c_temp):
    """ Returns: converted temperature from Celsius to Fahrenheit """
    return (c_temp * (9 / 5)) + 32
