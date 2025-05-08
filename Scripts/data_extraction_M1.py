def extract_answers_sequence(filepath):
    j = 0 
    answers = []
    f = open(filepath, 'r')
    rows = [row.strip() for row in f.readlines()]
    while j < len(rows):
        lines = rows[j]
        if lines.startswith("Question"):
            choosen_answer = 0 
            for k in range(4):
                answer_lines = rows[j + 1 + k] 
                if "[x]" in answer_lines:
                    choosen_answer = k + 1
            answers.append(choosen_answer)
            j += 5        
        else:
            j += 1
    return answers


def write_answers_sequence(answers, n):
    file_name = f"answers_list_respondent_{n}.txt"
    x = open(file_name, "w")
    for digit in answers:
        x.write(f"{digit}\n")
    x.close()    
