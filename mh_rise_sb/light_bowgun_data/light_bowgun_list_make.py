import csv

def csv_to_html(csv_file, html_file):
    """
    CSVファイルを読み込み、HTMLファイルに変換する関数

    Args:
      csv_file: 読み込むCSVファイル名
      html_file: 出力するHTMLファイル名
    """

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<meta charset="UTF-8">\n')
        file.write('<title>ライトボウガンデータ</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<table>\n')

        # ヘッダー行の出力
        if data:
            file.write('<tr>\n')
            for header in data[0]:
                file.write(f'<th>{header}</th>\n')
            file.write('</tr>\n')

        # データ行の出力
        for row in data[1:]:
            file.write('<tr>\n')
            for cell in row:
                file.write(f'<td>{cell}</td>\n')
            file.write('</tr>\n')

        file.write('</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')

if __name__ == '__main__':
    csv_to_html('mh_rise_sb/light_bowgun_data/light_bowgun_data - list.csv', 
                'mh_rise_sb/light_bowgun_data/light_bowgun_data.html')