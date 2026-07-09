import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Create datasets directory if it doesn't exist
os.makedirs("datasets", exist_ok=True)
np.random.seed(42)

def generate_retail_sales():
    print("Generating Retail Sales Dataset...")
    n_records = 25000
    
    # Generate Customer IDs
    n_customers = 5000
    customer_pool = [f"CUST-{i:04d}" for i in range(1, n_customers + 1)]
    # Use Pareto Principle: 20% of customers generate 65% of orders
    weights = np.random.exponential(scale=1.0, size=n_customers)
    weights /= weights.sum()
    # Adjust weights so top 20% gets exactly 65% weight
    sorted_idx = np.argsort(weights)[::-1]
    top_20_count = int(0.2 * n_customers)
    top_20_idx = sorted_idx[:top_20_count]
    other_idx = sorted_idx[top_20_count:]
    
    weights[top_20_idx] = 0.65 / top_20_count
    weights[other_idx] = 0.35 / (n_customers - top_20_count)
    weights /= weights.sum()
    
    customers = np.random.choice(customer_pool, size=n_records, p=weights)
    
    # Generate Products & Categories
    products = {
        "Electronics": ["Smartphone", "Laptop", "Smartwatch", "Headphones", "Tablet"],
        "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Socks"],
        "Home & Kitchen": ["Blender", "Coffee Maker", "Toaster", "Cookware", "Vacuum"],
        "Books": ["Fiction Novel", "Textbook", "Biography", "Self-Help", "Sci-Fi Comic"],
        "Beauty": ["Perfume", "Skincare Set", "Lipstick", "Shampoo", "Hair Dryer"]
    }
    
    categories = list(products.keys())
    # Category revenue shares: Electronics = 34.1%, Clothing = 25%, Home = 18%, Books = 12%, Beauty = 10.9%
    cat_probs = [0.341, 0.25, 0.18, 0.12, 0.109]
    record_categories = np.random.choice(categories, size=n_records, p=cat_probs)
    
    record_products = []
    record_sales = []
    record_profit = []
    record_quantity = np.random.randint(1, 6, size=n_records)
    
    # Electronics margins are 45%, others vary from 15% to 35%
    margins = {
        "Electronics": 0.45,
        "Clothing": 0.30,
        "Home & Kitchen": 0.25,
        "Books": 0.20,
        "Beauty": 0.35
    }
    
    base_prices = {
        "Electronics": 15000,
        "Clothing": 1200,
        "Home & Kitchen": 3500,
        "Books": 500,
        "Beauty": 1500
    }
    
    for i in range(n_records):
        cat = record_categories[i]
        prod = np.random.choice(products[cat])
        record_products.append(prod)
        
        # Price model
        base_p = base_prices[cat]
        price = np.random.lognormal(mean=np.log(base_p), sigma=0.4)
        
        qty = record_quantity[i]
        sales_val = price * qty
        record_sales.append(sales_val)
        
        profit_val = sales_val * margins[cat]
        record_profit.append(profit_val)
        
    # Generate Order Dates spanning 2025
    start_date = datetime(2025, 1, 1)
    date_offsets = np.random.randint(0, 365, size=n_records)
    
    order_dates = []
    hour_of_day = []
    day_of_week = []
    
    for i in range(n_records):
        offset = date_offsets[i]
        dt = start_date + timedelta(days=int(offset))
        
        # High sales in December (offset 334 to 364)
        if 334 <= offset <= 364:
            # Shift some dates from earlier months to December to boost sales
            if np.random.rand() < 0.4:
                dt = datetime(2025, 12, np.random.randint(1, 32))
                
        # Evening hours (5-8 PM, i.e., 17:00 to 20:59) account for 60% of sales
        if np.random.rand() < 0.60:
            hour = np.random.randint(17, 21)
        else:
            hour = np.random.choice(list(range(0, 17)) + list(range(21, 24)))
            
        dt = dt.replace(hour=hour, minute=np.random.randint(0, 60), second=np.random.randint(0, 60))
        order_dates.append(dt)
        hour_of_day.append(hour)
        day_of_week.append(dt.strftime("%A"))
        
    df = pd.DataFrame({
        "OrderID": [f"ORD-{i:06d}" for i in range(1, n_records + 1)],
        "CustomerID": customers,
        "OrderDate": order_dates,
        "Product": record_products,
        "Category": record_categories,
        "Quantity": record_quantity,
        "Sales": record_sales,
        "Profit": record_profit,
        "Discount": np.random.choice([0.0, 0.05, 0.1, 0.15, 0.2], size=n_records, p=[0.5, 0.2, 0.15, 0.1, 0.05]),
        "Region": np.random.choice(["North", "South", "East", "West"], size=n_records),
        "HourOfDay": hour_of_day,
        "DayOfWeek": day_of_week
    })
    
    # Adjust sales and profit based on discounts
    df["Sales"] = df["Sales"] * (1 - df["Discount"])
    df["Profit"] = df["Profit"] - (df["Sales"] * df["Discount"] * 0.5) # Reduce profit due to discount
    
    # Apply Weekend Promotion boost (40% increase on Sat/Sun)
    weekend_mask = df["DayOfWeek"].isin(["Saturday", "Sunday"])
    df.loc[weekend_mask, "Sales"] = df.loc[weekend_mask, "Sales"] * 1.4
    df.loc[weekend_mask, "Profit"] = df.loc[weekend_mask, "Profit"] * 1.4
    
    # Scale total values to match target stats: Avg transaction value ~1458
    avg_txn = df["Sales"].mean()
    scale_factor = 1458.0 / avg_txn
    df["Sales"] = df["Sales"] * scale_factor
    df["Profit"] = df["Profit"] * scale_factor
    
    df.to_csv("datasets/retail_sales_data.csv", index=False)
    print("Retail sales dataset successfully saved. Shape:", df.shape)


