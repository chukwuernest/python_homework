import os
import time
import sqlite3
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def stage1_scrape_data():
    print(" Stage 1: Scraping MLB data... \n")

    url = "https://www.baseball-reference.com/leagues/MLB/"
    output_csv = "mlb_history.csv"

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    try:
        table = driver.find_element(By.XPATH, '//table[contains(@class, "stats_table")]')
        rows = table.find_elements(By.TAG_NAME, "tr")

        data = []
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")

           
            if len(cols) < 6:
                continue

            year = cols[0].text.strip()
            league = cols[1].text.strip()
            team = cols[2].text.strip()
            wins = cols[3].text.strip()
            losses = cols[4].text.strip()
            win_pct = cols[5].text.strip()

            data.append([year, league, team, wins, losses, win_pct])

        df = pd.DataFrame(data, columns=["Year", "League", "Team", "Wins", "Losses", "Win_Pct"])
        df.to_csv(output_csv, index=False)
        print(f" Data scraped and saved to {output_csv}")

    except Exception as e:
        print(" Failed to locate table element. Check XPath or page structure.")
        print("Error details:", str(e))

    driver.quit()



def stage2_import_to_sqlite():
    print("\n Stage 2: Importing CSV to SQLite...")

    csv_file = "mlb_history.csv"
    db_file = "mlb_data.db"

    if not os.path.exists(csv_file):
        print(f" CSV file {csv_file} not found. Run stage1_scrape_data() first.")
        return

    try:
        df = pd.read_csv(csv_file)
        conn = sqlite3.connect(db_file)
        df.to_sql("mlb_stats", conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()
        print(f" Data imported into {db_file}")

    except Exception as e:
        print(" Error importing CSV to database:", str(e))



def stage3_query_database():
    print("\nStage 3: Querying database...")

    db_file = "mlb_data.db"
    if not os.path.exists(db_file):
        print(f"Database file {db_file} not found.")
        return

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        query = """
            SELECT Team, Wins, Losses, Win_Pct
            FROM mlb_stats
            WHERE Win_Pct >= 0.6
            LIMIT 10;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        print("Top Teams with Win % >= 0.6:")
        for row in results:
            print(row)

    except Exception as e:
        print("Error querying the database:", str(e))



def stage4_plot_data():
    print("\n Stage 4: Plotting data...")

    import matplotlib.pyplot as plt

    db_file = "mlb_data.db"
    if not os.path.exists(db_file):
        print(" Database file not found.")
        return

    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_sql_query("SELECT Year, AVG(Win_Pct) as Avg_WinPct FROM mlb_stats GROUP BY Year", conn)
        conn.close()

        df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
        df = df.dropna()

        plt.figure(figsize=(10, 6))
        plt.plot(df["Year"], df["Avg_WinPct"], marker='o')
        plt.title("Average Win % by Year")
        plt.xlabel("Year")
        plt.ylabel("Average Win Percentage")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(" Error generating plot:", str(e))


if __name__ == "__main__":
    stage1_scrape_data()
    stage2_import_to_sqlite()
    stage3_query_database()
    stage4_plot_data()
