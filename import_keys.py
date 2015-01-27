#!/usr/bin/env python2
#
# Script imports API keys from the Alliance Auth database and from the SeAT database and inserts missings ones into the
# SeAT database for synchronization. Allows easy management of API keys as people add them to the Alliance Auth system.
#
# Requires a file in JSON form containing the API auth for SeAT.

import sys, getopt
import json, pymysql, requests

def pull_allianceauth_data(conf):
    database = pymysql.connect(host='localhost', user=conf['mysql_user_auth'], passwd=conf['mysql_pw_auth'])
    db_connection = database.cursor(pymsql.cursors.DictCursor)
    query = "SELECT api_id,api_key FROM {0}.eveonline_eveapikeypair".format(conf['mysql_db_auth'])
    db_connection.execute(query)
    return db_connection.fetchall()

def pull_seat_data(conf):
    database = pymysql.connect(host='localhost', user=conf['mysql_user_seat'], passwd=conf['mysql_pw_seat'])
    db_connection = database.cursor(pymsql.cursors.DictCursor)
    query = "SELECT keyID,vCode FROM {0}.seat_keys".format(conf['mysql_db_seat'])
    db_connection.execute(query)
    return db_connection.fetchall()

def submit_keys(conf):
    pass

def read_conf_file(conf_file):
    valid_file = True
    with open(conf_file,'r') as f:
        conf = json.load(f)
    req_values = ['user_key1','user_key2', 'url', 'mysql_user_auth', 'mysql_pw_auth', 'mysql_db_auth', 'mysql_user_seat','mysql_pw_seat', 'mysql_db_seat'] 
    for value in req_values:
        if value not in conf:
            raise Exception('Invalid configuration file, need {0} value'.format(value))
    return conf

def main(argv):
    conf_file = None
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile=",])
    except getopt.GetoptError:
        print('import_keys.py -i <conf_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('import_keys.py -i <conf_file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            conf_file = arg
    print('Input file is "', conf_file)
    conf = read_conf_file(conf_file)
    auth_data = pull_auth_data(conf)
    seat_data = pull_seat_data(conf)


if __name__ == "__main__":
   main(sys.argv[1:])