def generate_healthcare():
    print("Generating Healthcare Dataset...")
    n_records = 12000
    
    ages = np.random.randint(0, 95, size=n_records)
    genders = np.random.choice(["Male", "Female", "Other"], size=n_records, p=[0.48, 0.50, 0.02])
    
    departments = ["Pediatrics", "Cardiology", "Oncology", "General Medicine", "Neurology"]
    
    # Pediatrics has patient satisfaction average of 4.7/5.0, others average ~4.0
    patient_depts = []
    for age in ages:
        if age <= 18:
            patient_depts.append("Pediatrics")
        else:
            patient_depts.append(np.random.choice(departments[1:]))
            
    # Satisfaction Scores
    satisfaction = []
    for dept in patient_depts:
        if dept == "Pediatrics":
            satisfaction.append(min(5, max(1, np.random.normal(loc=4.7, scale=0.35))))
        else:
            satisfaction.append(min(5, max(1, np.random.normal(loc=4.0, scale=0.6))))
            
    satisfaction = np.round(satisfaction, 1)
    
    # Admission Date in 2025
    start_date = datetime(2025, 1, 1)
    admission_offsets = np.random.randint(0, 365, size=n_records)
    admission_dates = [start_date + timedelta(days=int(offset)) for offset in admission_offsets]
    
    # Length of Stay (1 to 20 days)
    length_of_stay = np.random.geometric(p=0.15, size=n_records)
    length_of_stay = np.clip(length_of_stay, 1, 30)
    discharge_dates = [adm + timedelta(days=int(los)) for adm, los in zip(admission_dates, length_of_stay)]
    
    # Treatment Cost: Weekend admissions are 30% more costly
    base_costs = {
        "Pediatrics": 30000,
        "Cardiology": 80000,
        "Oncology": 95000,
        "General Medicine": 25000,
        "Neurology": 75000
    }
    
    treatment_costs = []
    for adm, dept, los in zip(admission_dates, patient_depts, length_of_stay):
        base_c = base_costs[dept] * (1 + 0.1 * los)
        cost = np.random.normal(loc=base_c, scale=base_c * 0.15)
        # 30% increase for weekend admissions (Saturday/Sunday)
        if adm.strftime("%A") in ["Saturday", "Sunday"]:
            cost *= 1.3
        treatment_costs.append(max(5000, cost))
        
    treatment_costs = np.round(treatment_costs, 2)
    
    # Staff to Patient Ratio (1:3 to 1:6)
    staff_ratios = np.random.choice([3.0, 4.0, 5.0, 6.0], size=n_records, p=[0.15, 0.45, 0.30, 0.10])
    
    # Telemedicine Follow-Up (randomly assigned to some discharged patients)
    telemedicine = np.random.choice([True, False], size=n_records, p=[0.4, 0.6])
    
    # Readmitted: overall rate ~8.3%
    # Influences:
    # 1. Telemedicine reduces readmission by 45%
    # 2. Early discharge (length of stay <= 3 days) reduces readmission by 25%
    readmitted = []
    for tm, los in zip(telemedicine, length_of_stay):
        base_p = 0.12 # Base readmission probability
        
        if tm:
            base_p *= 0.55 # 45% reduction
        if los <= 3:
            base_p *= 0.75 # 25% reduction
            
        readmitted.append(1 if np.random.rand() < base_p else 0)
        
    df = pd.DataFrame({
        "PatientID": [f"PAT-{i:05d}" for i in range(1, n_records + 1)],
        "Age": ages,
        "Gender": genders,
        "Department": patient_depts,
        "AdmissionDate": admission_dates,
        "DischargeDate": discharge_dates,
        "LengthOfStay": length_of_stay,
        "TreatmentCost": treatment_costs,
        "SatisfactionScore": satisfaction,
        "StaffToPatientRatio": staff_ratios,
        "TelemedicineFollowUp": telemedicine,
        "Readmitted": readmitted
    })
    
    df.to_csv("datasets/healthcare_data.csv", index=False)
    print("Healthcare dataset successfully saved. Shape:", df.shape)


