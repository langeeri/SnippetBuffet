#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Debugger HTTP XML server

A simple HTTP server for serving XML data. This script creates an HTTP server
that responds to GET requests with XML content. Intended just for quick XML client 
testing.

Classes:
    XMLRequestHandler: Handles incoming HTTP requests.
    HttpXmlServer: Manages the HTTP server.

Functions:
    run_server: Starts the XML server based on provided configuration.

Usage:
    Run the script to start the server. It listens on localhost:5000 by default.
    Access http://localhost:5000/get_xml_data to retrieve XML data.

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from typing import Dict

class XMLRequestHandler(BaseHTTPRequestHandler):
    """
    A request handler class for the HTTP XML server.

    Methods
    -------
    do_GET(self):
        Handles the GET request to the server.
    create_xml_data(self) -> str:
        Generates XML data as a string.

    """

    def do_GET(self):
        """Handle the GET request to the server."""
        if self.path == '/get_xml_data':
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            logging.debug("Header send")
            xml_data = self.create_xml_data()
            self.wfile.write(xml_data.encode())
            logging.debug(f"Data send {xml_data}")
        else:
            self.send_error(404, "Not Found")
            logging.debug("Error while trying to send data")

    def create_xml_data(self) -> str:
        """Generate XML data as a string."""
        xml_data = """<?xml version="1.0" encoding="UTF-8"?>
        <data>
            <value>200</value>
            <status>OK</status>
        </data>"""
        return xml_data

class HttpXmlServer:
    """
    A class to manage the HTTP XML server.

    Attributes
    ----------
    host : str
        Hostname of the server.
    port : int
        Port number of the server.
    http_server : HTTPServer or None
        Instance of the HTTPServer.

    Methods
    -------
    start_server(self):
        Starts the HTTP XML server.
    stop_server(self):
        Stops the HTTP XML server.

    """

    def __init__(self, host: str, port: int):
        """
        Initialize the HttpXmlServer with host and port.

        Parameters
        ----------
        host : str
            Hostname for the server.
        port : int
            Port number for the server.

        """
        self.host = host
        self.port = port
        self.http_server = None

    def start_server(self):
        """Starts the HTTP XML server."""
        try:
            self.http_server = HTTPServer((self.host, self.port), XMLRequestHandler)
            logging.info(f"Server listening on {self.host}:{self.port}")
            self.http_server.serve_forever()
        except Exception as e:
            logging.error(f"Error running XML server: {e}")

    def stop_server(self):
        """Stops the HTTP XML server."""
        if self.http_server:
            self.http_server.shutdown()
            self.http_server.server_close()
            logging.info("Server stopped.")

def run_server(xml_server_config: Dict[str, int]) -> None:
    """
    Starts the HTTP XML server based on provided configuration.

    Parameters
    ----------
    xml_server_config : dict
        Configuration for the XML server, including 'host' and 'port'.

    """
    xml_server = HttpXmlServer(**xml_server_config)
    
    try:
        xml_server.start_server()
    except KeyboardInterrupt:
        # Stop the server if the main process is interrupted
        xml_server.stop_server()
    finally:
        # Cleanup logging resources
        logging.shutdown()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
    xml_server_config = {'host': 'localhost', 'port': 5000}
    run_server(xml_server_config)

