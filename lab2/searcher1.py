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
    "regexp": {
      "text": {
        # "value": r'(ustaw(a|y|ie|ę|ą|o|y|om|ami|ach))|(ustaw)',
        "value": "ustawa",
      }
    }
  }})

print(res.keys())
print(res['hits'].keys())
print(res['hits']['hits'])
print(res['hits']['total']['value'])

