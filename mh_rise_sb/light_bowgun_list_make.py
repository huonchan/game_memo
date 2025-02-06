import csv

def read_csv(filename):
  """
  CSVファイルを読み込んでコンソールに出力する関数

  Args:
    filename: 読み込むCSVファイル名
  """

  with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
      print(row)

if __name__ == '__main__':
  read_csv('mh_rise_sb/light_bowgun_data - list.csv')  # 'data.csv' を読み込む