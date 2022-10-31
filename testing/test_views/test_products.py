"""
Test products
"""

from flask import url_for


def test_add_product(client):
    """
    Test get_item
    :param client:
    :return:
    """
    url = url_for('products_app.add')
    data = {
        "product-name": "Test product name"
    }
    response = client.post(url, data=data)
    assert response.status_code < 400, response.text
    assert 'location' in response.headers
