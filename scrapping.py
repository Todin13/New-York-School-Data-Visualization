import csv

input_file = 'output2.csv'
output_file = 'output3.csv'

with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in, delimiter=';')
    writer = csv.writer(file_out, delimiter=';')

    # Write the header row
    writer.writerow(['Name', 'Latitude', 'Longitude', 'Address'])

    for row in reader:
        name = row[0]
        latitude = row[1]
        longitude = row[2]
        address = row[3]

        # Remove duplicate information at the end of the address
        if address.endswith(name):
            common_prefix = address[:len(address) - len(name)].strip()
            address = address[len(common_prefix):].strip()

        writer.writerow([name, latitude, longitude, address])
