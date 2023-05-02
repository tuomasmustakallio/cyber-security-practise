#!/usr/bin/env python3
import sys
import json


def get_vulnerabilities(name, db):
	vulnerabilities = []
	vulnerabilitiesJson = json.load(db)
	selected = vulnerabilitiesJson[name]
	for report in selected:
		vulnerabilities.append((report["id"], report["v"], report["cve"]))
	return vulnerabilities


def main(argv):
	name = sys.argv[1]
	db = open(sys.argv[2])
	vulnerabilities = get_vulnerabilities(name, db)
	for v in vulnerabilities:
		print('%s; %s; %s' % (v[0], v[1], v[2]))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s name db' % sys.argv[0])
	else:
		main(sys.argv)
