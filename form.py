from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,FloatField,HiddenField
from wtforms.validators import DataRequired,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed,FileSize

class Create_score_subjectForm(FlaskForm):
    name = StringField('Student name',validators=[DataRequired()])
    math_score = FloatField('Math score',validators=[DataRequired(), NumberRange(min=0, max=100)])
    chinese_score = FloatField('chinese score',validators=[DataRequired(), NumberRange(min=0, max=100)])
    total_score=HiddenField()
    submit = SubmitField()

class EditScoreForm(FlaskForm):
    name = StringField('Student name',validators=[DataRequired()])
    math_score = FloatField('Math score',validators=[DataRequired(), NumberRange(min=0, max=100)])
    chinese_score = FloatField('chinese score',validators=[DataRequired(), NumberRange(min=0, max=100)])
    total_score=HiddenField()
    submit = SubmitField()

class DeleteScoreForm(FlaskForm):
    submit = SubmitField('Delete')

class UploadForm(FlaskForm):
    upload_excel = FileField('Upload excel', validators=[FileRequired(), FileAllowed(['xlsx']),FileSize(max_size=3 * 1024 * 1024)])
    submit = SubmitField()
    #def validate_answer(form, field):
     #   if field.upload_excel != ???: 设置判断文件后缀不是xlsx的验证情况，或者自己在内部做文件格式转换
      #      raise ValidationError('Must be ***.')