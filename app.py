import os, xlsxwriter, openpyxl,click
from flask import Flask, render_template, url_for, session, flash, redirect, request, abort, send_from_directory,current_app
from form import Create_score_subjectForm, EditScoreForm, DeleteScoreForm, UploadForm
from flask_sqlalchemy import SQLAlchemy
from utils import generate_filename, random_filename
import contextlib
import pymysql
from sqlalchemy import Column, Float, String

app = Flask(__name__)

app.config['SECRET_KEY'] = 'WFAA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zara:zhourong1995929@127.0.0.1:3306/learning_mysql'
db = SQLAlchemy(app)
app.config['DOWNLOAD_PATH'] = os.path.join(app.root_path, 'downloads')
if not os.path.exists(app.config['DOWNLOAD_PATH']):
    os.makedirs(app.config['DOWNLOAD_PATH'])

app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])


class Score_database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    math_score = db.Column(db.Float)
    chinese_score = db.Column(db.Float)
    total_score = db.Column(db.Float)


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):  #
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')

with app.app_context():
    def get_info():
        datas = Score_database.query.all()
        # print(datas)
        list1 = []
        for data in datas:
            list2 = [data.id, data.name, data.math_score, data.chinese_score, data.total_score]
            # lis2 should be list type, because dict and set type's elements are out-of-order
            list1.append(list2)
        return list1


    # data_info = get_info() #if wtiter there, the downloads program only execute one times

    def generate_excel(filename):
        data_info = get_info()
        # should be writer here, We click to download once,
        # and this function of grabbing information will also be executed synchronously

        file_path = os.path.join(app.config['DOWNLOAD_PATH'], filename)
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet('test')
        title = ["id", "name", "math_score", "chinese_score", "total_score"]
        worksheet.write_row('A1', title)
        for i in range(len(data_info)):
            row = [data_info[i][0], data_info[i][1], data_info[i][2], data_info[i][3], data_info[i][4]]
            # print(row)

            worksheet.write_row('A' + str(i + 2), row)
        workbook.close()


    def delete_excel():
        dirs = os.listdir(app.config['DOWNLOAD_PATH'])
        print(type(dirs[0]))  # dirs is list including str type
        for file in dirs:
            if len(file) != 0:
                absolute_path = (app.config['DOWNLOAD_PATH']) + '/' + file
                os.remove(absolute_path)
                # print(absolute_path)


    def delete_uploadsExcel():
        dirs = os.listdir(app.config['UPLOAD_PATH'])
        print(dirs)
        for file in dirs:
            if len(file) != 0:
                absolute_path = app.config['UPLOAD_PATH'] + '/' + file
                print(absolute_path)
                os.remove(absolute_path)


@app.route('/')
def index():
    form = DeleteScoreForm()
    scores = Score_database.query.order_by(Score_database.total_score.desc())
    return render_template('index.html',scores=scores, form=form)


@app.route('/new', methods=['GET', 'POST'])
def new_form():
    form = Create_score_subjectForm()
    if form.validate_on_submit():
        name = form.name.data
        math_score = form.math_score.data
        chinese_score = form.chinese_score.data
        total_score = math_score + chinese_score
        score_database = Score_database(name=name, math_score=math_score, chinese_score=chinese_score,
                                        total_score=total_score)
        db.session.add(score_database)
        db.session.commit()
        flash('info add it', 'success')
        print(url_for('index'))
        return redirect(url_for('index'))
    scores = Score_database.query.all()
    return render_template('new_form.html', form=form, scores=scores)


@app.route('/edit/<int:form_id>', methods=['GET', 'POST'])
def edit_form(form_id):
    form = EditScoreForm()
    # print('edit', request.form)
    score = Score_database.query.get(form_id)
    if form.validate_on_submit():
        score.name = form.name.data
        score.math_score = form.math_score.data
        score.chinese_score = form.chinese_score.data
        score.total_score = form.math_score.data + form.chinese_score.data
        db.session.commit()
        flash('Your form is updated.')
        return redirect(url_for('index'))
    form.name.data = score.name
    form.math_score.data = score.math_score  # preset form input's value
    form.chinese_score.data = score.chinese_score
    form.total_score.data = score.total_score
    return render_template('edit_form.html', form=form, score=score)


@app.route('/delete/<int:form_id>', methods=['POST'])
def delete_form(form_id):
    form = DeleteScoreForm()
    print(request.form)
    if form.validate_on_submit():
        score = Score_database.query.get(form_id)
        db.session.delete(score)
        db.session.commit()
        flash('Your note is deleted.')
    else:
        return 'wrong page!'
    return redirect(url_for('index'))


@app.route('/downloads')
def downloads():
    with contextlib.ExitStack() as stack:
        stack.callback(delete_excel)
        generate_excel(generate_filename())
        # print(generate_excel(generate_filename()))
        return send_from_directory(app.config['DOWNLOAD_PATH'], generate_filename(), as_attachment=True)


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    form = UploadForm()
    if form.validate_on_submit():
        excel_object = form.upload_excel.data
        filename = random_filename(excel_object.filename)  # got the excel's name
        # print(filename)
        excel_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        # print('excel path',excel_path)#set the absolute path for openpyxl use
        excel_object.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('上传文件成功！.')
        upload_infoToDatabse(excel_path)
        delete_uploadsExcel()  # Control server storage space
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)


def upload_infoToDatabse(filename):
    wb = openpyxl.load_workbook(filename)
    activeSheet = wb.active
    all_values = []
    for row in activeSheet.iter_rows(min_row=1, min_col=2):
        one_row_data = Score_database(name=row[0].value, math_score=row[1].value, chinese_score=row[2].value,
                                      total_score=row[3].value)
        all_values.append(one_row_data)
        db.session.add_all(all_values)
        db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
