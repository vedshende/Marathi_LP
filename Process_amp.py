import mysql.connector
from mysql.connector import Error
import plotwave as pw

class DB:
    conn = None    
    
    def connect_db(self):
        try:
            if not self.conn:
                self.conn=mysql.connector.connect(host='localhost',database='audio',user='root',password='myworld')
                print('Connected')
        except Error as e:
            print(e)

    def write_file(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(data)
    
    def add_amp(self):
        query = "SELECT name,voice FROM clips WHERE amplitude=0;" 		#select new recording whose amplitude is yet to be calculated
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            for row in data:
                self.write_file(row[1], 'output/temp.wav')
                amp = float(pw.get_amplitude())
                query = "UPDATE clips SET amplitude=%s WHERE name=%s" 		#Update amplitude of recording
                args = (amp, row[0])
                try:
                    cursor = self.conn.cursor()
                    cursor.execute(query, args)
                    self.conn.commit()
                    print('Final Successful.')
                except Error as e:
                    print(e)
                    
        finally:
            print('Final Successful.')
            cursor.close()

    def calc_avg(self):
        print('In it.')
        query = "SELECT amplitude FROM clips WHERE name like 'Man%';" 		#select new recording whose amplitude is yet to be calculated
        try:
            tot=0
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            for row in data:
                tot += row[0]
            
            length = len(data)
            print(tot)
            print(length)
            avg = float(tot / length)
            print(avg)
            query = "UPDATE avgamp SET Average=%s WHERE name like %s;" 		#select new recording whose amplitude is yet to be calculated
            args = (avg, 'Man%')
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            self.conn.commit()
            print('Final again Successful.')
            
        except Error as e:
            print(e)
                
        finally:
            cursor.close()
            
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
    c1.add_amp()
    c1.calc_avg()
    c1.close_conn()


if __name__ == '__main__':
    main()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
