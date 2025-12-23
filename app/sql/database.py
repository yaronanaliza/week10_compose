import mysql.connector




# Configuration and call
config = {
    'host': 'localhost',
    'user': 'root',
    # 'password': 'password',
    'database': 'DB_CONTACTS'
}

def check_db_exists(db_name,db_config):
    try:
        # Connect to the server (omit 'database' argument)
        conn = mysql.connector.connect(**db_config)

        cursor = conn.cursor()

        # Query to search for the specific database name
        cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")

        # If fetchone() returns a result, the DB exists
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result is not None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


def run_init_sql(filename, db_config):
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Read the SQL file
        with open(filename, 'r') as f:
            sql_script = f.read()

        # Execute the script
        # multi=True returns an iterator for multiple statements
        results = cursor.execute(sql_script, multi=True)

        # You must consume the iterator to ensure all statements run
        for result in results:
            if result.with_rows:
                result.fetchall()

        conn.commit()
        print(f"Successfully executed {filename}")

    except mysql.connector.Error as err:
        print(f"SQL Error: {err}")
    finally:
        cursor.close()
        conn.close()




def start_db():
    if not check_db_exists("DB_CONTACTS",config):
        run_init_sql('init.sql', config)

