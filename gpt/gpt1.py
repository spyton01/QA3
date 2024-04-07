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
               (1, 'What is the primary objective of Operation Logistic OCM? A: Enhancing supply chain efficiency B: Implementing new technology solutions C: Streamlining operational processes', "A"),
               (2, 'Who is the key stakeholder responsible for driving change in Operation Logistic OCM? A: Project Manager B: Operations Director C: Change Management Team', "C"),
               (3, 'What is the name of the software platform used for managing logistics data in Operation Logistic OCM? A: Supply Chain Navigator B: Logistics Pro C: Operations Dashboard', "A"),
               (4, 'Which aspect of logistics is prioritized in Operation Logistic OCM? A: Inventory management B: Transportation planning C: Warehouse optimization', "C"),
               (5, 'What is the critical success factor for effective change implementation in Operation Logistic OCM? A: Employee training B: Executive sponsorship C: Stakeholder communication', "B"),
               (6, 'Which change management model is utilized in Operation Logistic OCM for guiding organizational transformation? A: ADKAR Model B: Kotters 8-Step Process C: Lewins Change Management Model', "B"),
               (7, 'What is the name of the risk assessment technique employed in Operation Logistic OCM to identify potential obstacles? A: SWOT Analysis B: PESTLE Analysis C: FMEA (Failure Mode and Effects Analysis)', "C"),
               (8, 'Which communication channel is preferred for disseminating updates and progress reports in Operation Logistic OCM? A: Email newsletters B: Town hall meetings C: Intranet portal', "C"),
               (9, 'What is the recommended approach for managing resistance to change in Operation Logistic OCM? A: Forceful persuasion B: Active listening and engagement C: Ignoring dissenting voices', "B"),
               (10, 'What is the key outcome expected from Operation Logistic OCM? A: Cost reduction B: Improved operational agility C: Increased customer satisfaction', "B")
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Modern_History
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Modern_History (id, questions, answers) VALUES
               (1, 'Which event marked the beginning of World War I? A: Assassination of Archduke Franz Ferdinand B: Treaty of Versailles C: Battle of Stalingrad', "A"),
               (2, 'Who was the leader of the Soviet Union during the Cuban Missile Crisis? A: Nikita Khrushchev B: Joseph Stalin C: Mikhail Gorbachev', "A"),
               (3, 'What was the name of the ship sunk during World War II that played a significant role in bringing the United States into the war? A: HMS Belfast B: RMS Lusitania C: USS Arizona', "B"),
               (4, 'Which treaty officially ended World War I? A: Treaty of Versailles B: Treaty of Trianon C: Treaty of Brest-Litovsk', "A"),
               (5, 'Who was the first woman to fly solo across the Atlantic Ocean? A: Amelia Earhart B: Bessie Coleman C: Harriet Quimby', "A"),
               (6, 'What was the name of the military operation that led to the invasion of Normandy during World War II? A: Operation Overlord B: Operation Barbarossa C: Operation Neptune', "A"),
               (7, 'Which event marked the beginning of the Cold War? A: Berlin Airlift B: Korean War C: Yalta Conference', "C"),
               (8, 'Who was the first leader of independent India? A: Jawaharlal Nehru B: Mahatma Gandhi C: Muhammad Ali Jinnah', "B"),
               (9, 'Which country was divided into North and South after World War II, leading to the Korean War? A: Vietnam B: Germany C: Korea', "C"),
               (10, 'What year did the Berlin Wall fall, symbolizing the end of the Cold War? A: 1989 B: 1991 C: 1987', "A")
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Finance
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Finance (id, questions, answers) VALUES
               (1, 'What is the primary function of a central bank in a country\`s economy? A: Regulating interest rates B: Issuing currency C: Conducting monetary policy', "C"),
               (2, 'Who is known as the "Oracle of Omaha" in the world of finance? A: Warren Buffett B: Bill Gates C: Elon Musk', "A"),
               (3, 'What is the term for the measure of the rate of return on an investment relative to its cost? A: Dividend yield B: Return on investment (ROI) C: Price-to-earnings (P/E) ratio', "B"),
               (4, 'Which financial instrument represents ownership in a corporation? A: Bond B: Stock C: Mutual fund', "B"),
               (5, 'What is the market where securities are bought and sold after their initial offering? A: Primary market B: Secondary market C: Derivatives market', "B"),
               (6, 'Which economic indicator measures the total value of goods and services produced within a country in a given period? A: GDP (Gross Domestic Product) B: CPI (Consumer Price Index) C: PPI (Producer Price Index)', "A"),
               (7, 'What is the term for a financial asset representing a promise to repay a loan with interest at a specified date in the future? A: Stock B: Bond C: Option', "B"),
               (8, 'Which type of risk refers to the possibility of loss due to changes in interest rates? A: Credit risk B: Market risk C: Interest rate risk', "C"),
               (9, 'What is the term for the practice of spreading investments among different assets to reduce risk? A: Diversification B: Leverage C: Arbitrage', "A"),
               (10, 'What financial ratio measures a company\`s ability to cover its short-term liabilities with its short-term assets? A: Current ratio B: Debt-to-equity ratio C: Return on equity (ROE)', "A")
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Business_Analytics
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Business_Analytics (id, questions, answers) VALUES
               (1, 'What statistical method is used to identify patterns and relationships in large datasets? A: Regression analysis B: Cluster analysis C: Time series analysis', "B"),
               (2, 'Which software tool is commonly used for data visualization and business intelligence? A: Tableau B: Python C: Excel', "A"),
               (3, 'What is the term for the process of transforming raw data into meaningful insights for business decision-making? A: Data mining B: Data wrangling C: Data analytics', "C"),
               (4, 'Which key performance indicator (KPI) measures a company\`s profitability relative to its revenue? A: Return on investment (ROI) B: Gross profit margin C: Net promoter score (NPS)', "B"),
               (5, 'What technique is used to forecast future values based on historical data? A: Regression analysis B: Time series analysis C: Monte Carlo simulation', "B"),
               (6, 'Which type of analysis is used to identify factors that drive customer behavior and preferences? A: Market basket analysis B: Cohort analysis C: Customer segmentation', "C"),
               (7, 'What is the term for the process of identifying and rectifying errors or inconsistencies in data? A: Data cleansing B: Data validation C: Data aggregation', "A"),
               (8, 'Which statistical measure represents the average value of a dataset? A: Median B: Mode C: Mean', "C"),
               (9, 'What is the term for a statistical model used to predict the probability of a binary outcome? A: Decision tree B: Logistic regression C: Naive Bayes classifier', "B"),
               (10, 'What technique is used to identify outliers or anomalies in a dataset? A: Descriptive analytics B: Predictive analytics C: Anomaly detection', "C")
               ''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Prog_Logic
               (id integer, questions text, answers text)''')

cursor.execute('''
               INSERT INTO Prog_Logic (id, questions, answers) VALUES
               (1, 'What is the fundamental concept in programming that involves breaking down a problem into smaller, more manageable parts? A: Decomposition B: Abstraction C: Iteration', "A"),
               (2, 'Which data structure uses a last-in, first-out (LIFO) approach? A: Queue B: Stack C: Linked List', "B"),
               (3, 'What is the term for a sequence of instructions that is repeated until a certain condition is met? A: Loop B: Function C: Conditional statement', "A"),
               (4, 'Which programming paradigm emphasizes the use of functions and data immutability? A: Imperative programming B: Declarative programming C: Functional programming', "C"),
               (5, 'What is the term for a logical expression that evaluates to either true or false? A: Variable B: Boolean C: String', "B"),
               (6, 'Which sorting algorithm has a worst-case time complexity of O(n^2)? A: Quick sort B: Merge sort C: Bubble sort', "C"),
               (7, 'What is the term for a variable that is accessible only within the scope of a specific function? A: Global variable B: Local variable C: Static variable', "B"),
               (8, 'Which control structure allows a program to execute different sequences of instructions based on certain conditions? A: Loop B: Function C: Conditional statement', "C"),
               (9, 'What is the process of tracing through code to understand its behavior and identify errors? A: Debugging B: Testing C: Profiling', "A"),
               (10, 'Which logical operator returns true if at least one of its operands is true? A: AND B: OR C: NOT', "B")
               ''')

# sending data to .db file
connect.commit()

# stop command
connect.close()