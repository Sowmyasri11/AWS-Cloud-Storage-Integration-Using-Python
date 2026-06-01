import hashlib

def get_hash(filename):
    sha = hashlib.sha256()
    
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)
            
            if not chunk :
                break
            sha.update(chunk)
    
    return sha.hexdigest()

original = get_hash("data/sample_data.csv")
downloaded = get_hash("downloads/sample_data.csv")

print("Original:",original)
print("Downloaded:",downloaded)

if original == downloaded:
    print("File integrity verified")
else:
    print("Files are different")