import requests

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    file_name = f'a{respondent_index}.txt'
    download_url = f"https://leeds365-my.sharepoint.com/:f:/r/personal/mbhs1277_leeds_ac_uk/Documents/quiz_answers_named_a1_to_a25?csf=1&web=1&e=9jwFSK={file_name}"
    
    response = requests.get(download_url)
    if response.status_code == 200:
        save_path = f"{path_to_data_folder}/answers_respondent_{respondent_index}.txt"
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded and saved {file_name} to {path_to_data_folder}")
    else:
        print ("Fail to download the file")

# Example usage
cloud_url = "https://leeds365-my.sharepoint.com/:f:/r/personal/mbhs1277_leeds_ac_uk/Documents/quiz_answers_named_a1_to_a25?csf=1&web=1&e=9jwFSK"

path_to_data_folder = "data"
respondent_index = 3

download_answer_files(cloud_url, path_to_data_folder, respondent_index)
