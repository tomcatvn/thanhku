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
    phim=[
        {
            "name":"Moana",
            "desc1": "Hoạt hình, Gia đình",
            "desc2":"105 phút",
            "ref":"https://www.cgv.vn/vn/hanh-trinh-cua-moana.html",
            "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/m/o/moana_240x355.jpg"

        },
    {
        "name":"Vệ Sĩ Sài Gòn",
        "desc1":"Hành động, Hài",
        "desc2":"100 phút",
        "ref":"https://www.cgv.vn/vn/ve-si-sai-gon.html",
        "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/v/s/vssg_mainposter_240x355_1.jpg"
            },
    {
        "name":"Sing",
        "desc1":"Hoạt hình, Hài",
        "desc2":"110 phút",
        "ref":"https://www.cgv.vn/vn/dau-truong-am-nhac.html",
        "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/s/i/sing-poster-240x355.jpg"
    },
        {
            "name":"Underworld",
            "desc1":"Hành Động, Kinh Dị",
            "desc2":"95 phút",
            "ref":"https://www.cgv.vn/vn/the-gioi-ngam-tran-chien-dam-mau.html",
            "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/u/n/underworld_240x355.jpg"

        },
        {
            "name":"Incarnate",
            "desc1":"Kinh dị",
            "desc2":"90 phút",
            "ref":"https://www.cgv.vn/vn/quy-am.html",
            "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/i/n/incarnate-240x355.jpg"

        },
        {
            "name":"Thần Kiếm",
            "desc1":"Võ thuật",
            "desc2":"110 phút",
            "ref":"https://www.cgv.vn/vn/than-kiem.html",
            "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/s/m/sm_240x355.jpeg"
        },
        {
            "name":"Eliminators",
            "desc1":"Hành động, Tội phạm",
            "desc2":"100 phút",
            "ref":"https://www.cgv.vn/vn/doi-thanh-trung.html",
            "img":"https://www.cgv.vn/media/catalog/product/cache/1/small_image/210x310/0f396e8a55728e79b48334e699243c07/e/l/eliminators_240x355.jpg"

        }

    ]
    return render_template('intro.html',phim=phim)

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



if __name__ == '__main__':
    app.run(port =5555)
