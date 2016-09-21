import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from textwrap import wrap
import re
from collections import Counter

class GSOC(object):
    def __init__(self):
        """
        Load GSOC 2016 data from a CSV file.
        """

        self.data = pd.read_csv('resources/data.csv')
        self.cols = self.data.keys()
        self.orgs = self.data[self.cols[2]].unique()
        self.titles = self.data[self.cols[0]].tolist()

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

    def org_projects(self, org=None, threshold=None, order='desc'):
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
            # For consistency later
            org = [org]

        projects = dict()

        for o in org:
            projects[o] = len([i for i in self.data[self.cols[2]] if i==o])

        if threshold is not None:
            for p in projects.keys():
                if projects[p] < threshold:
                    projects.pop(p, 'None')

        if order == 'asc':
            projects = sorted(projects.items(), key=lambda x: x[1])
        else:
            projects = sorted(projects.items(), key=lambda x: -x[1])

        return projects


    def search_projects(self, name):
        """
        Search all projects containing input string.
        """

        matches = dict()

        for t in self.titles:
            if name.lower() in t.lower():
                # Some pandas stuff here, maybe it can be made more concise.
                match = self.data[self.data[self.cols[0]] == t]
                index = match[self.cols[2]].index.tolist()
                matches[t] = match.at[int(index[0]), self.cols[2]]

        return matches

    def combine_titles(self):
        """
        Combine all titles into a single string
        """

        return ' '.join(self.titles)

    def plot_orgs(self, threshold):
        """
        Plot a bar chart of organizations, arranged according to 
        number of projects they accepted.
        """

        projects = self.org_projects(threshold=threshold, order='asc')
        orgs = ['\n'.join(wrap(p[0], 18)) for p in projects]
        y_pos = np.arange(len(orgs))
        counts = [p[1] for p in projects]
        plt.barh(y_pos, counts, align='center', alpha=0.5, color='green')
        plt.yticks(y_pos, orgs, size=10, family='monospace')
        plt.grid(True)
        plt.xlabel('Number of Projects Accepted', size=14, family='monospace')
        plt.show()

    def extract_keywords(self):
        """
        Extract the most frequent words from project titles, after removing stop
        words.
        """

        STOPWORDS = [x.strip() for x in open('resources/stopwords.txt').read().split('\n')]
        text = self.combine_titles()
        words = re.findall('\w+', text.lower())
        counts = Counter(words).most_common(500)

        final = []

        for c in counts:
            if c[0] not in STOPWORDS:
                final.append(c)

        return final