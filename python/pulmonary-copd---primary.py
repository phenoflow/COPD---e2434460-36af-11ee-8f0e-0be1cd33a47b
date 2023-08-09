# Eleanor L Axson, Jennifer K Quint, 2023.

import sys, csv, re

codes = [{"code":"14B3.12","system":"readv2"},{"code":"66YI.00","system":"readv2"},{"code":"679V.00","system":"readv2"},{"code":"8CR1.00","system":"readv2"},{"code":"9Nk7000","system":"readv2"},{"code":"H36..00","system":"readv2"},{"code":"H37..00","system":"readv2"},{"code":"H3?00","system":"readv2"},{"code":"H3B..00","system":"readv2"},{"code":"H3z..11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('copd-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pulmonary-copd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pulmonary-copd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pulmonary-copd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
