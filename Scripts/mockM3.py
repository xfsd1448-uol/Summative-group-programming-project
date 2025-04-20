import data_extraction_M1 as M1
import numpy as np

def generate_means_sequence(collated_path):
    
    final_out = []
    
    for i in range(99, len(collated_path), 100):
        total = 0
        total += file_content[i]
    final_out.append(total)
    
    return final_out        
    
file_content = M1.extract_answers_sequence("Output/collated_answers.txt") 
print(generate_means_sequence(file_content))
 


def sum_every_100th(file_content, question_index):
    total = 0
    for i in range(question_index, len(file_content), 100):
        total += file_content[i]
    return total

#print(sum_every_100th(M1.extract_answers_sequence("Output/collated_answers.txt"), 1))
