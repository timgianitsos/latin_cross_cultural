'''
Latin features
'''
import os
import subprocess
import sys
import re

import qcrit.extract_features
from qcrit.textual_feature import textual_feature, setup_tokenizers

CORPUS_DIR = os.path.join('tesserae', 'texts', 'la')

TERMINAL_PUNCTUATION = ('.', '?', '!')
setup_tokenizers(terminal_punctuation=TERMINAL_PUNCTUATION)

def _download_corpus():
	'''
	Downloads latin corpus from tesserae

	Sparse checkout reference here:
	#https://stackoverflow.com/a/28039894/7102572
	'''
	if not os.path.isdir('tesserae'):
		try:
			cmd_list = (
				'mkdir tesserae',
				'git -C tesserae init',
				'git -C tesserae remote add origin https://github.com/timgianitsos/tesserae.git',
				'git -C tesserae config core.sparseCheckout true',
				'echo "texts/la/*" >> tesserae/.git/info/sparse-checkout',
				'git -C tesserae pull --depth=1 origin master',
			)
			cmd_str = ' && '.join(cmd_list)
			proc = subprocess.run(cmd_str, shell=True)
			proc.check_returncode()
		except OSError as ex:
			print('An OS error occured', file=sys.stderr)
			raise ex
		except subprocess.CalledProcessError as ex:
			prgrm_names = {s.split(maxsplit=1)[0] for s in cmd_list}
			print(f'Your system could not run one of the following commands: {prgrm_names}', file=sys.stderr)
			raise ex

def _parse_tess_remove_nonalphanumeric(file_name):
	punct = '\\' + '\\'.join(TERMINAL_PUNCTUATION)
	return re.sub(
		fr'[^a-zA-Z0-9α-ωΑ-Ω\n\r{punct}]+', ' ',
		qcrit.extract_features.parse_tess(file_name)
	).lower()

def feature_extraction(output, use_universal_features):
	'''Perform a feature extraction'''
	_download_corpus()
	if use_universal_features == '-u':
		import qcrit.features.universal_features #seemingly unused, but allows the recognition of features
	else:
		import latin_features

	qcrit.extract_features.main(
		corpus_dir=CORPUS_DIR,
		file_extension_to_parse_function={'tess': _parse_tess_remove_nonalphanumeric},
		output_file=output
	)

if __name__ == '__main__':
	try:
		os.remove(sys.argv[1])
	except:
		pass
	feature_extraction(
		None if len(sys.argv) <= 1 else sys.argv[1],
		None if len(sys.argv) <= 2 else sys.argv[2],
	)
