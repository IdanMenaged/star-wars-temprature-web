import sys
import os
sys.path.append(f'{os.getcwd()}')

from apis.starwars.main import orgonize

def test_orgonize():
    data = orgonize()
    assert 'Tatooine' in data['arid']
    for key in data.keys():
        assert ',' not in key
        assert data[key] != []