import regex
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from elasticsearch import Elasticsearch
import elasticsearch
from constants import MAIN_INDEX_NAME

es = Elasticsearch([
        'http://elastic:elastic@localhost:9200/'],verify_certs=True)

res= es.search(index=MAIN_INDEX_NAME,body={
    "query": {
        "match": {
            "text": {
                "query": "konstytucja"
            }
        }
    },
    "size": 10,
    "_source": [ "name" ],
    "highlight": {
        "number_of_fragments": 3,
        "fragment_size": 125,
        "fields": {
            "text": {}
        }
    }
    })
# print(res.keys())
# print(res['hits'].keys())
print(res['hits']['hits'][0])
# print(res['hits']['total']['value'].__class__)
# print(res['hits']['hits'][0]['_source']['name'])
print('The number of legislative acts containing the words \'wchodzi w życie\' allowing for up to 2 additional words {}'.format(res['hits']['total']['value']))


for document in res['hits']['hits'] :
    print('filname: ' + document['_source']['name'] + 'score: ' + str(document['_score']))
    for highlight in document['highlight']['text']:
        print('\t'+highlight)
        print('')

