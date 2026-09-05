import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app


def test_add_and_get():
    client = app.test_client()
    resp = client.post('/add', json={'username': 'alice', 'password': 's3cr3t'})
    assert resp.status_code == 201
    resp = client.get('/get/alice')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['password'] == 's3cr3t'


def test_get_nonexistent():
    client = app.test_client()
    resp = client.get('/get/doesnotexist')
    assert resp.status_code == 404
    data = resp.get_json()
    assert 'error' in data
