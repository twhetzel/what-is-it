#!/usr/bin/python3
import inquirer
from IdentifiersDataManager import IdentifiersDataManager
from InputDataManager import InputDataManager
from TextAnalysis import TextAnalysis
from IndentifyToken import IndentifyToken


def main():
    """
    Main module for application.
    """
    responses = user_prompts()

    if (responses['data_type'].lower() == 'text'):
        process_text_data(responses['data_directory_path'])
    else:
        # process_image_data()
        pass

    get_identifiers_registry_data()


def user_prompts():
    """
    Prompt user for type of input data, listing defined options.
    """
    questions = [
        inquirer.List('data_type',
                      message="What is the source of your input data?",
                      choices=['Text', 'Images'],
                      ),
        inquirer.Path('data_directory_path',
                      message="What is the full path to the data directory?",
                      path_type=inquirer.Path.DIRECTORY,
                      default='/Users/whetzel/git/what-is-it/data/'
                      ),
    ]
    answers = inquirer.prompt(questions)

    return answers


def get_identifiers_registry_data():
    """
    Get lastest version of Identifier.org registry data.
    """
    resource_manager = IdentifiersDataManager()
    data = resource_manager.get_registry_data()
    resource_manager.save_registry_data(data)


def process_text_data(data_directory_path):
    """
    Execute workflow steps for Text data.
    """
    data_manager = InputDataManager()
    text_analysis_manager = TextAnalysis()
    resource_manager = IndentifyToken()

    # Extract tokens from input file(s)
    all_input_files = data_manager.get_all_filenames(data_directory_path)
    for file in all_input_files:
        text_data = data_manager.get_data(data_directory_path+file)
        tokens = text_analysis_manager.generate_tokens(text_data)
        print(f'\nF: {file} -- {tokens}')

        # Identify/profile text based on matches to resource identifiers
        # resource_manager.indentify_resources(tokens)

        # Identify/profile text based on ontology terms
        resource_manager.identify_ontology_terms(tokens)


if __name__ == '__main__':
    main()
