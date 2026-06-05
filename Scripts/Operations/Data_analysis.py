from .connection import connection

class Analysis_data:
    def __init__(self):
        self.connection=connection()
    def churn_rate(self):
        conn = self.connection
        curr = conn.cursor()

        churn_rate_sql = """
        SELECT
            100.0 * SUM(CASE WHEN customer_status = TRUE THEN 1 ELSE 0 END) / COUNT(*) AS churn_rate_percentage
        FROM analytics;
        """ 

        curr.execute(churn_rate_sql)
        churn_rate = curr.fetchone()[0]
        print("churn rate:", churn_rate, "%")
        
    def top_churned_cities(self):
        conn = self.connection
        curr = conn.cursor()
        top_cities_sql = """
        SELECT city, COUNT(*) AS churned_count
        FROM analytics
        WHERE customer_status=TRUE
        GROUP BY city
        ORDER BY churned_count DESC
        LIMIT 10;
        """

        curr.execute(top_cities_sql)
        top_cities = curr.fetchall()
        print("Top Churned Cities:")
        for city, count in top_cities:
            print(f"  {city}: {count}")

    def tenure_groups(self):
        conn = self.connection
        curr = conn.cursor()

        tenure_group_sql = """
        SELECT
        CASE 
        WHEN tenure BETWEEN 0 AND 12 THEN '0-12 months'
        WHEN tenure BETWEEN 13 AND 24 THEN '13-24 months'
        WHEN tenure BETWEEN 25 AND 36 THEN '25-36 months'
        WHEN tenure BETWEEN 37 AND 48 THEN '37-48 months'
        ELSE '49+ months'
        END AS tenure_group,
        COUNT(*) AS churned_count
        FROM analytics
        WHERE customer_status=TRUE
        GROUP BY tenure_group
        ORDER BY tenure_group;"""
        
        curr.execute(tenure_group_sql)
        tenure_groups = curr.fetchall()
        print("Churned Customers by Tenure Group:")
        for group, count in tenure_groups:
            print(f"  {group}: {count}")
    
    def loss_revenue(self):       
        conn = self.connection
        curr = conn.cursor()
        loss_revenue="""select sum(total_charges) as total_revenue_loas from analytics where customer_status=TRUE;"""
        curr.execute(loss_revenue)
        total_loss = curr.fetchone()[0]
        print("Total Revenue Lost from Churned Customers:")
        print(f"  ${total_loss:,.2f}")

    def population_vs_customer(self):
        conn = self.connection
        curr = conn.cursor()
        population_vs_customer="""select zip_code,population,count(customer_id) as costomer_count from analytics group by zip_code,population order by population desc;"""
        curr.execute(population_vs_customer)
        population_data = curr.fetchall()
        print("Population vs. Customer Count (Top 10):")
        for zip_code, population, customer_count in population_data:
            print(f"  {zip_code}: Population={population}, Customers={customer_count}")