def generate_sports():
    print("Generating Sports Analytics Dataset...")
    n_matches = 2000
    
    teams = [
        "Thunderbolts", "Ironclads", "Strikers", "Phoenix FC", 
        "Vipers", "Titans", "Wizards", "Centurions", "Gladiators", "Knights"
    ]
    
    match_dates = [datetime(2025, 1, 1) + timedelta(days=int(i)) for i in np.random.randint(0, 365, size=n_matches)]
    
    team_a_list = []
    team_b_list = []
    team_a_score = []
    team_b_score = []
    win_probability = []
    outcome = []
    
    # Let's say Team A refers to Thunderbolts. They have a 65% win probability when matching with others.
    for i in range(n_matches):
        t_a = np.random.choice(teams)
        t_b = np.random.choice([t for t in teams if t != t_a])
        
        team_a_list.append(t_a)
        team_b_list.append(t_b)
        
        # Calculate scores
        # Win probabilities
        if t_a == "Thunderbolts":
            win_p = 0.65
        elif t_b == "Thunderbolts":
            win_p = 0.35
        else:
            win_p = 0.50
            
        win_probability.append(win_p)
        
        # Score generation based on win probability
        if np.random.rand() < win_p:
            s_a = np.random.randint(1, 5)
            s_b = np.random.randint(0, s_a)
        elif np.random.rand() < 0.2: # Draw
            s_a = np.random.randint(0, 3)
            s_b = s_a
        else:
            s_b = np.random.randint(1, 5)
            s_a = np.random.randint(0, s_b)
            
        team_a_score.append(s_a)
        team_b_score.append(s_b)
        
        if s_a > s_b:
            outcome.append("Team A Win")
        elif s_b > s_a:
            outcome.append("Team B Win")
        else:
            outcome.append("Draw")
            
    # Player Statistics (for 50 players, 100 matches per player)
    n_player_records = 5000
    player_names = [
        "Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappe", "Erling Haaland", "Kevin De Bruyne",
        "Mohamed Salah", "Harry Kane", "Robert Lewandowski", "Luka Modric", "Virgil van Dijk",
        "Neymar Jr", "Bruno Fernandes", "Marcus Rashford", "Son Heung-min", "Bukayo Saka",
        "Martin Odegaard", "Antoine Griezmann", "Jude Bellingham", "Vinicius Jr", "Rodri",
        "Bernardo Silva", "Pedri", "Gavi", "Jamal Musiala", "Harry Maguire",
        "Declan Rice", "Jack Grealish", "Trent Alexander-Arnold", "Alisson Becker", "Ederson",
        "Casemiro", "Raphael Varane", "Thiago Silva", "Reece James", "Ben Chilwell",
        "Raheem Sterling", "Kai Havertz", "Mason Mount", "Christian Eriksen", "Lisandro Martinez",
        "Antony", "Jadon Sancho", "Darwin Nunez", "Luis Diaz", "Alexis Mac Allister",
        "Dominik Szoboszlai", "Cody Gakpo", "Diogo Jota", "Andrew Robertson", "Virgil van Dijk"
    ][:35] + [f"Player {i}" for i in range(15)]
    
    player_ids = [f"PLR-{i:03d}" for i in range(1, len(player_names) + 1)]
    player_teams = np.random.choice(teams, size=len(player_names))
    player_positions = np.random.choice(["Forward", "Midfielder", "Defender", "Goalkeeper"], size=len(player_names), p=[0.25, 0.40, 0.25, 0.10])
    
    records = []
    for i in range(n_player_records):
        p_idx = np.random.randint(0, len(player_names))
        name = player_names[p_idx]
        pid = player_ids[p_idx]
        team = player_teams[p_idx]
        pos = player_positions[p_idx]
        
        goals = 0
        assists = 0
        tackles = 0
        pass_accuracy = np.random.uniform(65, 95)
        
        if pos == "Forward":
            goals = np.random.choice([0, 1, 2, 3], p=[0.60, 0.30, 0.08, 0.02])
            assists = np.random.choice([0, 1, 2], p=[0.75, 0.20, 0.05])
            tackles = np.random.randint(0, 3)
        elif pos == "Midfielder":
            goals = np.random.choice([0, 1, 2], p=[0.85, 0.12, 0.03])
            assists = np.random.choice([0, 1, 2, 3], p=[0.60, 0.30, 0.08, 0.02])
            tackles = np.random.randint(1, 6)
        elif pos == "Defender":
            goals = np.random.choice([0, 1], p=[0.95, 0.05])
            assists = np.random.choice([0, 1], p=[0.92, 0.08])
            tackles = np.random.randint(3, 10)
        elif pos == "Goalkeeper":
            goals = 0
            assists = 0
            tackles = 0
            pass_accuracy = np.random.uniform(50, 75)
            
        minutes = np.random.choice([90, 90, 90, 75, 60, 45, 15], p=[0.6, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05])
        
        records.append({
            "MatchID": f"MCH-{np.random.randint(1, n_matches + 1):04d}",
            "PlayerID": pid,
            "PlayerName": name,
            "Team": team,
            "Position": pos,
            "Goals": goals,
            "Assists": assists,
            "Tackles": tackles,
            "PassAccuracy": np.round(pass_accuracy, 1),
            "MinutesPlayed": minutes,
            "Rating": np.round(min(10.0, max(4.0, np.random.normal(loc=6.5 + goals*1.2 + assists*0.8 + (tackles*0.1 if pos=="Defender" else 0), scale=0.6))), 1)
        })
        
    df_players = pd.DataFrame(records)
    
    # Store match summaries separately
    df_matches = pd.DataFrame({
        "MatchID": [f"MCH-{i:04d}" for i in range(1, n_matches + 1)],
        "Date": match_dates,
        "TeamA": team_a_list,
        "TeamB": team_b_list,
        "TeamA_Score": team_a_score,
        "TeamB_Score": team_b_score,
        "Possession_TeamA": np.random.randint(35, 65, size=n_matches),
        "Shots_TeamA": np.random.randint(5, 20, size=n_matches),
        "WinProbability": win_probability,
        "Outcome": outcome
    })
    
    df_matches.to_csv("datasets/sports_matches_data.csv", index=False)
    df_players.to_csv("datasets/sports_players_data.csv", index=False)
    print("Sports datasets successfully saved.")


