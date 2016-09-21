# GSOC 2016 Statistics
Query key GSOC statistics from last year! 

## Setup

Clone this library by running:

    git clone https://github.com/usmanwardag/gsoc_stats
    
Once installed, go to cloned directory open python terminal and run:

    import gsoc

## Examples

To start off, initialize `GSOC` class object:

    obj = gsoc.GSOC()
    
Count total number of projects and organizations from this year:

    obj.total_projects()
    >>> 1206
    obj.total_orgs()
    >>> 178
    
Count projects accepted by each organization:

    obj.org_projects()
    
This will give a sorted list of organization with a count of number of projects they accepted. You can also apply a filter:

    obj.org_projects(threshold=25)
    >>> [('Python Software Foundation', 53), ('Apache Software Foundation', 50), ('KDE', 37), ('FOSSASIA', 30), ('Debian    Project', 25)]
    
Search for specific projects accepted this year. 

    obj.search_projects('radio')
    >>> {'Radiology Reporting Enhancement': 'OpenMRS'}
    
# Contributions

The main motivation behind this repository is to help students from next year to better get sense of projects accepted by organizations this year. Feel free to contribute in any way!
