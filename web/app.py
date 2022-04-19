# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from flask import Flask, request,redirect,Response,url_for,abort, render_template,request,send_from_directory
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict #初期値を設定可能な辞書型
from multiprocessing import Value

counter = Value('i', 0)
now_ip = ""
ipadress =[]
app = Flask(__name__)#Flaskクラスのインスタンスをつくる
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "hiogo;go;hgiulaehiwbiulefgawoguwhhaofgahw"

class User(UserMixin):#ユーザー情報(オブジェクト)(現在未使用)
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

# ログイン用ユーザー作成(現在未使用)
users = {
    1: User(1, "kofupass", "Sparkle2020"),
}

# ユーザーチェックに使用する辞書作成(現在未使用)
nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in users.values():
    user_check[i.name]["password"] = i.password
    user_check[i.name]["id"] = i.id

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

##############################################以下URL設定###############################################

@app.route('/')
def protected_index():
    already = False
    if request.headers.getlist("X-Forwarded-For"):
        remote_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        remote_ip = request.remote_addr
    with open("ip_list", "rt") as fin:
        ip_list = fin.read().split('\n')
    for ip in ip_list:
        if ip == remote_ip:
            already = True
    if already is False:
        with open("ip_list", "at") as fout:
            fout.write(remote_ip + '\n')
    return render_template('index.html', count=len(ip_list))

@app.route('/food')
def protected_food():
    return render_template('food.html')

@app.route('/access')
def protected_access():
    return render_template('access.html')

@app.route('/map-highschool')
def protected_maphs():
    return render_template('map-highschool-top.html')

@app.route('/map-highschool/infoh-1')
def protected_infoh1():
    return render_template('infoh-1.html')

@app.route('/map-highschool/infoh-2')
def protected_infoh2():
    return render_template('infoh-2.html')

@app.route('/map-highschool/infoh-3')
def protected_infoh3():
    return render_template('infoh-3.html')

@app.route('/map-highschool/infoh-4')
def protected_infoh4():
    return render_template('infoh-4.html')

@app.route('/map-highschool/infoh-5')
def protected_infoh5():
    return render_template('infoh-5.html')

@app.route('/map-highschool/infoh-6')
def protected_infoh6():
    return render_template('infoh-6.html')        

@app.route('/map-juniorhighschool/infoj-1')
def protected_infoj1():
    return render_template('infoj-1.html')

@app.route('/map-juniorhighschool/infoj-3')
def protected_infoj3():
    return render_template('infoj-3.html')

@app.route('/map-juniorhighschool/infoj-4')
def protected_infoj4():
    return render_template('infoj-4.html')

@app.route('/map-juniorhighschool/infoj-5')
def protected_infoj5():
    return render_template('infoj-5.html')

@app.route('/map-juniorhighschool')
def protected_mapjhs():
    return render_template('map-juniorhighschool-top.html')    

@app.route('/map-stage')
def protected_mapst():
    return render_template('map-stage-top.html')

@app.route('/map-science')
def protected_mapsc():
    return render_template('map-science-top.html')

@app.route('/map-stage/infost-1')
def protected_infost1():
    return render_template('infost-1.html') 

@app.route('/map-stage/infost-2')
def protected_infost2():
    return render_template('infost-2.html')

@app.route('/map-stage/infost-3')
def protected_infost3():
    return render_template('infost-3.html')

@app.route('/map-science/infosc-1')
def protected_infosc1():
    return render_template('infosc-1.html')

@app.route('/map-science/infosc-2')
def protected_infosc2():
    return render_template('infosc-2.html')

@app.route('/map-science/infosc-3')
def protected_infosc3():
    return render_template('infosc-3.html')       

@app.route('/aboutus')
def protected_aboutus():
    return render_template('aboutus.html')

@app.route('/virtual')
def protected_virtual():
    return render_template('Virtual.html')

@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

#########################################################################################################

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="127.0.0.1")
