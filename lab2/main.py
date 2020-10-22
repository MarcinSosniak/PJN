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

DATA_PATH  = '../data'
# MAIN_INDEX_NAME= 'ustawy'

onlyfiles = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]



# r = requests.get('http://localhost:9200')



try:
    es.indices.create(index=MAIN_INDEX_NAME, body={
        'settings': {
            # custom analyzer for analyzing file paths
            'analysis': {
                "analyzer": {
                    "polish":{
                        "type" : "custom",
                        "tokenizer" : "standard",
                        "filter" : ["lowercase", "synonym","morfologik_stem"]
                    }
                },
                "filter": {
                      "synonym": {
                        "type": "synonym",
                         "tokenizer": "standard",
                        "synonyms": [ "kpk, kodeks postępowania karnego", "kpc, kodeks postępowania cywilnego", "kk, kodeks karny", "kc, kodeks cywilny"]
                      }
                }
            }
        },
        "mappings": {
            "dynamic": "strict",
            "properties": {
                "text": {
                    "type": "text",
                    "analyzer": "polish"
                },
                "name": {"type": "text"}
            }
        }
    })
except elasticsearch.exceptions.RequestError as e:
    if True: #not str(e).startswith('RequestError(400, \'resource_already_exists_exception\', \'index ['+MAIN_INDEX_NAME+'/'):
        raise e
    else:
        raise e


for i, file in enumerate(onlyfiles):
    if i % 50 == 0:
        print('processing {}/{}'.format(i, len(onlyfiles)))
    file_content = None
    year = file.split('_')[0]
    with open(DATA_PATH+'/' + file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    es.index(index=MAIN_INDEX_NAME,id=i,body={'name': file,'text':file_content})



#
#
# try:
#     es.indices.create(
#         index=MAIN_INDEX_NAME,
#         body={
#           'settings': {
#             # custom analyzer for analyzing file paths
#             'analysis': {
#                 "analyzer": {
#                     "polish":{
#                         "type" : "morfologik",
#                         "tokenizer" : "standard",
#                         "filter" : ["lowercase", "synonym","morfologik_stem"]
#                 }},
#                 "filter": {
#                   "synonym": {
#                     "type": "synonym",
#                      "tokenizer": "standard",
#                     # "lenient": True,
#                     "synonyms": [ "kpk => kodeks postępowania karnego" ,"kpc => kodeks postępowania cywilnego", "kk => kodeks karny", "kc => kodeks cywilny"]
#                   }
#                 },
#                 "mappings": {
#                     "dynamic": "strict",
#                     "properties": {
#                         "text": {
#                             "type": "text",
#                             "analyzer": "polish"
#                         },
#                         "name": {"type": "text"}
#                     }
#                 }
#
#             }
#           }
#         })
# except elasticsearch.exceptions.RequestError as e:
#     if True: #not str(e).startswith('RequestError(400, \'resource_already_exists_exception\', \'index ['+MAIN_INDEX_NAME+'/'):
#         raise e
#     else:
#         raise e