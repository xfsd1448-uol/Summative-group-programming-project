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

    # Ensure path ends with a slash

    if not data_folder_path.endswith('/'):

        data_folder_path += '/'

    # Manually list all 25 filenames (since files.txt is missing)

    filenames = [f"answers_respondent_{i}.txt" for i in range(1, 26)]

    # Open output file (will crash if Output/ doesn't exist)

    output_file = open("Output/collated_answers.txt", "w")

    # Process each file (will crash if any file is missing)

    for i in range(len(filenames)):

        filepath = data_folder_path + filenames[i]

        content = open(filepath, "r").read().strip()

        output_file.write(content)

        if i < len(filenames) - 1:

            output_file.write("\n*\n")

    output_file.close()

    print("Collated file created at Output/collated_answers.txt")
 
# Call the function (adjust path if needed)

collate_answer_files("Data/")
 
