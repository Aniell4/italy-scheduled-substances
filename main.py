import pandas as pd
import os


def main():
	tabelle_directory = "tabelle/"

	items = os.listdir(tabelle_directory)

	# Filter out only the files (not directories)
	tabelle_paths = [item for item in items if os.path.isfile(os.path.join(tabelle_directory, item))]

	search = input("[#] Search: ")

	for tabella_path in tabelle_paths:

		df = pd.read_excel(tabelle_directory + tabella_path)

		for key, value in df.items():
			for obj in df[key]:
				if search.lower() in (str(obj)).lower():
					print(f"\n{obj} | è nella ({key})")


if __name__ == '__main__':
	main()
