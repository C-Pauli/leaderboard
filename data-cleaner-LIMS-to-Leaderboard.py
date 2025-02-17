import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function to clean the data
def clean_data(df):
    # Define the columns to extract
    columns_to_extract = [
        'Sample_Name', 'Sample_LabCode', 'Sample_SampleType', 'Sample_BatchCode',
        'Alkaloid_1_4AcetoxyDMT_AmountMgG', 'Alkaloid_1_4AcetoxyMET_AmountMgG', 
        'Alkaloid_1_4HydroxyDET_AmountMgG', 'Alkaloid_1_4HydroxyTMT_AmountMgG',
        'Alkaloid_1_4Hydroxytryptamine_AmountMgG', 'Alkaloid_1_4PropanoyloxyDMT_AmountMgG',
        'Alkaloid_1_5Hydroxytryptophan_AmountMgG', 'Alkaloid_1_5MethoxyDMT_AmountMgG',
        'Alkaloid_1_5MethoxyNMT_AmountMgG', 'Alkaloid_1_Adenosine_AmountMgG',
        'Alkaloid_1_Aeruginascin_AmountMgG', 'Alkaloid_1_Baeocystin_AmountMgG',
        'Alkaloid_1_Bufotenin_AmountMgG', 'Alkaloid_1_Methylcybin_AmountMgG',
        'Alkaloid_1_N,NDMT_AmountMgG', 'Alkaloid_1_NNMT_AmountMgG', 
        'Alkaloid_1_Norbaeocystin_AmountMgG', 'Alkaloid_1_Norpsilocin_AmountMgG', 
        'Alkaloid_1_PsilocinEquivalent_AmountMgG', 'Alkaloid_1_Psilocin_AmountMgG', 
        'Alkaloid_1_Psilocybin_AmountMgG', 'Alkaloid_1_Serotonin_AmountMgG',
        'Alkaloid_1_Tryptamine_AmountMgG', 'Alkaloid_1_Tryptophan_AmountMgG',
        'Alkaloid_1_4AcetoxyDMT_AmountMgPkg', 'Alkaloid_1_4AcetoxyMET_AmountMgPkg',
        'Alkaloid_1_4HydroxyDET_AmountMgPkg', 'Alkaloid_1_4HydroxyTMT_AmountMgPkg',
        'Alkaloid_1_4Hydroxytryptamine_AmountMgPkg', 'Alkaloid_1_4PropanoyloxyDMT_AmountMgPkg',
        'Alkaloid_1_5Hydroxytryptophan_AmountMgPkg', 'Alkaloid_1_5MethoxyDMT_AmountMgPkg',
        'Alkaloid_1_5MethoxyNMT_AmountMgPkg', 'Alkaloid_1_Adenosine_AmountMgPkg',
        'Alkaloid_1_Aeruginascin_AmountMgPkg', 'Alkaloid_1_Baeocystin_AmountMgPkg',
        'Alkaloid_1_Bufotenin_AmountMgPkg', 'Alkaloid_1_Methylcybin_AmountMgPkg',
        'Alkaloid_1_N,NDMT_AmountMgPkg', 'Alkaloid_1_NNMT_AmountMgPkg',
        'Alkaloid_1_Norbaeocystin_AmountMgPkg', 'Alkaloid_1_Norpsilocin_AmountMgPkg',
        'Alkaloid_1_PsilocinEquivalent_AmountMgPkg', 'Alkaloid_1_Psilocin_AmountMgPkg',
        'Alkaloid_1_Psilocybin_AmountMgPkg', 'Alkaloid_1_Serotonin_AmountMgPkg',
        'Alkaloid_1_Tryptamine_AmountMgPkg', 'Alkaloid_1_Tryptophan_AmountMgPkg',
        'Alkaloid_1_4AcetoxyDMT_AmountMgSrv', 'Alkaloid_1_4AcetoxyMET_AmountMgSrv',
        'Alkaloid_1_4HydroxyDET_AmountMgSrv', 'Alkaloid_1_4HydroxyTMT_AmountMgSrv',
        'Alkaloid_1_4Hydroxytryptamine_AmountMgSrv', 'Alkaloid_1_4PropanoyloxyDMT_AmountMgSrv',
        'Alkaloid_1_5Hydroxytryptophan_AmountMgSrv', 'Alkaloid_1_5MethoxyDMT_AmountMgSrv',
        'Alkaloid_1_5MethoxyNMT_AmountMgSrv', 'Alkaloid_1_Adenosine_AmountMgSrv',
        'Alkaloid_1_Aeruginascin_AmountMgSrv', 'Alkaloid_1_Baeocystin_AmountMgSrv',
        'Alkaloid_1_Bufotenin_AmountMgSrv', 'Alkaloid_1_Methylcybin_AmountMgSrv',
        'Alkaloid_1_N,NDMT_AmountMgSrv', 'Alkaloid_1_NNMT_AmountMgSrv', 
        'Alkaloid_1_Norbaeocystin_AmountMgSrv', 'Alkaloid_1_Norpsilocin_AmountMgSrv',
        'Alkaloid_1_PsilocinEquivalent_AmountMgSrv', 'Alkaloid_1_Psilocin_AmountMgSrv',
        'Alkaloid_1_Psilocybin_AmountMgSrv', 'Alkaloid_1_Serotonin_AmountMgSrv',
        'Alkaloid_1_Tryptamine_AmountMgSrv', 'Alkaloid_1_Tryptophan_AmountMgSrv'
    ]
    
    # Extract the selected columns
    extracted_df = df[columns_to_extract]

    # Replace " mg/srv", " mg/pkg", " mg/g" with nothing
    extracted_df = extracted_df.replace({
        " mg/srv": "", 
        " mg/pkg": "", 
        " mg/g": ""
    }, regex=True)

    # Replace "Alkaloid_1_" with nothing and "_Amount_" with " "
    extracted_df.columns = extracted_df.columns.str.replace("Alkaloid_1_", "", regex=True)
    extracted_df.columns = extracted_df.columns.str.replace("_Amount_", " ", regex=True)

    # Convert only columns containing 'MgG', 'MgPkg', or 'MgSrv' to numeric
    columns_to_convert = [col for col in extracted_df.columns if any(x in col for x in ['MgG', 'MgPkg', 'MgSrv'])]
    
    for column in columns_to_convert:
        extracted_df[column] = pd.to_numeric(extracted_df[column], errors='coerce')

    # Remove columns where all values are 0
    extracted_df = extracted_df.loc[:, (extracted_df != 0).any(axis=0)]
    
    return extracted_df

# Function to upload and clean the file
def upload_and_clean():
    file_path = filedialog.askopenfilename(
        initialdir="/mnt/c/Users/User/Downloads", 
        title="Select a CSV File", 
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        try:
            df = pd.read_csv(file_path)
            cleaned_df = clean_data(df)
            messagebox.showinfo("Success", "Data cleaned successfully!")
            save_cleaned_file(cleaned_df)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to save the cleaned file
def save_cleaned_file(cleaned_df):
    save_path = filedialog.asksaveasfilename(
        initialdir="/mnt/c/Users/User/Downloads", 
        defaultextension=".csv", 
        filetypes=[("CSV files", "*.csv")]
    )
    if save_path:
        try:
            cleaned_df.to_csv(save_path, index=False)
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving: {str(e)}")

# Setting up the GUI
root = tk.Tk()
root.title("Data Cleaner")

# Create the Upload and Clean Button
upload_button = tk.Button(root, text="Upload and Clean File", command=upload_and_clean)
upload_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
