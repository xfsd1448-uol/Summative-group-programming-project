import data_extraction_M1 as M1

import numpy as np
def generate_means_sequence(collated_path):
   
    #file = open("Output/collated_answers.txt",'r')
    #file_content = file.read()
    #file.close()
    file_content = M1.extract_answers_sequence("/workspaces/Summative-group-programming-project/Output/collated_answers.txt")           
    #respondents_data = file_content.split('*')

#import data_extraction_M1 as M1    
    #all_answers = []
    
    
    #for respondent in file_content:
        
        #if respondent.strip() == "":
            #continue
            
    #text = [file_content]
    answers = []
    
        #answers = ast.literal_eval(respondent.strip())
        #for line in file_content.split('\n'):
            #answers = ast.literal_eval(file_content.strip())
            #if line.strip() != "":
                # This simplifies the processing and actually requires parsing according to the file format
                #answers.append(float(line.strip()))  # Suppose each row is a number
        
        # Make sure there are 100 answers (less than 0)
    #while len(text) < 100:
            #text.append(0)
            #answers = file_content[:100]  # Just take the first 100
        
    #all_answers.append(answers)
    file = [file_content]

    #file_content = list(range(1, 2500))
    group_size = 100

    # 转换为 NumPy 数组并分割
    array = np.array(file)
    grouped_arrays = np.array_split(array, 25)

    # 转换回列表（可选）
    grouped_list = [arr.tolist() for arr in grouped_arrays]

    print(grouped_list)