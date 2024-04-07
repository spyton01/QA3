from dataclasses import dataclass
from typing import List

# Define data classes for quiz data
@dataclass
class Question:
    text: str
    choices: List[str]
    answer: str

@dataclass
class Topic:
    name: str
    questions: List[Question]

@dataclass
class Quiz:
    topics: List[Topic]

# Function to initialize quiz topics with questions and choices
def initialize_quiz() -> Quiz:
    topics = []

    # Topic: OCM_Logistic
    ocm_logistic_questions = [
        Question(
            'What is the primary objective of Operation Logistic OCM?',
            ['Enhancing supply chain efficiency', 'Implementing new technology solutions', 'Streamlining operational processes'],
            'Enhancing supply chain efficiency'
        ),
        # Add more questions for OCM_Logistic...
    ]
    topics.append(Topic('OCM_Logistic', ocm_logistic_questions))

    # Topic: Modern_History
    modern_history_questions = [
        Question(
            'Which event marked the beginning of World War I?',
            ['Assassination of Archduke Franz Ferdinand', 'Treaty of Versailles', 'Battle of Stalingrad'],
            'Assassination of Archduke Franz Ferdinand'
        ),
        # Add more questions for Modern_History...
    ]
    topics.append(Topic('Modern_History', modern_history_questions))

    # Add more topics with their respective questions...

    # Topic: Topic_3
    topic_3_questions = [
        Question(
            'Question Text 1?',
            ['Choice A', 'Choice B', 'Choice C'],
            'Correct Answer'
        ),
        # Add more questions for Topic_3...
    ]
    topics.append(Topic('Topic_3', topic_3_questions))

    # Topic: Topic_4
    topic_4_questions = [
        Question(
            'Question Text 1?',
            ['Choice A', 'Choice B', 'Choice C'],
            'Correct Answer'
        ),
        # Add more questions for Topic_4...
    ]
    topics.append(Topic('Topic_4', topic_4_questions))

    # Topic: Topic_5
    topic_5_questions = [
        Question(
            'Question Text 1?',
            ['Choice A', 'Choice B', 'Choice C'],
            'Correct Answer'
        ),
        # Add more questions for Topic_5...
    ]
    topics.append(Topic('Topic_5', topic_5_questions))

    return Quiz(topics)

# Example usage:
my_quiz = initialize_quiz()

# Accessing quiz topics and questions
for topic in my_quiz.topics:
    print(f"Topic: {topic.name}")
    for idx, question in enumerate(topic.questions, start=1):
        print(f"Question {idx}: {question.text}")
        for choice in question.choices:
            print(choice)
        print(f"Correct Answer: {question.answer}")
    print()