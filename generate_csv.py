# pylint: disable = missing-docstring, invalid-name
'''
python <this script> name_of_output.csv
	Outputs content of csv to file
'''

import pickle
from collections import OrderedDict
import os
import csv

from run_feature_extraction import feature_extraction

def generate_csv():
	output_csv = 'stylometry_data_result.csv'
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
		('Iste', 'iste'),
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
		('Atque + consonant', 'startf'),
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

	# Remap feature names to remove dots and underscores and to capitalize first letter of every word
	features = {
		' '.join(map(
			lambda s: s[0].upper() + s[1:],
			filename[filename.rindex(os.sep) + 1: filename.index('.tess')]
			.replace('.', ' ').replace('_', ' ').split()
		))
		:
		feature_to_value
		for filename, feature_to_value in features.items()
	}
	expected_names = [row[28] for row in csv.reader(open('stylometry_data_expected.csv', mode='r'))][1:]

	output = csv.writer(open(output_csv, mode='w'))
	output.writerow(pretty_name_to_feature_name.keys())
	for filename in expected_names:
		csv_row = features.get(filename, {})
		csv_row['filename'] = filename

		#Rounding to 5 decimal places:
		#https://github.com/qcrit/DSH-2018-LatinProseVerse/blob/master/stylometry/imports/api/stylometry.js#L769
		output.writerow(
			f'{csv_row.get(feature_name):.5f}'
			if isinstance(csv_row.get(feature_name), float)
			else csv_row.get(feature_name)
			for feature_name in pretty_name_to_feature_name.values()
		)
	print(f'Successfully generated {output_csv}')

if __name__ == '__main__':
	generate_csv()
