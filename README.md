# What-Is-It

## What-Is-It is a tool to help identify what resources and/or ontology terms are relevant to a section of scientific text. The input can either be image files or text files.

## Resource Dependencies
- [Identifiers.org](Identifiers.org)
- [BioPortal](https://bioportal.bioontology.org/)

## Software Dependencies
- Python3
- Google Cloud Platform - PubSub, Cloud Vision OCR, Storage Buckets
- NLTK (pip install --user -U nltk
and 
```
pip install certifi
/Applications/Python\ 3.6/Install\ Certificates.command
import nltk
nltk.download()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
# From: https://stackoverflow.com/questions/38725583/unable-to-download-nltk-data
```
- Inquirer


## Installation
- Git clone repo
- Install dependencies, `pip install -r requirements.txt`



