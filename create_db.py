#!/bin/env python3
"""
Create newsletter_automation database when MySQL is ready
Script to be used by the Dockerfile to:
    - Wait till MySQL is up
    - Create the newsletter_automation DB, if not present already
"""

import time
import pymysql

if __name__ == '__main__':

    # check if MySQL is up, poll for 150 secs to check if MySQL is up
    # sleep is needed to wait for the MySQL service to be up before the newsletter app starts
    # 3rd party apps like dockerize, wait-for-it.sh only allow checking if MySQL opens 3306 port, not if init completed
    for attempt in range(150):
        try:
            connection_obj = pymysql.connect(host='127.0.0.1',
                                        port=3306,
                                        user='root',
                                        password='root')

            print("MySQL is ready for connection in the {}th attempt".format(attempt))
            cursor_obj = connection_obj.cursor()
            cursor_obj.execute("CREATE DATABASE IF NOT EXISTS newsletter_automation;")
            connection_obj.close()
            break
        except Exception as err: #pylint: disable=broad-except
            time.sleep(1)
            print("MySQL not ready for connection yet, due to {}".format(err))
