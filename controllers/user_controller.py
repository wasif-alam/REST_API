from app import app
from model.user_model import *
from flask import request, send_file
from datetime import datetime
obj=user_model()

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods= ['POST'])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/update", methods= ['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>", methods= ['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>", methods= ['PATCH'])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

@app.route("/user/getall/limit/<limit>/page/<page>", methods= ['GET'])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)

@app.route("/user/<uid>/upload/avater", methods=['PUT'])
def user_upload_avater_controller(uid):
    file = request.files['avater']
    uniqueFileName = str(datetime.now().timestamp()).replace(".", "")
    FileNameSplit = file.filename.split(".")
    ext = FileNameSplit[len(FileNameSplit)-1]
    finalFilePath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    return obj.user_upload_avater_model(uid,finalFilePath)

@app.route("/uploads/<filename>")
def user_getavater_controller(filename):
    return send_file(f"uploads/{filename}")
