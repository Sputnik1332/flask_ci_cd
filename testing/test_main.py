"""
test main
"""

import random
from flask import url_for


def test_get_item(client):
    """
    Test get_item
    :param client:
    :return:
    """
    random_id = random.randint(1, 100)
    url = url_for('get_item', item_id=random_id)
    # url = f"/items/{random_id}/"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['item']['id'] == random_id
