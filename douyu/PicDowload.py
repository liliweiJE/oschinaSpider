# -*- coding: utf-8 -*-

import urllib.request
import pymysql

class picDowload(object):
    def __init__(self):
        self.connect=pymysql.connect(
            host='localhost',
            db='crm',
            user='root',
            passwd='',
            charset='utf8',
            use_unicode=True
        )
        self.cursor=self.connect.cursor()

    def selectImport(self):
        self.cursor.execute('select id,imgurl from importnew_doc WHERE  id > %s' ,3096)
        self.connect.commit()
        row_all=self.cursor.fetchall()
        for i in range(row_all.__len__()):
            row_one=list(row_all)[i][1]
            row_id = list(row_all)[i][0]
            now_url=self.dowPic(row_one,i)
            self.update(row_id,now_url)

    def update(self,id, im):
        sql = "UPDATE importnew_doc SET imgurl=%s WHERE id=%s "
        sta = self.cursor.execute(sql,(im,id))
        self.connect.commit()
        if sta == 1:
            print('Done')
        else:
            print('Failed')

    def dowPic(self,url,name):
        now_url="D:\\index\\%s.jpg" % name
        urllib.request.urlretrieve(url,now_url)
        return now_url

if __name__=='__main__':
    pd=picDowload()
    pd.selectImport()

