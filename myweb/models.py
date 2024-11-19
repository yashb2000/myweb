import pymysql

class EmpOperations:
    def checkuser(self,id,ps):
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from users where userid='%s' and psw='%s'" %(id,ps))
        data=curs.fetchone()
        if data:
            page="Admin.html"
        else:
            page="Failure.html"
        con.close()
        return page
    
    def addemp(self,no,nm,dp,lo,po,sl):
        try:
            con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
            curs=con.cursor()
            curs.execute("insert into employees values(%d,'%s','%s','%s','%s','%.2f')" %(no,nm,dp,po,lo,sl))
            con.commit()
            msg="Employee added successfully"
            con.close()
        except:
            msg="Failed to add Employee"
        
        return msg

    def serachonempno(self,no):
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from employees where empno=%d" %no)
        data=curs.fetchone()
        print(data) 
        dic={}
        if data:
            dic['empno']=data[0]
            dic['empnm']=data[1]
            dic['dept']=data[2]
            dic['post']=data[3]
            dic['location']=data[4]
            dic['salary']=data[5]
        else:
            dic['empno']=no
            dic['empnm']='not found'
            dic['dept']='na'
            dic['post']='na'
            dic['location']='na'
            dic['salary']=0
        con.close()
        return dic

    def getallemp(self):
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from employees")
        data=curs.fetchall()
        con.close()
        return data
    
    
    def changesalary(self,no,sal):
        msg=None
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from employees where empno=%d" %no)
        data=curs.fetchone()
        if data:
            curs.execute("update employees set salary=%.2f where empno=%d" %(sal,no))
            con.commit()
            msg="salary updated successfully"
        else:
            msg="employee not found"
        
        con.close()
        return msg
    
    def deleteemp(self,no):
        msg=None
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from employees where empno=%d" %no)
        data=curs.fetchone()

        if data:
            curs.execute("insert into delemps values(%d,'%s','%s','%s','%s',%.2f,now())" %(data[0],data[1],data[2],data[3],data[4],data[5]))
            con.commit()
            curs.execute("delete from employees where empno=%d" %no)
            con.commit()
            msg='employee deleted successfully'
        else:
            msg='employee not found'
        
        print(msg)
        con.close()
        return msg
    
    def emplist(self):
        con=pymysql.connect(host='bfkbvujl9ds3vcmjau0a-mysql.services.clever-cloud.com',user='upvz3pkgoyt29gmf',password='5XwI1MHonNZGFZD8N5tf',database='bfkbvujl9ds3vcmjau0a')
        curs=con.cursor()
        curs.execute("select * from employees where %d"  )