def generate_financial():
    print("Generating Financial Market Dataset...")
    n_days = 1000
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    sectors = {
        "AAPL": "Technology",
        "MSFT": "Technology",
        "GOOGL": "Technology",
        "AMZN": "Consumer Cyclical",
        "TSLA": "Automotive"
    }
    
    start_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(n_days)]
    
    # Exclude weekends to simulate actual market days
    market_dates = [d for d in dates if d.weekday() < 5]
    n_market_days = len(market_dates)
    
    # Base starting prices
    prices = {
        "AAPL": 150.0,
        "MSFT": 250.0,
        "GOOGL": 100.0,
        "AMZN": 110.0,
        "TSLA": 200.0
    }
    
    # Annual drift (bullish signal for tech sector) and volatility
    drifts = {
        "AAPL": 0.18,
        "MSFT": 0.20,
        "GOOGL": 0.15,
        "AMZN": 0.12,
        "TSLA": 0.25
    }
    
    volatilities = {
        "AAPL": 0.22,
        "MSFT": 0.20,
        "GOOGL": 0.25,
        "AMZN": 0.28,
        "TSLA": 0.45
    }
    
    records = []
    
    for ticker in tickers:
        current_price = prices[ticker]
        drift = drifts[ticker] / 252 # daily drift
        vol = volatilities[ticker] / np.sqrt(252) # daily volatility
        
        for i, dt in enumerate(market_dates):
            # Geometric Brownian Motion simulation
            rand_shock = np.random.normal()
            ret = drift + vol * rand_shock
            close_price = current_price * np.exp(ret)
            
            # Intraday fluctuation
            high = max(current_price, close_price) * (1 + abs(np.random.normal(0, 0.008)))
            low = min(current_price, close_price) * (1 - abs(np.random.normal(0, 0.008)))
            open_p = current_price
            
            volume = int(np.random.lognormal(mean=16, sigma=0.5))
            
            records.append({
                "Date": dt.strftime("%Y-%m-%d"),
                "Ticker": ticker,
                "Sector": sectors[ticker],
                "Open": np.round(open_p, 2),
                "High": np.round(high, 2),
                "Low": np.round(low, 2),
                "Close": np.round(close_price, 2),
                "Volume": volume
            })
            current_price = close_price
            
    df = pd.DataFrame(records)
    df.to_csv("datasets/financial_market_data.csv", index=False)
    print("Financial dataset successfully saved. Shape:", df.shape)


