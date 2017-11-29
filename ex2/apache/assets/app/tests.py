#!/usr/bin/env python

import unittest
import requests

class TestCase(unittest.TestCase):

    def test_get_mainpage(self):
        page = requests.get("http://localhost/")
        assert page.status_code == 200
        assert 'It works!' in str(page.content)

    def test_asset(self):
        page = requests.get("http://localhost/asset.txt")
        assert page.status_code == 200
        assert 'Hi' in str(page.content)
        assert 'CDmon' in str(page.content)
        assert 'FreeBSD' not in str(page.content)

    def test_non_existing_html(self):
        page = requests.get("http://localhost/non_existing.txt")
        assert page.status_code == 404

    def test_production_headers(self):
        page = requests.get("http://localhost/non_existing.txt")
        assert 'text/html' in str(page.headers['content-type'])
        assert 'Apache/2.4' not in str(page.headers['server'])

if __name__ == '__main__':
    unittest.main()
