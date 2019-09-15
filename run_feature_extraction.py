'''
Latin features
'''
import os
import subprocess
import sys
import qcrit.extract_features

from latin_features import * #pylint: disable = wildcard-import, unused-wildcard-import

CORPUS_DIR = os.path.join('tesserae', 'texts', 'la')

def _download_corpus():
	'''
	Downloads latin corpus from tesserae

	Sparse checkout reference here:
	#https://stackoverflow.com/a/13738951/7102572
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

if __name__ == '__main__':
	_download_corpus()
	qcrit.extract_features.main(
		corpus_dir=CORPUS_DIR, file_extension_to_parse_function={'tess': qcrit.extract_features.parse_tess}
	)
