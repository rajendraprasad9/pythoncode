# dupFinder.py
import os
import sys
import hashlib
 
def findDup(parentFolder):
	dups = {}
	files = [f for f in os.listdir(parentFolder) if os.path.isfile(f)]
	for filename in files:
        # Get the path to the file
		path = os.path.join(parentFolder, filename)
        # Calculate hash
		file_hash = hashfile(path)
        # Add or append the file path
		if file_hash in dups:
			dups[file_hash].append(path)
		else:
			dups[file_hash] = [path]
	return dups
 
# def hashfile(path, blocksize = 65536):
def hashfile(path, blocksize = 10):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
 
    else:
        print('No duplicate files found.')
 
 
if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folder = sys.argv[1]
        if os.path.exists(folder):
            # Find the duplicated files and append them to the dups
            dups = findDup(folder)
        else:
            print('%s is not a valid path, please verify' % folder)
            sys.exit()
        printResults(dups)
    else:
        print('Usage: python dupFinder.py folder')