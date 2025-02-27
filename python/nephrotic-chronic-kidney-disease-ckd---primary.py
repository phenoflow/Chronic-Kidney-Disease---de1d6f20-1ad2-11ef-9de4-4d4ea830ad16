# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2024.

import sys, csv, re

codes = [{"code":"K01x300","system":"readv2"},{"code":"K01z.00","system":"readv2"},{"code":"K01..00","system":"readv2"},{"code":"K01x400","system":"readv2"},{"code":"K013.12","system":"readv2"},{"code":"K01x200","system":"readv2"},{"code":"K01x000","system":"readv2"},{"code":"K01w.00","system":"readv2"},{"code":"K01x100","system":"readv2"},{"code":"K01A.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-kidney-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nephrotic-chronic-kidney-disease-ckd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nephrotic-chronic-kidney-disease-ckd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nephrotic-chronic-kidney-disease-ckd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
