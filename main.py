import pandas as pd

df = pd.read_excel('C_17_pagineAree_3729_0_file.xlsx')

search = input("[#] Search: ")

for key, value in df.items():
	for obj in df[key]:
		if search.lower() in (str(obj)).lower():
			print(f"\n{obj} | è nella ({key})")


df = pd.read_excel('C_17_pagineAree_3729_3_file.xlsx')

for key, value in df.items():
	for obj in df[key]:
		if search.lower() in (str(obj)).lower():
			print(f"\n{obj} | è nella ({key})")
