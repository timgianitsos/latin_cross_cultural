import sys
import pickle
import os
from os.path import join
from collections import Counter
import csv

def main():
	try:
		data_filename = sys.argv[1]
	except:
		print('Please input the filename as the first command line argument', file=sys.stderr)
		return
	pfeatures = pickle.load(open(data_filename, 'rb'))
	name_to_pretty_name = {
		filename
		:
		' '.join(map(
			lambda s: s[0].upper() + s[1:],
			filename[filename.rindex(os.sep) + 1: filename.index('.tess')]
			.replace('.', ' ').replace('_', ' ').split()
		))
		for filename in pfeatures
	}
	# pretty_name_to_label = {row[28]: row[30] for row in csv.reader(open('stylometry_data_expected.csv', mode='r'))}

	for foldername, _, filenames in os.walk('old_labels'):
		for filename in filenames:
			if filename.endswith('.csv'):
				with open(join(foldername, filename), mode='r') as input_csv:
					reader_iter = iter(csv.reader(input_csv))
					val_to_name = {tok.split(':')[1]: tok.split(':')[0] for tok in next(reader_iter)}
					next(reader_iter)
					pretty_name_to_genre = {line[0]: val_to_name[line[1]] for line in reader_iter}

				foldername_list = foldername.split(os.sep)
				newfoldername = 'labels' if len(foldername_list) == 1 else join('labels', *foldername_list[1:])
				with open(join(newfoldername, f'{filename}'), mode='w') as output_csv:
					writer = csv.writer(output_csv)
					writer.writerow([f'{v}:{v}' for v in val_to_name.values()])
					writer.writerow(['Textname', 'Genre'])
					for name in sorted(name_to_pretty_name.keys()):
						if name_to_pretty_name[name] in pretty_name_to_genre:
							writer.writerow([name, pretty_name_to_genre[name_to_pretty_name[name]]])
					# for name, genre in name_to_genre.items():
					# 	writer.writerow([name, genre])

	# writer = csv.writer(open('labels/prosody.csv', 'w'))
	# writer.writerow(['Prose:Prose', 'Verse:Verse'])
	# writer.writerow(['Textname', 'Genre'])
	

	# print([item for item, count in Counter(name_to_pretty_name.values()).items() if count > 1])
	# assert len(name_to_pretty_name) == len(set(name_to_pretty_name.values())), f'{len(name_to_pretty_name)}, {len(set(name_to_pretty_name.values()))}'
	# expected_names = [row[28] for row in csv.reader(open('stylometry_data_expected.csv', mode='r'))][1:]

if __name__ == '__main__':
	main()
