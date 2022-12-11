from pymongo.collection import Collection
from pymongo import MongoClient
import random
import pytest
from unittest.mock import Mock


def get_client():
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    return client['firstbase']['Products']

def choose_one(c):
    if not isinstance(c, Collection):
        raise TypeError(f"expected collection, got {type(c)}")
    
    items = [*c.find({}, {"name": 1, "_id": 0})]
    res = random.choice(items)
    return res['name']


def test_choose_type():
    with pytest.raises(TypeError):
        choose_one('a')

def test_first_entry():
    c = Mock(spec=Collection)
    c.find.return_value = [{'name': 'Ace Ski Boot'}]
    assert choose_one(c) == 'Ace Ski Boot'
        
        
if __name__ == "__main__":
    print(choose_one(get_client()))