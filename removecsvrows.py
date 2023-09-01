import csv
import os

os.chdir('C:\\Users\\linds\\Desktop\\44671-80\\Module_02\\streaming-02-multiple-processes') # changes working directory to the correct child path vs. the default folder in python
input_file_name = "spotifytop200songs.csv"  # Replace with your CSV file's name
output_file_name = "spotifytop200songsslimversion.csv"  # Name for the new CSV file with 5000 rows

# Open the input and output CSV files
with open(input_file_name, "r", newline="", encoding="utf-8") as input_file, \
     open(output_file_name, "w", newline="", encoding="utf-8") as output_file:

    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the header row (if it exists) to the output file
    header = next(reader, None)
    if header:
        writer.writerow(header)

    # Write the first 5000 rows to the output file
    for i, row in enumerate(reader):
        if i < 5000:
            writer.writerow(row)
        else:
            break

print(f"{output_file_name} created with 5000 rows.")
