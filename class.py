class Question:
    def __init__(self, id, question, options, answer):
        self.id = id
        self.question = question
        self.options = options
        self.answer = answer

class OCM_Logistic:
    def __init__(self):
        self.questions = []

    def add_question(self, id, question, options, answer):
        self.questions.append(Question(id, question, options, answer))

    def generate_sql_inserts(self):
        sql_statements = []
        for question in self.questions:
            options_with_answers = question.options.split('\n')
            options = options_with_answers[:-1]  # Remove last item (empty string)
            correct_answer = options_with_answers[-1].strip()
            
            # Escape single quotes by doubling them to prevent SQL injection
            question_text = question.question.replace("'", "''")
            options_text = question.options.replace("'", "''")
            
            sql = f"INSERT INTO OCM_Logistic (id, questions, answers) VALUES ({question.id}, "
            sql += f"'{question_text}', "
            sql += f"'{options_text}', "
            sql += f"'{correct_answer}')"
            sql_statements.append(sql)
        
        return sql_statements

# Instantiate OCM_Logistic class
ocm = OCM_Logistic()

# Add questions for OCM_Logistic
ocm.add_question(1, 'What is the primary objective of Operation Logistic OCM? \nA: Enhancing supply chain efficiency \nB: Implementing new technology solutions \nC: Streamlining operational processes', "A", "A")
ocm.add_question(2, 'Who is the key stakeholder responsible for driving change in Operation Logistic OCM? \nA: Project Manager \nB: Operations Director \nC: Change Management Team', "C", "C")
# Add more questions similarly...

# Generate SQL INSERT statements
insert_statements = ocm.generate_sql_inserts()

# Print generated SQL INSERT statements
for statement in insert_statements:
    print(statement)