import collections

def duplicate_list(mylist):
	return [item for item, count in collections.Counter(mylist).items() if count > 1]