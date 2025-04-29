import data_extraction_M1 as M1
import data_preparation_M2 as M2
import mockM3 as M3

def full_analysis(cloud_url, data_folder, output_folder, n=1):
 
    M2.download_answer_files(cloud_url, data_folder, respondent_index=25)  
    M2.collate_answer_files(data_folder)

    collated_file = f"{output_folder}/collated_answers.txt"

   
    for i in range(1, 26):  
        input_file = f"{data_folder}/answers_respondent_{i}.txt"
        answers = M1.extract_answers_sequence(input_file)

    
    means_sequence = M3.generate_means_sequence(collated_file)
    M3.visualize_data(collated_file, n)

    