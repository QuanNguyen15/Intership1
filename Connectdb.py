import pyodbc


def connections():

    print(pyodbc.drivers())
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                SERVER=DESKTOP-9HGBU5H\SQLEXPRESS; '
                                'Database=Student_Timetable2; UID=mq; PWD=151611')
    return connection