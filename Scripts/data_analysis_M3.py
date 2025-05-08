import data_extraction_M1 as M1
import matplotlib.pyplot as plt
 
def generate_means_sequence(collated_path):
 
    file_content = M1.extract_answers_sequence(collated_path)
 
    total_respondents = len(file_content) // 100  
 
    means = []
 
    for question_index in range(100):  
 
        total = 0
 
        for i in range(question_index, len(file_content), 100):
 
            total += file_content[i]
 
        mean = total / total_respondents
 
        means.append(mean)
 
    return means
 
print(generate_means_sequence("Output/collated_answers.txt"))

plt.figure(figsize=(12, 6))
plt.scatter(range(1, 101), means, color='blue', alpha=0.7)
plt.title('Mean Answer Values per Question')
plt.xlabel('Question Number')
plt.ylabel('Mean Answer Value (1-4)')
plt.xticks(range(0, 101, 10))
plt.yticks(range(1, 5))
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()