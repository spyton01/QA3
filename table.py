# enable database feature (does not require server)
import sqlite3

# create empty database
connect = sqlite3.connect('QuestionsAnswer1.db')
cursor = connect.cursor()

# create table
cursor.execute('''CREATE TABLE IF NOT EXISTS OCM_Logistic
               (id integer, questions text, answers text)''')

# fill in table with values
cursor.execute('''
               INSERT INTO OCM_Logistic (id, questions, answers) VALUES
               (1, 'What is the primary objective of Operation Logistic OCM? \nA: Enhancing supply chain efficiency \nB: Implementing new technology solutions \nC: Streamlining operational processes', "A"),
               (2, 'Who is the key stakeholder responsible for driving change in Operation Logistic OCM? \nA: Project Manager \nB: Operations Director \nC: Change Management Team', "C"),
               (3, 'What is the name of the software platform used for managing logistics data in Operation Logistic OCM? \nA: Supply Chain Navigator \nB: Logistics Pro \nC: Operations Dashboard', "A"),
               (4, 'Which aspect of logistics is prioritized in Operation Logistic OCM? \nA: Inventory management \nB: Transportation planning C: Warehouse optimization', "C"),
               (5, 'What is the critical success factor for effective change implementation in Operation Logistic OCM? \nA: Employee training \nB: Executive sponsorship \nC: Stakeholder communication', "B"),
               (6, 'Which change management model is utilized in Operation Logistic OCM for guiding organizational transformation? \nA: ADKAR Model \nB: Kotters 8-Step Process \nC: Lewins Change Management Model', "B"),
               (7, 'What is the name of the risk assessment technique employed in Operation Logistic OCM to identify potential obstacles? \nA: SWOT Analysis \nB: PESTLE Analysis \nC: FMEA (Failure Mode and Effects Analysis)', "C"),
               (8, 'Which communication channel is preferred for disseminating updates and progress reports in Operation Logistic OCM? \nA: Email newsletters \nB: Town hall meetings \nC: Intranet portal', "C"),
               (9, 'What is the recommended approach for managing resistance to change in Operation Logistic OCM? \nA: Forceful persuasion \nB: Active listening and engagement \nC: Ignoring dissenting voices', "B"),
               (10, 'What is the key outcome expected from Operation Logistic OCM? \nA: Cost reduction \nB: Improved operational agility \nC: Increased customer satisfaction', "B")
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Modern_History
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Modern_History (id, questions, answers) VALUES
               (1, 'Which event marked the beginning of World War I? \nA: Assassination of Archduke Franz Ferdinand \nB: Treaty of Versailles \nC: Battle of Stalingrad', "A"),
               (2, 'Who was the leader of the Soviet Union during the Cuban Missile Crisis? \nA: Nikita Khrushchev \nB: Joseph Stalin \nC: Mikhail Gorbachev', "A"),
               (3, 'What was the name of the ship sunk during World War II that played a significant role in bringing the United States into the war? \nA: HMS Belfast \nB: RMS Lusitania \nC: USS Arizona', "B"),
               (4, 'Which treaty officially ended World War I? \nA: Treaty of Versailles \nB: Treaty of Trianon \nC: Treaty of Brest-Litovsk', "A"),
               (5, 'Who was the first woman to fly solo across the Atlantic Ocean? \nA: Amelia Earhart \nB: Bessie Coleman \nC: Harriet Quimby', "A"),
               (6, 'What was the name of the military operation that led to the invasion of Normandy during World War II? \nA: Operation Overlord \nB: Operation Barbarossa \nC: Operation Neptune', "A"),
               (7, 'Which event marked the beginning of the Cold War? \nA: Berlin Airlift \nB: Korean War \nC: Yalta Conference', "C"),
               (8, 'Who was the first leader of independent India? \nA: Jawaharlal Nehru \nB: Mahatma Gandhi \nC: Muhammad Ali Jinnah', "B"),
               (9, 'Which country was divided into North and South after World War II, leading to the Korean War? \nA: Vietnam \nB: Germany \nC: Korea', "C"),
               (10, 'What year did the Berlin Wall fall, symbolizing the end of the Cold War? \nA: 1989 \nB: 1991 \nC: 1987', "A")
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Finance
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Finance (id, questions, answers) VALUES
               (1, 'What is the primary function of a central bank in a country\`s economy? \nA: Regulating interest rates \nB: Issuing currency \nC: Conducting monetary policy', "C"),
               (2, 'Who is known as the "Oracle of Omaha" in the world of finance? \nA: Warren Buffett \nB: Bill Gates \nC: Elon Musk', "A"),
               (3, 'What is the term for the measure of the rate of return on an investment relative to its cost? \nA: Dividend yield \nB: Return on investment (ROI) C\n: Price-to-earnings (P/E) ratio', "B"),
               (4, 'Which financial instrument represents ownership in a corporation? \nA: Bond \nB: Stock \nC: Mutual fund', "B"),
               (5, 'What is the market where securities are bought and sold after their initial offering? \nA: Primary market \nB: Secondary market \nC: Derivatives market', "B"),
               (6, 'Which economic indicator measures the total value of goods and services produced within a country in a given period? \nA: GDP (Gross Domestic Product) \nB: CPI (Consumer Price Index) \nC: PPI (Producer Price Index)', "A"),
               (7, 'What is the term for a financial asset representing a promise to repay a loan with interest at a specified date in the future? \nA: Stock \nB: Bond \nC: Option', "B"),
               (8, 'Which type of risk refers to the possibility of loss due to changes in interest rates? \nA: Credit risk \nB: Market risk \nC: Interest rate risk', "C"),
               (9, 'What is the term for the practice of spreading investments among different assets to reduce risk? \nA: Diversification \nB: Leverage \nC: Arbitrage', "A"),
               (10, 'What financial ratio measures a company\`s ability to cover its short-term liabilities with its short-term assets? \nA: Current ratio \nB: Debt-to-equity ratio \nC: Return on equity (ROE)', "A")
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Business_Analytics
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Business_Analytics (id, questions, answers) VALUES
               (1, 'What statistical method is used to identify patterns and relationships in large datasets? \nA: Regression analysis \nB: Cluster analysis \nC: Time series analysis', "B"),
               (2, 'Which software tool is commonly used for data visualization and business intelligence? \nA: Tableau \nB: Python \nC: Excel', "A"),
               (3, 'What is the term for the process of transforming raw data into meaningful insights for business decision-making? \nA: Data mining \nB: Data wrangling \nC: Data analytics', "C"),
               (4, 'Which key performance indicator (KPI) measures a company\`s profitability relative to its revenue? \nA: Return on investment (ROI) \nB: Gross profit margin \nC: Net promoter score (NPS)', "B"),
               (5, 'What technique is used to forecast future values based on historical data? \nA: Regression analysis \nB: Time series analysis \nC: Monte Carlo simulation', "B"),
               (6, 'Which type of analysis is used to identify factors that drive customer behavior and preferences? \nA: Market basket analysis \nB: Cohort analysis \nC: Customer segmentation', "C"),
               (7, 'What is the term for the process of identifying and rectifying errors or inconsistencies in data? \nA: Data cleansing \nB: Data validation \nC: Data aggregation', "A"),
               (8, 'Which statistical measure represents the average value of a dataset? \nA: Median \nB: Mode \nC: Mean', "C"),
               (9, 'What is the term for a statistical model used to predict the probability of a binary outcome? \nA: Decision tree \nB: Logistic regression \nC: Naive Bayes classifier', "B"),
               (10, 'What technique is used to identify outliers or anomalies in a dataset? \nA: Descriptive analytics \nB: Predictive analytics \nC: Anomaly detection', "C")
               ''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Prog_Logic
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Prog_Logic (id, questions, answers) VALUES
               (1, 'What is the fundamental concept in programming that involves breaking down a problem into smaller, more manageable parts? \nA: Decomposition \nB: Abstraction \nC: Iteration', "A"),
               (2, 'Which data structure uses a last-in, first-out (LIFO) approach? \nA: Queue B: Stack \nC: Linked List', "B"),
               (3, 'What is the term for a sequence of instructions that is repeated until a certain condition is met? \nA: Loop \nB: Function \nC: Conditional statement', "A"),
               (4, 'Which programming paradigm emphasizes the use of functions and data immutability? \nA: Imperative programming \nB: Declarative programming \nC: Functional programming', "C"),
               (5, 'What is the term for a logical expression that evaluates to either true or false? \nA: Variable \nB: Boolean \nC: String', "B"),
               (6, 'Which sorting algorithm has a worst-case time complexity of O(n^2)? \nA: Quick sort \nB: Merge sort \nC: Bubble sort', "C"),
               (7, 'What is the term for a variable that is accessible only within the scope of a specific function? \nA: Global variable \nB: Local variable \nC: Static variable', "B"),
               (8, 'Which control structure allows a program to execute different sequences of instructions based on certain conditions? \nA: Loop \nB: Function \nC: Conditional statement', "C"),
               (9, 'What is the process of tracing through code to understand its behavior and identify errors? \nA: Debugging \nB: Testing \nC: Profiling', "A"),
               (10, 'Which logical operator returns true if at least one of its operands is true? \nA: AND \nB: OR \nC: NOT', "B")
               ''')

# sending data to .db file
connect.commit()

# stop command
connect.close()









