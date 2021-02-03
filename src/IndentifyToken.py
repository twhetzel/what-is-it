#!/usr/bin/python3
from OntologyTerm import OntologyTerm


class IndentifyToken:
    def __init__(self):
        pass

    def indentify_resources(self, data):
        print(f'{data}')
        # Check if any tokens match an identifier pattern from Identifiers.org

    def identify_ontology_terms(self, data):
        ontology_manager = OntologyTerm()

        profile_results = {}
        profile_results['total_words'] = len(data)
        results = []

        params_exact = "local=true&exact=true"
        params_nonexact = "local=true&exact=false"

        for token in data:
            token_results = {}

            print(f'\nToken: {token}')
            token_results['token'] = token
            result = ontology_manager.search_OLS(token, params_exact)

            if result == 0:
                result = ontology_manager.search_OLS(token, params_nonexact)
                token_results['word_nonexact_matches'] = result
            else:
                token_results['word_exact_matches'] = result
            
            results.append(token_results)
        

        profile_results['results'] = results
        for k,v in profile_results.items():
            print(f'PR: {k} - {v}')