import requests

def download_answer_files(cloud_urls, path_to_data_folder, respondent_index):


    if 1 <= respondent_index <= len(cloud_urls):
        file_url = cloud_urls[respondent_index - 1]
        file_name = f'a{respondent_index}.txt'

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

cloud_urls= [
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/Edp4Leus4bhInnTwC61pAGABl7kYZ46ooAW39kkvdGgMoQ?e=ecyH52&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EQfilZ0BXNVPvx99hbEIm6YBUAymqr5szFQ5fAHRjualDw?e=TqXtEM&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/ETyN9xDQFLdAtndNs80-U20BH_QTPc4EgPt0SQAhcnTD7Q?e=nXbHFn&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EbHSu2RTX9dPiymdtvyr4rgBzTs2uZsJf5Juz--tFleBSw?e=xrTtSK&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EXKBUfseNtlGo2j4CYNmQwsBOFz3JIMda-IZlDi7KqsnAQ?e=Az4sEJ&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/ES6mqA3ggytNr5CzwTG_0GcB3oSxL4KtgoIGr3INmxXDfQ?e=T8FjWB&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/ETz6soThU_dAtrHyuW2BQm8BkynCfFppRcvLALxVfbcp2w?e=sVMFsM&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EX4qZhhAqQ1ErybuD4gORRgB4mir_hwXrzkWK1IBxUDkww?e=qU4dOt&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EaItX88bKRtNho9_tLBOko4BiQuEMJukOTwqQLX7Wwj0QQ?e=vLbVrW&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EWBsptEnoRFNnbaJ1evPxMkBBAKfXzyPOHk0_A07-kk5FQ?e=1bKdui&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EdrY1wlxrGxEiaW2vctDj0oB-PSjMz0NsCnE3LUYozPTpA?e=fxloPJ&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EUAvgSyPvXFCijmjKMz5S0wB-vsabPiydLe6LGspxqynsw?e=hhrF3F&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/Eao4E6xpQBtIl5ZHFGaBoxgBd_2z8g919_EYPuRL2s_DNA?e=kOzKac&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EWTFBGLZdsRAlDmDTBLSzPQBa6DcR6YB3l41LkmEOJtVLA?e=BXcgnb&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EYz0ZnWS1qtLq04qmGQfmHQBdkTTfbDP-RjKPM25Vb18CQ?e=cAFdBP&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EWQRWwZ8ocZGs_a3eMG6fDYBG86IGqg7-rOfq9Tm0f93yg?e=GTwfNN&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EU5jqGOxHZ1HscYQYNTpaVIBo2bT2tY1n9oPfqr-egORLw?e=khJaWE&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/Ec5nKZ9HhH9Nks9nTG3JGi0B1PsrVPY5hyWcMl5_IotyNQ?e=ZZEGTX&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EQI3gdYuJspGstL2pz-vWikBMJKuvcvvEHAFoFYNxLZvhw?e=aMuZ19&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EZSjnmbms5tEubV67qdRM3kBeqi0jLOwbyXe7W4e0mRv9g?e=C1B6FJ&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EaxJzBbUGdRMpIMRjtWN4fMBOcByee07UTNYATKQFAl_3g?e=lJD9g2&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EQ1TbbnDf_FCjRrIj1keFg4B-1Y--sMIwSa_iF16fCIEbA?e=Y0p98J&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EXWEkv4VJaVEppOcR79CDB0BSS8rsXW0C31LoiOmxjJwIg?e=g4kMJx&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/EUgyOR_vxuBNkDtID7hN-UUBmrAgZwy3Jn3467emksv1YA?e=4iNXSe&download=1",
        "https://leeds365-my.sharepoint.com/:t:/g/personal/mbhs1277_leeds_ac_uk/Eb597gekkztPisYO0EMAyDYBmQHvS1iLfX4RJ6x1zoUyQA?e=gnED6s&download=1"

        
    ]
download_answer_files(cloud_urls, "data", 2)

def collate_answer_files(data_folder_path):
    # Manually construct the list of filenames in the folder
    # (requires that data_folder_path ends with a slash and only contains files)
    filenames = sorted(open("files.txt").read().splitlines())  # See note below

    output_file = open("output/collated_answers.txt", "w")

    for i in range(len(filenames)):
        filepath = data_folder_path + filenames[i]
        infile = open(filepath, "r")
        content = infile.read().strip()
        infile.close()
        output_file.write(content)
        if i < len(filenames) - 1:
            output_file.write("\n*\n")

    output_file.close()
    print("Collated file created at output/collated_answers.txt")




