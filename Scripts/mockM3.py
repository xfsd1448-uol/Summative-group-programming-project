import data_extraction_M1 as M1
 
def generate_means_sequence(collated_path):

    # 提取所有回答（一个长 list）

    file_content = M1.extract_answers_sequence(collated_path)
 
    total_respondents = len(file_content) // 100  # 每人100题

    means = []
 
    for question_index in range(100):  # 对每一题

        total = 0

        for i in range(question_index, len(file_content), 100):

            total += file_content[i]

        mean = total / total_respondents

        means.append(mean)
 
    return means

print(generate_means_sequence("Output/collated_answers.txt"))
