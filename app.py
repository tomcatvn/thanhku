from flask import Flask,render_template,url_for,request

import mongoengine

from mongoengine import *

connect(
    'thanhku',
    username = '8f8f8f8',
    password = '123456',
    host = 'ds135798.mlab.com',
    port = 35798
)



app = Flask(__name__)
class Phim(Document):
    tenphim = StringField()
    theloai = StringField()
    thoiluong = StringField()
    duongdan = URLField()
    anh = URLField()



@app.route('/intro')
def intro():

    return render_template('intro.html',phim=Phim.objects)



@app.route('/capnhatphim',methods=["GET","POST"])
def capnhatphim():
    if request.method == "GET":
        return render_template("capnhatphim.html")
    elif request.method == "POST":
        phim = Phim(tenphim = request.form["tenphim"], theloai = request.form["theloai"],
                    thoiluong = request.form["thoiluong"], duongdan=request.form["duongdan"],
                    anh = request.form["anh"])
        phim.save()
        return 'da up len mongodb'

# @app.route('/deletezai/<str:id>')

@app.route('/capnhatphim/xoasua')
def xoasua():
    return render_template("xoasua.html",listsua=Phim.objects)

@app.route('/capnhatphim/xoa/<phimid>')
def xoa(phimid):
    phim = Phim.objects().with_id(phimid)
    phim.delete()
    return 'Đã xóa phim ' +phim.tenphim

@app.route('/capnhatphim/sua/<phimid>',methods=["GET","POST"])
def sua(phimid):

    if request.method == "GET":
        return render_template("sua.html",phimid=phimid)

    elif request.method == "POST":
        phim = Phim.objects().with_id(phimid)
        if request.form["tenphim"] != "":
            phim.update(set__tenphim = request.form["tenphim"])
        if request.form["theloai"] != "":
            phim.update(set__theloai = request.form['theloai'])
        if request.form["thoiluong"] != "":
            phim.update(set__thoiluong = request.form["thoiluong"])
        if request.form["duongdan"] != "":
            phim.update(set__duongdan = request.form["duongdan"])
        if request.form["anh"] != "":
            phim.update(set__anh = request.form["anh"])
        return 'Đã chỉnh sửa phim '+phim.tenphim




if __name__ == '__main__':
    app.run(port =5556)
