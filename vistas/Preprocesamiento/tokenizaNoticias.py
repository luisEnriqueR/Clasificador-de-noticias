import re
import sys

def tokenizar(linea):
	contents = []
	num = []
	data = linea.split()
	for word in data:
		if re.search('^[0-9]+', word):
			try:
				if re.search('[0-9]+\.$', word):
					result = re.split(r'([\W])', word)
					result[:] = [item for item in result if item != '']
					contents.append(result)
				else:
					float(word)
					num.append(word)
					contents.append(num)
					num = []
			except Exception as e:
				result = re.split(r'([\W])', word)
				result[:] = [item for item in result if item != '']
				contents.append(result)
		else:
			result = re.split(r'([\W])', word)
			result[:] = [item for item in result if item != '']
			contents.append(result)

	
	
	final_str = ""
	for element in contents:
		for word in element:
			final_str += word
			final_str += " "

	return(final_str)

"""

"""