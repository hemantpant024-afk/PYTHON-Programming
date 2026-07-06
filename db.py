import mysql.connector
from mysql.connector import Error

class DBConnection:

    def connect(self, query: str, param) -> list:
        try:
            # 1. Establish the connection
            connection = mysql.connector.connect(
                host="sql12.freesqldatabase.com",
                database="sql12832358",
                user="sql12832358",
                password="wbcVqElhAR",
                port=3306                  # Default MySQL port
            )

            if connection.is_connected():
                print("Successfully connected to the database!")
                
                # 2. Create a cursor object to execute queries
                cursor = connection.cursor(buffered=True)
                cursor.execute(query, (param,))
                result = cursor.fetchone()

                print(f"Data:: {result}")
                return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

        finally:
            # 3. Always close the connection when done
            if cursor:
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")


    def get_student_data(self, roll_num: str):
        query: str = "SELECT roll_num, name, age, branch, blood_group, mobile_num FROM student WHERE roll_num = %s"
        self.connect(query=query, param=roll_num)
        
