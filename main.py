from Scripts.Operations.Data_analysis import Analysis_data


def main():
    analysis = Analysis_data()
    analysis.churn_rate()
    analysis.top_churned_cities()
    analysis.tenure_groups()
    analysis.loss_revenue()
    analysis.population_vs_customer()


if __name__ == "__main__":
    main()
    