import os

# create the 'data' folder if it does not exist yet
if not os.path.exists("data"):
    print("🔎 'data' folder does not exist yet. Creating...")
    os.mkdir('data')
    print("✅ Created 'data' folder")
else:
    print("Folder 'data' already exists")


# create the 'brands' folder, which is a sub folder of data
if not os.path.exists("data/brands"):
    print("🔎 'data/brands' folder does not exist yet. Creating...")
    os.makedirs("data/brands")
    print("✅ Created 'data/brands' folder")