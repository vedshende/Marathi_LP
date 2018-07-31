import mysql.connector
from mysql.connector import Error
import fileaccess as fa

class DB:
    conn = None
    def connect_db(self):
        try:
            if not self.conn:
                self.conn=mysql.connector.connect(host='localhost',database='audio',user='root',password='myworld')
                print('Connected')
        except Error as e:
                print(e)

#========================================================================================================================================================
    def read_file(self, filename):
        with open(filename, 'rb') as f:
            audio = f.read()
        return audio
#=========================================================================================================================================================
    def insert_blob(self, filename):
	    # read file
	    data = self.read_file('C:/Users/lenovo/Documents/LearnPython/Sounds2/'+filename)

	    # prepare update query and data
	    query = "INSERT INTO clips VALUES(%s, %s, %s, %s);"

	    args = (filename, filename, data, 0)

	    try:
	        cursor = self.conn.cursor()
	        cursor.execute(query, args)
	        self.conn.commit()
	        print('Insert Successful.')
	    except Error as e:
	        print(e)
	    finally:
	        cursor.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def write_file(self, data, filename):
	    with open(filename, 'wb') as f:
	        f.write(data)
#===========================================================================================================================================================
    def read_blob(self, filename):
	    # select photo column of a specific author
	    query = "SELECT voice FROM clips WHERE name=%s LIMIT 0, 1;"
	    args = (filename,)
	    try:
	        # query blob data form the authors table
	        cursor = self.conn.cursor()
	        cursor.execute(query, args)
	        data = cursor.fetchone()[0]

	        # write blob data into a file
	        self.write_file(data, 'output/'+filename)
	        print('Write Successful.')

	    except Error as e:
	        print(e)

	    finally:
	        cursor.close()
#==============================================================================================================================================================

    def close_conn(self):
        try:
            self.conn.close()
            if not self.conn.is_connected():
                print('Disconnected')
            else:
                print('Unsuccessful')
        except Error as e:
            print(e)
#=============================================================================================================================================================

def main():
    c1 = DB()
    c1.connect_db()

    location = fa.fetch_location()       #fa = fileaccess module object
    for file in location:
        fn1 = file.split('/')
        fn = fn1[5].split('\\')
        print(fn[1])
        c1.insert_blob(fn[1])

    #for file in location:
     #   fn1 = file.split('/')
      #  fn = fn1[5].split('\\')
       # print(fn[1])
        #c1.read_blob(fn[1])

    c1.close_conn()


if __name__ == '__main__':
    main()
