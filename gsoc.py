
import numpy as np
import pandas as pd

class GSOC(object):
	def __init__(self):
		"""
		Load GSOC 2016 data from a CSV file.

		Attributes
		----------
		data: 
		"""

		self.data = pd.read_csv('data.csv')
		self.cols = self.data.keys()
		self.orgs = self.data[self.cols[2]].unique()
		self.titles = self.data[self.cols[0]]

	def total_projects(self):
		"""
		Count total projects that got accepted in GSOC 2016.
		"""
		return len(self.titles)

	def total_orgs(self):
		"""
		Count total organizations that participated in GSOC 2016.
		"""

		return len(self.orgs)

	def org_projects(self, org=None, threshold=None):
		"""
		List projects posted by each organization.

		Parameters
		----------
		org: str
			Organization name

		threshold: int
			Threshold for number of projects by an organization
		"""

		if (org not in self.orgs) and (org is not None):
			raise ValueError('No such organization by this name.')

		elif org is None:
			org = self.orgs

		else:
			org = [org]

		projects = dict()

		for o in org:
			projects[o] = len([i for i in self.data[self.cols[2]] if i==o])

		if threshold is not None:
			for p in projects.keys():
				if projects[p] < threshold:
					projects.pop(p, 'None')

		return sorted(projects.items(), key=lambda x: -x[1])

	def search_projects(self, name):
		"""
		Search all projects containing input string.
		"""

		matches = dict()

		for t in self.titles:
			if name.lower() in t.lower():
				match = self.data[self.data[self.cols[0]] == t]
				index = match[self.cols[2]].index.tolist()
				matches[t] = match.at[int(index[0]), self.cols[2]]

		return matches

gsoc = GSOC()
print gsoc.total_projects()
print gsoc.total_orgs()
print gsoc.org_projects(threshold=20)
print gsoc.search_projects('signal')
