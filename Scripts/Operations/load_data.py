import psycopg2
from connection import connection

def load_churn_data():
    conn = connection()
    conn.autocommit = True  # 
    curr = conn.cursor()

    curr.execute("""ALTER TABLE churn
                    ALTER COLUMN city TYPE VARCHAR(100);""")
    curr.execute("""ALTER TABLE churn
                    ALTER COLUMN customer_id TYPE VARCHAR(50);""")
    curr.execute("""ALTER TABLE churn
                    ALTER COLUMN zip_code TYPE VARCHAR(20);""")  


    load_data = """
    COPY churn_stage
    FROM 's3://pro-123-aa/raw/sample.csv'
    IAM_ROLE 'arn:aws:iam::103869374478:role/service-role/AmazonRedshift-CommandsAccessRole-20260605T110023'
    CSV IGNOREHEADER 1 DELIMITER ','
    REGION 'ap-south-1';
    """
    curr.execute(load_data)
    print("Data loaded into churn_stage successfully!")

    
    insert_sql = """
    INSERT INTO churn (
        customer_id, city, zip_code, tenure, monthly_charges, total_charges, customer_status
    )
    SELECT
        customer_id,
        city,
        zip_code,
        tenure_in_months,
        monthly_charge,
        total_charges,
        CASE WHEN customer_status='Churned' THEN TRUE ELSE FALSE END
    FROM churn_stage;
    """
    curr.execute(insert_sql)
    print("Data inserted into churn table successfully!")

    conn.commit() 
    curr.close()
    conn.close()

def drop_table():
    conn=connection()
    curr=conn.cursor()

    tab="""drop table churn_stage"""
    curr.execute(tab)
    conn.commit()
    curr.close()
    conn.close()

# load_churn_data()

def zip_data():
    conn = connection()
    curr = conn.cursor()
    load_data = """
    COPY ZIP
    FROM 's3://pro-123-aa/raw/sample1.csv'
    IAM_ROLE 'arn:aws:iam::103869374478:role/service-role/AmazonRedshift-CommandsAccessRole-20260605T110023'
    CSV IGNOREHEADER 1 DELIMITER ','
    REGION 'ap-south-1';
    """
    curr.execute(load_data)
    print("Data loaded into churn_stage successfully!")
    conn.commit() 
    curr.close()
    conn.close()



#drop_table()

zip_data()