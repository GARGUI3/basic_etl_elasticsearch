""" ElasticSearch Module """
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.exceptions import ElasticsearchException
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / 'environment_variables.env'
load_dotenv(dotenv_path=env_path)

__ES_CLIENT = {'client': None}

__ES_HOST = os.environ.get("esHost")
# Only use if you need authorization
__ES_USER = ''
__ES_PASS = ''

# Initialize instance ES
def __get_client():
    """ Returns a elastic search client """
    if not __ES_CLIENT['client']:
        __ES_CLIENT['client'] = Elasticsearch(
            __ES_HOST,
            # Only use if you need authorization
            http_auth=(
                __ES_USER,
                __ES_PASS
            )
        )
    return __ES_CLIENT['client']

def search(query):
    """ Returns the count of the dataset """
    query['allow_no_indices'] = True
    query['ignore_unavailable'] = True
    query['request_timeout'] = 30
    try:
        response = __ES_CLIENT['client'].search(**query)
        return response
    except ElasticsearchException as error:
        print('ElasticSearch error: %s', error)
        return error
    return None

def insert(documents):
    """Insert data on ElasticSearch"""
    bulk_data = []
    for doc in documents:
        bulk_data.append({
            '_index': doc['metadata']['_index'],
            '_type': doc['metadata']['_type'],
            '_source': doc['tweet']
        })
    try:
        response = bulk(__ES_CLIENT['client'], bulk_data)
        if response:
            return response
    except ElasticsearchException as error:
        return error
    return None


__get_client()
