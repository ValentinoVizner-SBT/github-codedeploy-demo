#!/usr/bin/env python
# coding: utf-8

import os
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2021, 2, 19),
    'email': ['valentino.vizner@axilis.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 10),
    'catchup': False
}

dag = DAG(
    'w-airflow-test-sample_v3',
    default_args=default_args,
    description='Simple insert into Vertica - sample test DAG.',
    schedule_interval= '0 * * * *'
)

script = '/home/airflow/airflow-repository/SQL_Scripts/wTtest/test-dag-w-v1.py '

t1 = BashOperator(
    task_id='w-airflow-test-run-no-bash',
    bash_command='python3 ' + script,
    dag=dag
    )
