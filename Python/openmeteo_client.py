#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module provides functionality to fetch and save weather data from the Open Meteo API.
It includes functions to request weather data based on specified geographical coordinates
and time frame, and to save this data in a JSON format.

Functions:
- get_weather_data: Fetches weather data from the Open Meteo API.
- save_as_json: Saves the fetched data into a JSON file.

Usage:
Call get_weather_data with latitude, longitude, start_date, and end_date parameters,
and then use save_as_json to save the data to a file.

"""

from typing import Optional, Dict, Union
import requests
import json


def get_weather_data(
    latitude: float, 
    longitude: float, 
    start_date: str, 
    end_date: str
) -> Optional[Dict[str, Union[str, float]]]:
    """
    Fetch weather data from the Open Meteo API.

    Parameters
    ----------
    latitude : float
        The latitude of the location.
    longitude : float
        The longitude of the location.
    start_date : str
        The start date for the weather forecast in the format "YYYY-MM-DD".
    end_date : str
        The end date for the weather forecast in the format "YYYY-MM-DD".

    Returns
    -------
    dict or None
        Weather data in JSON format, or None if an error occurs during the request.

    """

    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,shortwave_radiation",
        "wind_speed_unit": "ms",
        "timeformat": "unixtime",
        "start_date": start_date,
        "end_date": end_date,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def save_as_json(data: Dict[str, Union[str, float]], filename: str = "weather_data.json") -> None:
    """
    Save weather data to a JSON file.

    Parameters
    ----------
    data : dict
        Weather data in JSON format.
    filename : str, optional
        The name of the file to save the data. Defaults to "weather_data.json".

    """

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    # Example usage
    latitude = 50.088
    longitude = 14.4208
    start_date = "2023-12-26"
    end_date = "2023-12-26"

    weather_data = get_weather_data(latitude, longitude, start_date, end_date)

    if weather_data:
        save_as_json(weather_data)
