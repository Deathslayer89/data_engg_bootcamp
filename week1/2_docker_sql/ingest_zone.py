import os
import pandas as pd
from sqlalchemy import create_engine

def main():
    # Get the current working directory
    cwd = os.getcwd()

    # Specify the filename to read data from
    filename = "taxi_zone_lookup.csv"

    # Construct the full file path
    file_path = os.path.join(cwd, filename)

    # Create a SQLAlchemy engine
    engine = create_engine(f'postgresql://root:root@pgdatabase:5432/ny_taxi')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Create the zones table if it doesn't exist
    df.head(n=0).to_sql('zones', engine, if_exists='replace', index=False)

    # Insert the data into the zones table
    df.to_sql('zones', engine, if_exists='append', index=False)

    print("Data ingested into the zones table successfully.")

if __name__ == '__main__':
    main()