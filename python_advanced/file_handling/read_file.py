#!/usr/bin/env python3

def read_file(filename=""):

	with open("fichier.txt", "r", encoding="utf-8") as f:
		for line in f:
			print(line, end="")
