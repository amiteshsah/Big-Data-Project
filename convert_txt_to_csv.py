import csv

txt_file = r"part-00000"
csv_file = r"result1.csv"


in_txt = csv.reader(open(txt_file, "rb"), delimiter = '~')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)



