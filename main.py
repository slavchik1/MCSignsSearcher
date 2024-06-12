import anvil
import os

world_path = "world"
files = [f for f in os.listdir(f"{world_path}/region") if f.endswith('.mca')]

for i in range(len(files)):
    try:
        region = anvil.Region.from_file(f"{world_path}/region/{files[i]}")
        print(f"File loaded. Progress: {i + 1}/{len(files)}")
        for X in range(32):
            for Z in range(32):
                try:
                    chunk = region.get_chunk(X, Z)
                    print(f"Chunk loaded. Progress: {X * Z}/1024 {i + 1}/{len(files)}")
                    for x in range(16):
                        for z in range(16):
                            for y in range(-63, 319):
                                block = chunk.get_block(x, y, z)
                                print(f"{block.id} ({x}, {y}, {z}). Progress: {x * y + 63 * z}/98048 {X * Z}/1024 {i + 1}/{len(files)}")
                except Exception as e:
                    print(f"Chunk wasn't loaded. Error while loading a chunk: {e}. Progress: {X * Z}/1024 {i + 1}/{len(files)}")
    except Exception as e:
        print(f"Error loading region: {e}. Progress: {i + 1}/{len(files)}")
