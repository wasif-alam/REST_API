import mysql.connector  
import json
from flask import make_response

class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root", password="1234", database="flask_tutorial")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Sucessful")
        except:
            print("Some error ")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall() 
        if len(result) > 0:
            res = make_response({'payload':result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
            # return json.dumps(result)
        else:
            return make_response({"massage":"No data found!"},204 )
        
    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone ,role , password) VALUES('{data['name']}', '{data['email']}','{data['phone']}', '{data['role']}', '{data['password']}')")
        return make_response({"massage":"User created successfully!"}, 201)
     
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"massage":"User Updated successfully!"}, 201)
        else:
            return make_response({"massage":"Nothing to update!"}, 202)
        
    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"massage":"User Deleted successfully!"}, 200)
        else:
            return make_response({"massage":"Nothing to Delete!"}, 202) 
        
    def user_patch_model(self, data, id):
        qry = "UPDATE users SET "
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"massage":"User Updated successfully!"}, 201)
        else:
            return make_response({"massage":"Nothing to update!"}, 202)
        

    def user_pagination_model(self, limit, page):
        limit = int(limit)
        page = int(page)
        start = (page * limit) - limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({'payload': result, "page_no":page, "limit":limit}, 200)
        else:
            return make_response({'message': 'No data found!'}, 204)
    def user_upload_avater_model(self, uid, filePath):
        self.cur.execute(f"UPDATE users SET avater='{filePath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"massage":"User FILE_UPLOADED successfully!"}, 201)
        else:
            return make_response({"massage":"Nothing to update!"}, 202) 