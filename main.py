import anvil
import os

world_path = "world"
files = [f for f in os.listdir(f"{world_path}/region") if f.endswith('.mca')]

for i in range(len(files)):
    try:
        region = anvil.Region.from_file(f"{world_path}/region/{files[i]}")
        print(f"File loaded. Progress: {i + 1}/{len(files)}")
        all_chunks = []
        for x in range(32):
            for z in range(32):
                try:
                    chunk = region.get_chunk(x, z)
                    all_chunks.append(chunk)
                    print(f"Chunk loaded. Progress: {x * z}/1024 {i + 1}/{len(files)}")
                except Exception as e:
                    print(f"Chunk wasn't loaded. Error while loading a chunk: {e}. Progress: {x * z}/1024 {i + 1}/{len(files)}")
    except Exception as e:
        print(f"Error loading region: {e}. Progress: {i + 1}/{len(files)}")
