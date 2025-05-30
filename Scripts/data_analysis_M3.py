import data_extraction_M1 as M1
import matplotlib.pyplot as plt
 

def generate_means_sequence(collated_path):
    file_content = M1.extract_answers_sequence("Output/collated_answers.txt")
  
    total_respondents = len(file_content) // 100  
 
    means = []
 
    for question_index in range(100):  
 
        total = 0
 
        for i in range(question_index, len(file_content), 100):
 
            total += file_content[i]
 
        mean = total / total_respondents
 
        means.append(mean)
 
    return means
 


def visualize_data(collated_answers_path, n):
    file_content = M1.extract_answers_sequence("Output/collated_answers.txt")

    respondents = [file_content[i:i+100] for i in range(0, len(file_content), 100)]

    if n == 1:
        plt.figure(figsize=(12, 6))
        plt.scatter(range(1, 101), generate_means_sequence(collated_answers_path), color='blue', alpha=0.7)
        plt.title('Mean Answer Values per Question')
        plt.xlabel('Question Number')
        plt.ylabel('Mean Answer Value (1-4)')
        plt.xticks(range(0, 101, 10))
        plt.yticks(range(0, 5))
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    if n == 2:
        # Plot all respondents' answer sequences
        plt.figure(figsize=(12, 6))
        for i, seq in enumerate(respondents): 
            plt.plot(range(1, 101), seq, alpha=0.3,linewidth=1)               
        plt.title('All Respondents\' Answer line Graphs')
        plt.xlabel('Question Number')
        plt.ylabel('Answer Value (0=unanswered, 1-4=options)')
        plt.xticks(range(0, 101, 10))         
        plt.yticks(range(0, 5))              
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    if n not in [1, 2]:
        print("Invalid value for n. Use 1 (scatter) or 2 (line).")
