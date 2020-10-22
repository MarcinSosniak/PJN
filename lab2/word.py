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
        "query": "konstytucja",
      }
    }
  }})
# print(res)
# print(res.keys())
# print(res['hits'].keys())
# print(res['hits']['hits'].__class__)
# print(res['hits']['total']['value'].__class__)
# print(res['hits']['hits'][0]['_source']['name'])
print('total documents containg word \'ustawa\' in any form {}'.format(res['hits']['total']['value']))

