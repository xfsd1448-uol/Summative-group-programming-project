import data_extraction_M1 as M1
import data_preparation_M2 as M2
import data_analysis_M3 as M3

def run_full_analysis(cloud_url, data_folder, output_folder, n=1):
    """
    Executes the full analysis pipeline:
    1. Downloads and collates response data.
    2. Extracts structured answer sequences.
    3. Analyzes and visualizes the data.

    Parameters:
    cloud_url (str): URL to download response data.
    data_folder (str): Directory to store raw response files.
    output_folder (str): Directory to store processed outputs.
    n (int): Visualization type (1 = scatter plot, 2 = line plot).
    """
    print("\nStep 1: Downloading and collating responses...")
    M2.download_answer_files(cloud_url, data_folder, respondent_index=40)  # Adjust respondent count
    M2.collate_answer_files(data_folder)

    collated_file = f"{output_folder}/collated_answers.txt"

    print("\nStep 2: Extracting structured answer sequences...")
    for i in range(1, 41):  # Assuming 40 respondents
        input_file = f"{data_folder}/answers_respondent_{i}.txt"
        answers = M1.extract_answers_sequence(input_file)
        M1.write_answers_sequence(answers, i)

    print("\nStep 3: Analyzing and visualizing data...")
    means_sequence = M3.generate_means_sequence(collated_file)
    M3.visualize_data(collated_file, n)

    print("\nPipeline execution complete! Results saved in:", output_folder)
