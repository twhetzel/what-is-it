#!/usr/bin/python3
import requests
import json
import os
import sys


class IdentifiersDataManager:
    def __init__(self):
        self.data_file_location = 'src/resources/identifier_data/'
        self.data_file_name = 'identifier_registry.json'
        self.registry_url = 'https://registry.api.identifiers.org/resolutionApi/getResolverDataset'

    def get_registry_data(self):
        """
        Get Registry data from Idenifiers.org
        """
        try:
            response = requests.get(self.registry_url)
            response.raise_for_status()
        except HTTPError as http_err:
            raise SystemExit(http_err)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return response

    def save_registry_data(self, data):
        with open(self.data_file_location+self.data_file_name, 'w') as f:
            json.dump(data.json(), f)
