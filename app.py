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



@app.route('/themphim',methods=["GET","POST"])
def themphim():
    if request.method == "GET":
        return render_template("themphim.html")
    elif request.method == "POST":
        phim = Phim(tenphim = request.form["tenphim"], theloai = request.form["theloai"],
                    thoiluong = request.form["thoiluong"], duongdan=request.form["duongdan"],
                    anh = request.form["anh"])
        phim.save()

        return 'da up len mongodb'

# @app.route('/deletezai/<str:id>')



if __name__ == '__main__':
    app.run(port =5556)
