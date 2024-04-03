import psycopg2
import os

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="ny_taxi",
    port=5432,
    user="root",
    password="root"
)

# Create a cursor object
cur = conn.cursor()

# Get the current working directory
cwd = os.getcwd()

# Specify the filename to read data from
filename = "taxi_zone_lookup.csv"

# Construct the full file path
file_path = os.path.join(cwd, filename)

# Open the file and read its contents
with open(file_path, "r") as file:
    lines = file.readlines()

# Get the column names from the first line
column_names = lines[0].strip().split(",")

# Skip the first line (column names) when inserting data
for line in lines[1:]:
    values = line.strip().split(",")
    
    # Construct the SQL INSERT statement with column names
    columns = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))
    insert_query = f"INSERT INTO your_table ({columns}) VALUES ({placeholders})"
    
    # Execute the INSERT statement
    cur.execute(insert_query, values)

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cur.close()
conn.close()