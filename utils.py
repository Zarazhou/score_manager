import os,uuid
import datetime

def generate_filename():
    now_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f'test_{now_time}.xlsx'
    return fname
    # return (data.id,data.name,data.math_score,data.chinese_score,data.total_score) -->wrong

def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


'''
    def generate_excel(filename):
        file_path = os.path.join(app.config['DOWNLOAD_PATH'], filename)
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet('test')
        title = ["id", "name", "math_score", "chinese_score", "total_score"]
        worksheet.write_row('A1', title)
        for i in range(len(data_info)):
            row = [data_info[i][0], data_info[i][1], data_info[i][2], data_info[i][3], data_info[i][4]]
            worksheet.write_row('A' + str(i + 2), row)
        workbook.close()

'''
