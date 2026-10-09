
from os import scandir

import mne
from mne import Annotations
from mne.io import read_raw_edf, Raw

def get_filenames(parent_folder_path: str) -> list[list[str]] | None:
	print('Getting filenames')
	subfolders = [ f.path for f in scandir(parent_folder_path) if f.is_dir() ]

	n_files = 0
	out: list[list[str]] = []
	for dir in subfolders:
		edf_files = [f.path for f in scandir(dir) if f.is_file() and f.path.endswith('.edf')]
		if len(edf_files) == 0:
			continue

		n_files += len(edf_files)
		out.append(edf_files)

	if len(out) == 0:
		return None
	print('Got ' + str(n_files) + ' .edf files')
	return out

''' -> list[list[Raw]]'''
def read_edf_files(filenames: list[list[str]]):
	print('Reading files')
	out: list[Raw] = []
	for d in filenames:
		for f in d:
			out.append(read_raw_edf(f)) # type: ignore
	return out

