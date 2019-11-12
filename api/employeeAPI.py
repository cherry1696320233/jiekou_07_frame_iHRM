"""设计员工模块的增删改查"""
import app
from app import BASE_URL


class EmployeeDeal:

    def __init__(self):
        self.emp_url = BASE_URL + "/api/sys/user"
    #增
    def add_emp_func(self,session,username=None,mobile=None,timeOfEntry=None,
                 formOfEmployment=None,workNumber=None,departmentName=None,
                 departmentId=None,correctionTime=None):
        my_add = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry":timeOfEntry,
                    "formOfEmployment": formOfEmployment,
                    "workNumber": workNumber,
                    "departmentName": departmentName,
                    "departmentId": departmentId,
                    "correctionTime": correctionTime}

        return session.post(self.emp_url,json=my_add,headers ={"Authorization":"Bearer "+ app.TOKEN})
    #API改
    def update_emp_func(self,session,id,username):
        return session.put(self.emp_url + "/"+id,json={"username":username},headers ={"Authorization":"Bearer "+ app.TOKEN})
    #API查
    def get_emp_func(self,session,id):
        return session.get(self.emp_url + "/"+id,headers ={"Authorization":"Bearer "+ app.TOKEN})
    #API删
    def delete_emp_func(self,session,id):
        return session.delete(self.emp_url + "/" + id,headers ={"Authorization":"Bearer "+ app.TOKEN})