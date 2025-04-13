def generate_means_sequence(collated_path):
   
    file = open(collated_path, 'r')
    file_content = file.read()
    file.close()
    
    
    respondents_data = file_content.split('*')

    
    all_answers = []
    
    
    for respondent in respondents_data:
        
        if respondent.strip() == "":
            continue
            
        
        answers = []
        for line in respondent.split('\n'):
            if line.strip() != "":
                # This simplifies the processing and actually requires parsing according to the file format
                answers.append(float(line.strip()))  # Suppose each row is a number
        
        # Make sure there are 100 answers (less than 0)
        while len(answers) < 100:
            answers.append(0)
        answers = answers[:100]  # Just take the first 100
        
        all_answers.append(answers)
    
    
    means = []
    
    for question_num in range(100):  
        total = 0
        count = 0
        
        # Collect all respondents' responses to this question
        for respondent_answers in all_answers:
            answer = respondent_answers[question_num]
            if answer != 0:  # Ignore zero
                total += answer
                count += 1
        
        # Calculate the average
        if count > 0:
            average = total / count
        else:
            average = 0.0
            
        means.append(average)
    
    return means