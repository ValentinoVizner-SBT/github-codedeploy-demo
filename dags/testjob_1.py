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
    'start_date': dt.datetime(2021, 2, 4, 14, 32),
    'email': ['neven.trgovec@axilis.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 10),
    'catchup': False
}

dag = DAG(
    'Test-Job-1',
    default_args=default_args,
    description='DAG 1.',
    schedule_interval= '*/1 * * * *'
)

command_1 = '/home/airflow/airflow-repository/TestJobs/SBT_MasterWorkspace/SBT_BI_Neven_Test_1/SBT_BI_Neven_Test_1_run.sh '

t0 = BashOperator(
    task_id='job1-rights',
    bash_command='chmod +x ' + command_1,
    dag=dag
    )

t1 = BashOperator(
    task_id='job1-run',
    bash_command=command_1,
    dag=dag
    )

t0 >> t1



