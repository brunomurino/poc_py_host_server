
import pymysql

connection = pymysql.connect(host='mysql',
                     user='root',
                     password='mypassword',
                     db='testing_db')

try:
    with connection.cursor() as cursor:

        # with open('create_table_users.sql') as f:
        #     cursor.execute(f.read())

        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
