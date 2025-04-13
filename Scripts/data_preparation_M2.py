import requests

def download_download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    file_id = sharing_link.split('/d/')[1].split('/')[0]
    download_url = f"https://leeds365-my.sharepoint.com/:f:/r/personal/mbhs1277_leeds_ac_uk/Documents/quiz_answers_named_a1_to_a25?csf=1&web=1&e=9jwFSK={file_id}"
    index = respondent_index
    file_name = f'a{index}.txt'
    response = requests.get(downloard_url)
    if response.status_code == 200:
        path_to_data_folder_path = f"{path_to_data_folder}/downloaded.file.txt"
        with open(path_to_data_folder_path, wb) as file:
            file.write(response.content)
        print (f"file downloaded successfully to {path_to_data_folder}")
    else:
        print ("Fail to download the file")
