import psycopg2
from connection import connection

class CreteTable:
    def create_churn_table():
        conn=connection()
        cursor=conn.cursor()

        churn_table_querry="""
        CREATE TABLE IF NOT EXISTS churn (
            customer_id VARCHAR(20),
            city VARCHAR(20),
            ZIP_code VARCHAR(10),
            population INT,
            tenure BIGINT,
            monthly_charges DeCIMAL(10,2),
            total_charges DECIMAL(10,2),
            customer_status BOOLEAN
        )
    """
        cursor.execute(churn_table_querry)
        print("Churn table created successfully!")
        conn.commit()
        cursor.close()
        conn.close()
        

    def create_zip_table():
        conn=connection()
        cursor=conn.cursor()

        zip_code_table="""
        CREATE TABLE IF NOT EXISTS ZIP(
        zip_code INT,
        population BIGINT)"""
        
        cursor.execute(zip_code_table)
        print("Churn table created successfully!")
        conn.commit()
        cursor.close()
        conn.close()

    def churn_stage_table():
        conn=connection()
        cursor=conn.cursor()

        churn_table_querry="""
        CREATE TABLE IF NOT EXISTS churn_stage (
        customer_id VARCHAR(20),
        gender VARCHAR(20),
        age INT,
        married VARCHAR(10),
        number_of_dependents INT,
        city VARCHAR(100),
        zip_code VARCHAR(20),
        latitude DECIMAL(12,8),
        longitude DECIMAL(12,8),
        number_of_referrals INT,
        tenure_in_months INT,
        offer VARCHAR(50),
        phone_service VARCHAR(20),
        avg_monthly_long_distance_charges DECIMAL(10,2),
        multiple_lines VARCHAR(20),
        internet_service VARCHAR(20),
        internet_type VARCHAR(50),
        avg_monthly_gb_download INT,
        online_security VARCHAR(20),
        online_backup VARCHAR(20),
        device_protection_plan VARCHAR(20),
        premium_tech_support VARCHAR(20),
        streaming_tv VARCHAR(20),
        streaming_movies VARCHAR(20),
        streaming_music VARCHAR(20),
        unlimited_data VARCHAR(20),
        contract VARCHAR(50),
        paperless_billing VARCHAR(20),
        payment_method VARCHAR(100),
        monthly_charge DECIMAL(10,2),
        total_charges DECIMAL(10,2),
        total_refunds DECIMAL(10,2),
        total_extra_data_charges DECIMAL(10,2),
        total_long_distance_charges DECIMAL(10,2),
        total_revenue DECIMAL(10,2),
        customer_status VARCHAR(20),
        churn_category VARCHAR(100),
        churn_reason VARCHAR(500));"""

        
        cursor.execute(churn_table_querry)
        print("Churn table created successfully!")
        conn.commit()
        cursor.close()
        conn.close()

    def analytics_table():
        conn = connection()
        corr = conn.cursor()

        create_sql = """
        CREATE TABLE IF NOT EXISTS analytics (
            customer_id VARCHAR(50),
            city VARCHAR(100),
            zip_code VARCHAR(20),
            population INT,
            monthly_charges DECIMAL(10,2),
            total_charges DECIMAL(10,2),
            customer_status BOOLEAN,
            tenure BIGINT
        )
        DISTSTYLE KEY
        DISTKEY(zip_code)
        SORTKEY(tenure);
        """
        corr.execute(create_sql)
        conn.commit()
        print("Analytics table created successfully!")

        insert_sql = """
        INSERT INTO analytics
        SELECT
            c.customer_id,
            c.city,
            c.zip_code,
            z.population,
            c.monthly_charges,
            c.total_charges,
            c.customer_status,
            c.tenure
        FROM churn c
        JOIN zip z ON c.zip_code = z.zip_code;
        """
        corr.execute(insert_sql)
        conn.commit()
        print("Analytics table populated successfully!")

        corr.close()
        conn.close()


cr=CreteTable()
 
cr.create_churn_table()
cr.create_zip_table()
cr.churn_stage_table()


cr.analytics_table()