
from itertools import zip_longest

"""
file_process = ['File']
time_file = ['Time']
result_all = []        

  file_process.append(file)
  time_file.append(time.time() - start_all_process)

result_all.append(file_process)
result_all.append(time_file)  

with open(db[0] + 'time.csv', "w+") as f:
            writer = csv.writer(f)
            for values in zip_longest(*result_all):
                writer.writerow(values)
"""


def get_percent_from_file_bxb(filename):

    with open(filename, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        index = 0
        se_v = p_add_v = 0

        for row in csv_reader:
            if index > 0:
                # print('row = ', row[0])
                output = [s.strip() for s in row[0].split(' ') if s]
                if output[0] == 'Average':
                    break
                # print('len output = ', len(output))
                # print('output = ', output)
                if len(output) == 1:
                    continue
                if output[0] == 'Gross':
                    se_v = output[3]
                    p_add_v = output[4]
                    # se_s = output[5]
                    # p_add_s = output[6]

            index += 1

    return se_v, p_add_v
