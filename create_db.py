import pg8000.native

try:
    con = pg8000.native.Connection(user='postgres', password='postgres', host='localhost', port=5432)
    # create database cannot run in a transaction block
    con.run('COMMIT')
    con.run('CREATE DATABASE buddylearn_db')
    print("Database buddylearn_db created successfully.")
    con.close()
except Exception as e:
    print(f"Error: {e}")
