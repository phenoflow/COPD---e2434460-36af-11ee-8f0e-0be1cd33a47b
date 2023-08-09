# Eleanor L Axson, Jennifer K Quint, 2023.

import sys, csv, re

codes = [{"code":"10692761000119107","system":"snomedct"},{"code":"135836000","system":"snomedct"},{"code":"13645005","system":"snomedct"},{"code":"16003001","system":"snomedct"},{"code":"170628003","system":"snomedct"},{"code":"1823851000006103","system":"snomedct"},{"code":"185086009","system":"snomedct"},{"code":"195949008","system":"snomedct"},{"code":"195951007","system":"snomedct"},{"code":"195953005","system":"snomedct"},{"code":"195957006","system":"snomedct"},{"code":"195958001","system":"snomedct"},{"code":"195959009","system":"snomedct"},{"code":"195963002","system":"snomedct"},{"code":"196001008","system":"snomedct"},{"code":"196026004","system":"snomedct"},{"code":"196027008","system":"snomedct"},{"code":"198401000000104","system":"snomedct"},{"code":"198411000000102","system":"snomedct"},{"code":"198901000000105","system":"snomedct"},{"code":"266355005","system":"snomedct"},{"code":"266356006","system":"snomedct"},{"code":"270473001","system":"snomedct"},{"code":"293991000000106","system":"snomedct"},{"code":"313296004","system":"snomedct"},{"code":"313297008","system":"snomedct"},{"code":"313299006","system":"snomedct"},{"code":"383611000000102","system":"snomedct"},{"code":"390891009","system":"snomedct"},{"code":"390941006","system":"snomedct"},{"code":"394702007","system":"snomedct"},{"code":"394703002","system":"snomedct"},{"code":"40100001","system":"snomedct"},{"code":"401184000","system":"snomedct"},{"code":"401185004","system":"snomedct"},{"code":"413845009","system":"snomedct"},{"code":"414087000","system":"snomedct"},{"code":"45145000","system":"snomedct"},{"code":"4981000","system":"snomedct"},{"code":"52571006","system":"snomedct"},{"code":"61937009","system":"snomedct"},{"code":"63480004","system":"snomedct"},{"code":"68328006","system":"snomedct"},{"code":"713731000000102","system":"snomedct"},{"code":"716241000000106","system":"snomedct"},{"code":"716281000000103","system":"snomedct"},{"code":"716358000","system":"snomedct"},{"code":"716901000000101","system":"snomedct"},{"code":"717021000000106","system":"snomedct"},{"code":"717521000000104","system":"snomedct"},{"code":"723245007","system":"snomedct"},{"code":"736283006","system":"snomedct"},{"code":"741056003","system":"snomedct"},{"code":"74417001","system":"snomedct"},{"code":"760601000000107","system":"snomedct"},{"code":"760621000000103","system":"snomedct"},{"code":"77690003","system":"snomedct"},{"code":"826111000000109","system":"snomedct"},{"code":"84409004","system":"snomedct"},{"code":"848431000000106","system":"snomedct"},{"code":"857661000000104","system":"snomedct"},{"code":"866901000000103","system":"snomedct"},{"code":"87433001","system":"snomedct"},{"code":"8743301","system":"snomedct"},{"code":"89549007","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('copd-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["copd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["copd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["copd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
