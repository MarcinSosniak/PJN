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

es.indices.delete(index=MAIN_INDEX_NAME)
# print(es.get(index=))