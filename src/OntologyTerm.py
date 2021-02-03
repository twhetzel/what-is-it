#!/usr/bin/python3
import json
import requests


class OntologyTerm:
    def __init__(self):
        self.OLS_URL = "http://www.ebi.ac.uk/ols/api/search"
            #"http://www.ebi.ac.uk/ols/api/search?q={search_value:s}&" \
            # "{params}".format(search_value=search_value, params=params)
        self.BIOPORTAL_URL = 'TEST'

    def search_OLS(self, token, params):
        # search_value = urllib.quote(data)
        search_value = token
        
        OLS_URL = self.OLS_URL+"?q={search_value:s}&" \
            "{params}".format(search_value=search_value, params=params)
        print(f'{OLS_URL}')

        try:
            response = requests.get(OLS_URL)
            if response.status_code == 200:
                results = json.loads(response.content)
                print(f'{results["response"]["numFound"]}')
                return results["response"]["numFound"]
        except requests.exceptions.RequestException as e:
            print(e)
