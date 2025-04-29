import data_extraction_M1 as M1
import ast
def generate_means_sequence(collated_path):
   
    file = open("Output/collated_answers.txt",'r')
    file_content = file.read()
    file.close()
    
    
    #respondents_data = file_content.split('*')

    
    #all_answers = []
    
    
    #for respondent in file_content:
        
        #if respondent.strip() == "":
            #continue
            
    text = [file_content]
    answers = []
    
        #answers = ast.literal_eval(respondent.strip())
        #for line in file_content.split('\n'):
            #answers = ast.literal_eval(file_content.strip())
            #if line.strip() != "":
                # This simplifies the processing and actually requires parsing according to the file format
                #answers.append(float(line.strip()))  # Suppose each row is a number
        
        # Make sure there are 100 answers (less than 0)
    while len(text) < 100:
            text.append(0)
            answers = file_content[:100]  # Just take the first 100
        
    #all_answers.append(answers)
    
    
    means = []
    
    for question_num in range(100):  
        total = 0
        #count = 0
        
        # Collect all respondents' responses to this question
        for respondent_answers in answers:
            answer = respondent_answers[question_num]
            total += answer
            #count += 1
    count = len(answers)    
        # Calculate the average
    if count > 0:
        average = total / count
    else:
        average = 0.0
            
        means.append(average)
    
    return means

generate_means_sequence("Output/collated_answers.txt")
