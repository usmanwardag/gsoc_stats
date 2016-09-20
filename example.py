import gsoc

# Create a GSOC class object. This will load data from our main 
# CSV file.
obj = gsoc.GSOC()

# Count total number of projects
print obj.total_projects()

# Count total number of organizations
print obj.total_orgs()

# Count projects accepted by each organization
print obj.org_projects()

# Or, apply a threshold on last count
print obj.org_projects(threshold=5)

# Search for specific projects
print obj.search_projects('signal')
