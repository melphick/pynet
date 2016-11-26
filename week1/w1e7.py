#!/usr/bin/python
"""
A Python program that reads both the YAML file and the JSON file created in
exercise 6 and output to pretty print.
"""
from pprint import pprint
import yaml
import json

with open("example_yaml.yml") as f:
    yaml_list = yaml.load(f)

with open("example_json.json") as f:
    json_list = json.load(f)

print "\nHere is the pretty print of the list from YAML"
print "--------------------------------------------"
pprint(yaml_list)
print "--------------------------------------------\n"
print "Here is the pretty print of the list from JSON"
print "--------------------------------------------"
pprint(json_list)
print "--------------------------------------------"
