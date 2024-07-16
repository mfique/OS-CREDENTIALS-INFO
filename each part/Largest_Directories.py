import os

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def find_largest_directories(path='.'):
    directories = [(d, get_size(os.path.join(path, d))) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    largest_directories = sorted(directories, key=lambda x: x[1], reverse=True)[:5]
    return largest_directories

largest_dirs = find_largest_directories()
print("Largest Directories by Size:")
for directory, size in largest_dirs:
    print(f"{directory}: {size // (2**20)} MB")