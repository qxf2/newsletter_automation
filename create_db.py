#!/bin/env python3
"""
Create newsletter_automation database when MySQL is ready
Script to be used by the Dockerfile to:
    - Wait till MySQL is up
    - Create the newsletter_automation DB, if not present already
"""

import time
import pymysql

def create_newsletter_db():
    "Create newsletter_automation DB"

    connection_obj = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='root')

    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("CREATE DATABASE IF NOT EXISTS newsletter_automation;")

    # insert article catagories
    cursor_obj.execute("INSERT INTO article_category (category_name) VALUES ('comic'),('pastweek'),('currentweek'),('automation corner');")

    connection_obj.close()

if __name__ == '__main__':

    # check if MySQL is up, poll for 120 secs to check if MySQL is up
    # sleep is needed to wait for the MySQL service to be up before the newsletter app starts
    # 3rd part apps like dockerize, wait-for-it.sh etc did not help
    for _ in range(120):
        try:
            create_newsletter_db()
            print("MySQL is ready for connection")
            break

        except pymysql.err.OperationalError:
            time.sleep(1)
            print("MySQL not ready for connection yet")

        except Exception as err: #pylint: disable=broad-except
            print("Unable to connect to MySQL, Error: %s" % err)
            raise
