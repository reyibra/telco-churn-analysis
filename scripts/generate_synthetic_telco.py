import csv
import random
import argparse

def generate_row(i):
    customerID = f"CUST{i:05d}"
    tenure = random.randint(0,72)
    monthly_charges = round(random.uniform(10,150),2)
    total_charges = round(monthly_charges * max(1,tenure) + random.uniform(-10,50),2)
    contract = random.choices(['Month-to-month','One year','Two year'], weights=[0.6,0.25,0.15])[0]
    internet_service = random.choices(['DSL','Fiber optic','No'], weights=[0.3,0.5,0.2])[0]
    online_security = random.choice(['Yes','No'])
    tech_support = random.choice(['Yes','No'])
    streaming_tv = random.choice(['Yes','No'])
    gender = random.choice(['Female','Male'])
    senior_citizen = random.choices([0,1], weights=[0.9,0.1])[0]
    dependents = random.choice(['Yes','No'])
    payment_method = random.choice(['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    app_usage_min_per_week = random.randint(0,600)
    complaint_count_6m = random.choices([0,1,2,3,4,5], weights=[0.6,0.15,0.1,0.08,0.04,0.03])[0]
    satisfaction_rating = random.randint(1,10)
    engagement_score = round((app_usage_min_per_week/600)*0.5 + (satisfaction_rating/10)*0.5 + random.uniform(-0.1,0.1),3)
    churn_prob = 0.25
    if contract == 'Month-to-month': churn_prob += 0.15
    if tenure < 6: churn_prob += 0.05
    if complaint_count_6m >= 2: churn_prob += 0.15
    if engagement_score < 0.3: churn_prob += 0.1
    churn = 'Yes' if random.random() < churn_prob else 'No'
    return [
        customerID, gender, senior_citizen, dependents, tenure, contract,
        internet_service, online_security, tech_support, streaming_tv,
        monthly_charges, total_charges, payment_method,
        app_usage_min_per_week, complaint_count_6m, satisfaction_rating,
        engagement_score, churn
    ]

def main(out_file, n=3000):
    header = ['customerID','gender','senior_citizen','dependents','tenure','contract',
              'internet_service','online_security','tech_support','streaming_tv',
              'monthly_charges','total_charges','payment_method',
              'app_usage_min_per_week','complaint_count_6m','satisfaction_rating',
              'engagement_score','churn']
    with open(out_file,'w',newline='',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(header)
        for i in range(1, n+1):
            w.writerow(generate_row(i))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', dest='out', default='data/raw/telco_secret.csv')
    parser.add_argument('--n', dest='n', type=int, default=3000)
    args = parser.parse_args()
    main(args.out, args.n)
