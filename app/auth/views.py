# _*_ coding:utf-8 _*_
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Token
from forms import LoginForm, RegistrationForm, DoubanLoginForm
from app.email_module import send_email
from app.auth import auth
import httplib
import urllib
import json


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


domain = "frodo.douban.com"
user_agent = "com.douban.frodo"
conn_url = httplib.HTTPSConnection(domain)
headers = {
    'user-agent': user_agent,
    'content-type': "application/x-www-form-urlencoded"
}


@auth.route('/doubanlogin', methods=['GET', 'POST'])
def doubanlogin():
    form = DoubanLoginForm()
    api_url = "/service/auth2/token"
    request_body = {
        "client_id": "0ab215a8b1977939201640fa14c66bab",
        "client_secret": "22b2cf86ccc81009",
        "grant_type": "password",
        "username": form.email.data,
        "password": form.password.data,

    }
    if form.validate_on_submit():
        conn_url.request("POST", api_url, urllib.urlencode(request_body), headers)
        response = conn_url.getresponse()
        if response.status == 200:
            token = Token()
            db.session.add()
            db.session.commit()
            response_body = response.read().decode("utf-8")
            access_token_dict = json.loads(response_body)
            return redirect('doubanCrawler.html')
        else:
            flash('用户名或密码错误')
    return render_template('auth/doubanlogin.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('验证邮件已发送至您的邮箱，请查收')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('您已成功验证您的邮箱，谢谢！')
    else:
        flash('验证链接已失效或已过期')
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint[:5] != 'auth.':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('新的验证邮件已发送至您的邮箱')
    return redirect(url_for('main.index'))



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已登出！')
    return redirect(url_for('main.index'))


@auth.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed'


