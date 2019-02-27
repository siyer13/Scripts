import requests
print("Importing")

res = requests.get('http://localhost:9200')
print(res.content)


from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(es)

es.index(index='test-index', doc_type='test', id=1, body={'test': 'test'})
print('Searching')
res = es.search(index="enquero", doc_type="employees", body={"query": {"match": {"name": "Sridhar Iyer"}}})
print(res)
