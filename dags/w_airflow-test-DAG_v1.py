#!/usr/bin/env python
# coding: utf-8

import os
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'valentino',
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
    'w-airflow-test-sample_v1',
    default_args=default_args,
    description='Simple insert into Vertica - sample test DAG.',
    schedule_interval= '*/10 * * * *'
)

script = '/home/airflow/airflow-repository/SQL_Scripts/wTtest/test-dag-w-v1.py'
t1 = BashOperator(
    task_id='w-airflow-test-script-rights',
    bash_command='chmod +x ' + script,
    dag=dag
    )

t2 = BashOperator(
    task_id='w-airflow-test-run-script',
    bash_command='python3 ' + script,
    dag=dag
    )

t1 >> t2
