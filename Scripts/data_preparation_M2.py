import requests

def download_answer_files(cloud_urls, path_to_data_folder, respondent_index):


    if 1 <= respondent_index <= len(cloud_urls):
        file_url = cloud_urls[respondent_index - 1]
        file_name = f'answers_respondent_{respondent_index}.txt'

        response = requests.get(file_url)
        if response.status_code == 200:
            save_path = f"{path_to_data_folder}/answers_respondent_{respondent_index}.txt"
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f" Downloaded and saved {file_name} to {path_to_data_folder}")
        else:
            print("Fail to download the file")
            print(f"Status code: {response.status_code}")
    else:
        print(f"Invalid respondent index: {respondent_index}")




def collate_answer_files(data_folder_path):
   

    filenames = [f"answers_respondent_{i}.txt" for i in range(1, 26)]

    

    output_file = open("Output/collated_answers.txt", "w")

    

    for i in range(len(filenames)):

        filepath = data_folder_path + "/" + filenames[i]

        with open(filepath, "r") as file:
            x = file.read().strip()

        output_file.write(x)

        if i < len(filenames) - 1:

            output_file.write("\n*\n")

    output_file.close()

    print("Collated file created at Output/collated_answers.txt")
 



 


 





 
