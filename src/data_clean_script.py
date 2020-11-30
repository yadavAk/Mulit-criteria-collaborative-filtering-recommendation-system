import csv


filename = 'data.csv'

with open(filename, 'r', encoding='utf-8') as read_csv_file:

    csvreader = csv.reader(read_csv_file) 
    fields = next(csvreader) 

    # to write the cleaned data
    write_csv_file = open('cleaned_data.csv', 'w', encoding='utf-8')
    
    with open('cleaned_data.csv', 'w', encoding='utf-8') as write_csv_file:
        
        csvwriter = csv.writer(write_csv_file, lineterminator='\n')
        
        # Write column names to the cleaned data file
        csvwriter.writerow(fields)

        for row in csvreader:
            
            cleaned_row = []

            for val in row:
                if val == '-1':
                    cleaned_row.append(row[2])
                else:
                    cleaned_row.append(val)
            
            # Write cleaned row to the file
            csvwriter.writerow(cleaned_row)
        


