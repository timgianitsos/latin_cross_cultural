# pylint: disable = missing-docstring, invalid-name
'''
python <this script> name_of_output.csv
	Outputs content of csv to file
'''

import pickle
from collections import OrderedDict
import sys
import os
import csv
import getopt

from run_feature_extraction import feature_extraction

def generate_csv():
	if len(sys.argv) <= 1:
		raise getopt.GetoptError(
			'Please provide a command line argument for the output of the csv file\n'
			'Usage:\n\tpython <this script> <name of some file>.csv'
		)
	feature_file = 'feature_data.pickle'
	if not os.path.isfile(feature_file):
		print(f'File "{feature_file}" not found. Attempting to extract features.')
		feature_extraction(feature_file)
	with open(feature_file, mode='rb') as f:
		features = pickle.load(f)

	pretty_name_to_feature_name = OrderedDict([
		('Personal Pronouns', 'personal_pronoun'),
		('Demonstrative Pronouns', 'demonstrative_pronoun'),
		('Quidam', 'quidam'),
		('Reflexive Pronouns', 'reflexive_pronoun'),
		('Iste', 'reflexive_pronoun'),
		('Alius', 'alius'),
		('Ipse', 'ipse'),
		('Idem', 'idem'),
		('Priusquam', 'priu'),
		('Antequam', 'anteq'),
		('Quominus', 'quom'),
		('Dum', 'dum'),
		('Quin', 'quin'),
		('Ut', 'ut'),
		('Conditionals', 'conditional_clauses'),
		('Prepositions', 'prepositions'),
		('Interrogative Sentences', 'interrogative'),
		('Superlatives', 'superlatives'),
		('Atque + consonant', '?'),
		('Relative Clauses', 'relatives'),
		('Mean Length Relative Clauses', '?'),
		('Gerunds and Gerundives', 'end_gerund'),
		('Cum', 'cum_clause'),
		('Conjunctions', '?'),
		('Vocatives', '?'),
		('Mean Sentence Length', 'mean_sentence'),
		('Characters', 'characters'),
		('Words', 'words'),
		('Corpus Name', 'filename'),
		('Sentences', 'sentences'),
		('Type', '?'),
	])
	#If any of the names have commas, that will mess up the csv
	assert all(',' not in k and ',' not in v for k, v in pretty_name_to_feature_name.items())

	output = csv.writer(open(sys.argv[1], mode='w'))
	output.writerow(pretty_name_to_feature_name.keys())
	for filename, feature_to_value in features.items():
		feature_to_value['filename'] = filename
		#Rounding to 5 decimal places:
		#https://github.com/qcrit/DSH-2018-LatinProseVerse/blob/master/stylometry/imports/api/stylometry.js#L769
		output.writerow(
			f'{feature_to_value.get(feature_name):.5f}'
			if isinstance(feature_to_value.get(feature_name), float)
			else feature_to_value.get(feature_name)
			for feature_name in pretty_name_to_feature_name.values()
		)
	print(f'Successfully generated {sys.argv[1]}')

if __name__ == '__main__':
	generate_csv()
