import pandas as pd
import os

DATASET_PATH = "dataset.csv"
CHUNK_SIZE = 10000
OUTPUT_DIR = "output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "chunk_{index}.parquet")

def run():
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for i, chunk in enumerate(pd.read_csv(DATASET_PATH, chunksize=CHUNK_SIZE)):
            output_file = OUTPUT_PATH.format(index=i)
            chunk.to_parquet(output_file, index=False)
            print(f"Chunk {i} saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {DATASET_PATH} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run()