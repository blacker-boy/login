import web
import pymysql
import os
import json
# import model
import util
import sys
import os
import shutil
import imp

# imp.reload(sys)
# sys.setdefaultencoding("utf-8")

sys.path.append('../')
from config import configs
from model import model
import web
import util
from model.orm import *
urls=(
    '/Adminlogin','Admin_Login',
    '/Register','Register',
    '/SelectTeacher','SelectTeacher',
    '/AddTeacher','AddTeacher',
)
app=web.application(urls,globals())

class Admin_Login:
    def GET(self):
        # print (os.getcwd())

        # print(os.getcwd())
        # os.chdir('D:\PycharmProjects\login')
        os.chdir('../')
        # print(os.getcwd())
        return web.seeother('/static/index.html',True)
    def POST(self):
        # print(5)
        params=web.input()
        x=params['admin_id']
        y=params['password']
        x=str(x)
        y=str(y)
        # print(x,y)
        db = pymysql.connect("localhost", port=3306, user="admin", passwd="123456", db="admin_login", charset='utf8')
        cursor=db.cursor()
        sql= '''select * from adminlogin '''
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                adminid = row[0]
                password = row[1]
                # print(adminid, password)
                if  adminid==x  and  password==y :
                    return 1
                    break
            else:
                return False
        except:
            db.rollback()
        cursor.close()
        db.close()
class Register:
    def POST(self):
        params = web.input()
        x = params['admin_id']
        y = params['password']
        x = str(x)
        y = str(y)
        print(x,y)
        db = pymysql.connect("localhost", port=3306, user="admin", passwd="123456", db="admin_login", charset='utf8')
        cursor = db.cursor()
        sql = '''select * from adminlogin '''
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                adminid = row[0]
                password = row[1]
                print(adminid)
                if x == adminid:
                    print('000')
                    return False
                    break
            else:
                print(6)
                sql = """insert into adminlogin(
                                  ID_admin,password)
                                  values('{}','{}')""".format(x,y)
                print(sql)
                try:
                    cursor.execute(sql)
                    db.commit()
                    print(5)
                except:
                    db.rollback()
            return 1
        except:
            db.rollback()
        cursor.close()
        db.close()
class SelectTeacher:
    def POST(self):
        params=web.input()
        print(params)
        db = pymysql.connect("localhost", port=3306, user="admin", passwd="123456", db="examdb", charset='utf8')
        cursor=db.cursor()
        sql = '''select * from teacher '''
        cursor.execute(sql)
        results = cursor.fetchall()
        results=list(results)
        print(type(results),results)
        # new_dict=dict(results)
        # print(new_dict)
        result=json.dumps(results)
        print(type(result),result)
        # return result
        cursor.close()
        db.close()
        jsonResults=[]
        for row in results:
            data={}
            data["tc_id"]=row[0]
            data["tc_name"]=row[1]
            data["tc_password"]=row[2]
            data["tc_level"]=row[3]
            data["lenth"]=len(results)
            jsonResults.append(data)
        print(results)
        # result=list(results)
        # print(type(results))
        # print("next")
        print(jsonResults)
        return util.objtojson(jsonResults)
# class SelectTeacher:
#     def POST(self):
#         web.header("Access-Control-Allow-Origin", "*")
#         # 接收参数
#         params = web.input()
#         # session = web.ctx.session
#         count = model.Teacher_model.count()
#         if params.tc_name == '' and params.tc_id == '':
#             teacher = model.Teacher_model.query('select * from teacher ')
#             teacher = [model.Teacher_model(**item) for item in teacher]
#             print("teacher",teacher)
#             page = util.Page(data=teacher, totalRow=count,
#                              status=util.Status.__success__, message="未知")
#             response = util.Response(status=util.Status.__success__, body=page)
#             return util.objtojson(response)
#         elif params.tc_name != '' and params.tc_id == '':
#             teacher = model.Teacher_model.query('select * from teacher where tc_name ')
#             teacher = [model.Teacher_model(**item) for item in teacher]
#             page = util.Page(data=teacher, totalRow=teacher.__len__(),
#                              status=util.Status.__success__, message="未知")
#             response = util.Response(status=util.Status.__success__, body=page)
#             return util.objtojson(response)
#         else:
#             teacher = model.Teacher_model.getByPK(params.tc_id)
#             page = util.Page(data=teacher, totalRow=1),
#                              status=util.Status.__success__, message="未知")
#             response = util.Response(status=util.Status.__success__, body=page)
#             print(response)
#             return util.objtojson(response)
class AddTeacher:
    def POST(self):
        params = web.input()
        x = str(params['tc_id'])
        y = str(params['tc_name'])
        m = str(params['tc_password'])
        n = str(params['tc_level'])
        # x = str(x)
        # y = str(y)
        print(x,y,m,n)
        db = pymysql.connect("localhost", port=3306, user="admin", passwd="123456", db="examdb", charset='utf8')
        cursor = db.cursor()
        sql = '''select * from teacher '''
        # try:
        #     cursor.execute(sql)
        #     results = cursor.fetchall()
        #     result=list(results)
        #     lenth=len(result)
        #     print("len=",lenth)
        #     for row in results:
        #         tc_id = row
        #         # password = row[1]
        #         print(tc_id)
        #         if x == tc_id:
        #             # print('000')
        #             return False
        #             break
        #     else:
        #         print('add1')
        #         sql = """insert into teacher(
        #                           tc_id,
        #                           tc_name,
        #                           tc_password,
        #                           tc_level)
        #                           values('{}','{}','{}','{}')""".format(x,y,m,n)
        #         try:
        #             cursor.execute(sql)
        #             db.commit()
        #             print(51)
        #         except:
        #             db.rollback()
        #     return 1
        # except:
        #     db.rollback()
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print(type(results))
        print("next")
        return results
        result = list(results)
        print(result)
        print(type(result))
        lenth = len(result)
        print("len2=", lenth)
        for row in results:
            # tc_id = row
            # password = row[1]
            print(row)
        #     if x == tc_id:
        #         # print('000')
        #         return False
        #         break
        cursor.close()
        db.close()

if __name__=='__main__':
    app.run()
