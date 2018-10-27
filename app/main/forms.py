# _*_ coding:utf-8 _*_
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_pagedown.fields import PageDownField


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('昵称', validators=[Length(0, 64)])
    location = StringField('所在城市', validators=[Length(0, 64)])
    avatar = FileField('上传头像')
    about_me = TextAreaField('一句话描述自己')
    submit = SubmitField('提交')


class PostForm(FlaskForm):
    body = PageDownField("写下你现在的想法...", validators=[DataRequired()])
    submit = SubmitField('发布')


class CommentForm(FlaskForm):
    body = StringField('', validators=[DataRequired()])
    submit = SubmitField('提交')