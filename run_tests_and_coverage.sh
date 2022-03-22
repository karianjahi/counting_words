#!/bin/bash
pytest
pylint count_words
pylint test_count_words.py
pytest --cov
coverage html
