#!/usr/bin/python3
"""
Lists all values in the states table of a database where name
matches the argument.
"""

import sys
import MySQLdb

def main():
    """Main function to execute the script."""
    try:
        # Connect to the database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)

        # Create a cursor object to execute SQL queries
        with db.cursor() as cur:
            # Prepare and execute the SQL query
            query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
            cur.execute(query, (sys.argv[4],))

            # Fetch all rows returned by the query
            states = cur.fetchall()

            # Print the fetched rows
            for state in states:
                print(state)
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if db:
            db.close()

if __name__ == '__main__':
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    main()

