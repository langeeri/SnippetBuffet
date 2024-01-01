#!/usr/bin/env python3

"""
This module provides functionality to test an XML server by sending an HTTP GET request 
and displaying the response. It is designed to work with an XML server that responds 
to GET requests with XML data.

Attributes
----------
xml_server_host : str
    Host address of the XML server.
xml_server_port : int
    Port number of the XML server.
xml_server_path : str
    Path for the GET request to the XML server.

Functions
---------
test_xml_server(host: str, port: int, path: str)
    Sends a GET request to the specified XML server and prints the response.

"""

import http.client

def test_xml_server(host: str, port: int, path: str):
    """
    Sends a GET request to the specified XML server and prints the response.

    Parameters
    ----------
    host : str
        The hostname or IP address of the XML server.
    port : int
        The port number on which the XML server is listening.
    path : str
        The path to request from the XML server.

    Returns
    -------
    None

    """
    connection = http.client.HTTPConnection(host, port)
    connection.request("GET", path)
    response = connection.getresponse()

    print(f"Response status: {response.status}")
    print(f"Response headers: {response.getheaders()}")

    if response.status == 200:
        xml_data = response.read().decode('utf-8')
        print("XML Data:")
        print(xml_data)

    connection.close()

if __name__ == "__main__":
    # Example usage
    xml_server_host = "127.0.0.1"
    xml_server_port = 5000
    xml_server_path = "/get_xml_data"

    test_xml_server(xml_server_host, xml_server_port, xml_server_path)


