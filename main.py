
from sys import argv

import matplotlib.pyplot as plt

from parsing import *

def main():
	if len(argv) != 2:
		print(argv)
		print('Usage: py ./main.py [path to folder containing a folder for each participant with EEG .edf]')
		return 0

	edf_filenames = get_filenames(argv[1])
	if edf_filenames == None:
		print(argv[0] + ' is not a valid folder.')
		return 0

	raw_edfs = read_edf_files(edf_filenames)

	for an in raw_edfs[0].annotations:
		print(an['description'])

	#print(raw_edfs[0][0])
	#print(len(raw_edfs[0][11].annotations))
	raw_edfs[0].plot()
	#raw_edfs[0][0].ann()
	plt.show()


if __name__ == '__main__':
	main()
