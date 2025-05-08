import data_extraction_M1 as M1
import matplotlib.pyplot as plt
 
file_content = M1.extract_answers_sequence("Output/collated_answers.txt")

def generate_means_sequence(collated_path):
  
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
plt.scatter(range(1, 101), generate_means_sequence("Output/collated_answers.txt"), color='blue', alpha=0.7)
plt.title('Mean Answer Values per Question')
plt.xlabel('Question Number')
plt.ylabel('Mean Answer Value (1-4)')
plt.xticks(range(0, 101, 10))
plt.yticks(range(1, 5))
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


# Plot all respondents' answer sequences
plt.figure(figsize=(12, 6))
for i, seq in enumerate(file_content):  # 遍历每个回答者的序列
    plt.plot(range(1, 101), seq,         # x轴:1-100题，y轴:答案值
            alpha=0.3,                  # 设置透明度
            linewidth=1)                # 线宽
    
plt.title('All Respondents\' Answer Sequences')
plt.xlabel('Question Number')
plt.ylabel('Answer Value (0=unanswered, 1-4=options)')
plt.xticks(range(0, 101, 10))          # x轴刻度每10题一个
plt.yticks(range(0, 5))                # y轴刻度0-4
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()