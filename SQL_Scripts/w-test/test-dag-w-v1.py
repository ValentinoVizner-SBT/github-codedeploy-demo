#  !/usr/bin/env python
# coding: utf-8

import sys
import os

path = r'/home/airflow/airflow-repository/SQL_Scripts' + '/modules'
sys.path.insert(0, path)

import sql_vertica

from importlib import reload
reload(sql_vertica)

sql_vertica.run_script('w_test', 'w_sbx_de_insert_data.sql')