def generate_ecommerce():
    print("Generating E-commerce Analytics Dataset...")
    n_customers = 12000
    
    genders = np.random.choice(["Male", "Female"], size=n_customers, p=[0.45, 0.55])
    ages = np.random.randint(18, 70, size=n_customers)
    locations = np.random.choice(["Metro", "Urban", "Suburban", "Rural"], size=n_customers, p=[0.4, 0.3, 0.2, 0.1])
    
    # Signup date
    start_date = datetime(2023, 1, 1)
    signup_offsets = np.random.randint(0, 730, size=n_customers) # Signup in 2023-2024
    signup_dates = [start_date + timedelta(days=int(offset)) for offset in signup_offsets]
    
    order_counts = np.random.negative_binomial(n=3, p=0.15, size=n_customers) + 1 # At least 1 order
    
    total_spends = []
    recencies = []
    average_ratings = np.round(np.random.uniform(1.0, 5.0, size=n_customers) * 0.4 + 3.0, 1)
    average_ratings = np.clip(average_ratings, 1.0, 5.0)
    
    fav_categories = np.random.choice(["Electronics", "Apparel", "Home Decor", "Books", "Beauty"], size=n_customers)
    
    # Generate monetary values and last purchase date
    # Let's say today is Jan 1, 2026
    current_time = datetime(2026, 1, 1)
    
    for i in range(n_customers):
        orders = order_counts[i]
        # Spend distribution dependent on favorite category and order count
        base_spend = {"Electronics": 15000, "Apparel": 2000, "Home Decor": 4000, "Books": 800, "Beauty": 1500}[fav_categories[i]]
        spend = np.random.gamma(shape=orders * 2, scale=base_spend / 2)
        total_spends.append(np.round(spend, 2))
        
        # Last Purchase Date (Offset from signup date to current time)
        signup_dt = signup_dates[i]
        max_days = (current_time - signup_dt).days
        purchase_offset = np.random.randint(0, max_days + 1)
        last_purch = signup_dt + timedelta(days=purchase_offset)
        
        recency_days = (current_time - last_purch).days
        recencies.append(recency_days)
        
    total_spends = np.array(total_spends)
    recencies = np.array(recencies)
    
    # Identify Churn Risk (Recency is high, spend is low, lower rating)
    # Target: Exactly 320 high-risk churn customers identified (e.g. for marketing recommendation)
    # We will score customers and rank the top 320 as high risk
    churn_score = recencies * 0.5 - (total_spends / order_counts) * 0.1 + (5.0 - average_ratings) * 10
    # Normalize to 0-100
    churn_score = (churn_score - churn_score.min()) / (churn_score.max() - churn_score.min()) * 100
    
    # Sort and label the top 320
    top_320_indices = np.argsort(churn_score)[-320:]
    churn_risk = np.zeros(n_customers, dtype=int)
    churn_risk[top_320_indices] = 1
    
    df = pd.DataFrame({
        "CustomerID": [f"CUST-{i:05d}" for i in range(1, n_customers + 1)],
        "Gender": genders,
        "Age": ages,
        "Location": locations,
        "SignupDate": signup_dates,
        "LastPurchaseDate": [current_time - timedelta(days=int(r)) for r in recencies],
        "OrderCount": order_counts,
        "TotalSpend": total_spends,
        "FavCategory": fav_categories,
        "AverageRating": average_ratings,
        "Recency": recencies,
        "Frequency": order_counts,
        "Monetary": total_spends,
        "ChurnRisk": churn_risk
    })
    
    df.to_csv("datasets/ecommerce_customer_data.csv", index=False)
    print("E-commerce dataset successfully saved. Shape:", df.shape)
    print("High Churn Risk Customers:", df["ChurnRisk"].sum())


if __name__ == "__main__":
    generate_retail_sales()
    generate_healthcare()
    generate_sports()
    generate_financial()
    generate_ecommerce()
    print("All datasets successfully generated!")
