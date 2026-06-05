from connection import connection

def optimize_redshift():
    conn = connection()

    conn.autocommit = True

    curr = conn.cursor()

    curr.execute("VACUUM analytics;")
    print("VACUUM completed")

    curr.execute("ANALYZE analytics;")
    print("ANALYZE completed")

    curr.close()
    conn.close()

optimize_redshift()