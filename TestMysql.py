import pymysql


class Dept(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id}\t{self.name}'


def main():
    conn = pymysql.connect(host='192.168.21.109', port=3306,
                           user='root', password='123456',
                           db='testdb', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    print(conn)
    try:
        with conn.cursor() as cursor:
            cursor.execute('select id,name from name_table')
            for row in cursor.fetchall():
                dept = Dept(**row)
                print(dept)
                # print(row["id"], end='\t')
                # print(row["name"])
            # print(cursor.fetchone())
            # print(cursor.fetchall())
            # result = cursor.execute('insert into name_table values(1,"易维")')
            # if result == 1:
            #     print('添加成功')
            # conn.commit()
            # if result == 1:
            #     print('add success')
            # conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
