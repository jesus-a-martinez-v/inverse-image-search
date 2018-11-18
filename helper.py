

from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import requests
import random
import os
import base64
from sklearn.decomposition import TruncatedSVD
from keras.models import Model
from hashlib import md5
import pickle
from urllib.parse import unquote
from PIL import Image
from io import BytesIO
from IPython.display import HTML, Image as IPImage, display
import numpy as np
from tqdm import tqdm
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.preprocessing import image

query = '''SELECT ?pic
WHERE
{
    ?item wdt:P31 ?class . 
    ?class wdt:P18 ?pic
}'''

url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'

data = requests.get(url, params={'query': query, 'format': 'json'}).json()

pages_urls = [result['pic']['value'] for result in data['results']['bindings']]

print(f'Number of fetched pages urls: {len(pages_urls)}')
print(random.sample(pages_urls, 10))