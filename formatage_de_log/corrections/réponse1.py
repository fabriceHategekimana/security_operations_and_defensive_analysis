import sys
import re
import json
from collections import Counter, OrderedDict

if __name__ == '__main__':
	if len(sys.argv) > 1:
		print("Specify log file as argument!")
		exit(1)

	try:
		with open(sys.argv[1], "r") as fin:

			ip_paattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} -'
			log = fin.read()
			ipregex = re.findall(ip_paattern, log)
			iplist = list()
			for i in ipregex:
				iplist.append(i.split(" ")[0])
			
			ipcount1 = Counter(iplist)
			ipcount2 = OrderedDict(ipcount1.most_common())

			try:
				with open('results-1.json', 'w+') as fjson:
					json.dump(ipcount2, fjson, indent=2)

			except IOError:
				print ("Could not write result file!")

	except IOError:
		print ("Could not read log file!")
