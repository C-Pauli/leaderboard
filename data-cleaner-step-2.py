import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the full column mapping including the new keys
column_mapping = {
    'Sample_Name': 'Sample Name',
    'Sample_LabCode': 'Sample ID',  # Updated
    'Sample_SampleType': 'Sample Type',  # Updated
    'Sample_BatchCode': 'Grower ID',  # Updated
    'Sample_ClientName': 'Client Name',  # Updated
    'Norbaeocystin_AmountMgG': 'Norbaeocystin (mg/g)',
    'Psilocin_AmountMgG': 'Psilocin (mg/g)',
    'Psilocybin_AmountMgG': 'Psilocybin (mg/g)',
    'PsilocinEquivalent_AmountMgG': 'PsilocinEQ (mg/g)',
    'Baeocystin_AmountMgG': 'Baeocystin (mg/g)',
    'Bufotenin_AmountMgG': 'Bufotenin (mg/g)',
    'Methylcybin_AmountMgG': 'Methylcybin (mg/g)',
    'N,NDMT_AmountMgG': 'N,N-DMT (mg/g)',
    'NNMT_AmountMgG': 'N,N-MT (mg/g)',
    '4AcetoxyDMT_AmountMgG': '4-Acetoxy DMT (mg/g)',
    '5MethoxyDMT_AmountMgG': '5-Methoxy DMT (mg/g)',
    'Adenosine_AmountMgG': 'Adenosine (mg/g)',
    'Aeruginascin_AmountMgG': 'Aeruginascin (mg/g)',
    '4HydroxyTMT_AmountMgG': '4-Hydroxy TMT (mg/g)',
    '5Hydroxytryptophan_AmountMgG': '5-Hydroxytryptophan (mg/g)',
    'Serotonin_AmountMgG': 'Serotonin (mg/g)',
    'Tryptamine_AmountMgG': 'Tryptamine (mg/g)',
    'Tryptophan_AmountMgG': 'Tryptophan (mg/g)',
    '4AcetoxyMET_AmountMgG': '4-Acetoxy MET (mg/g)',
    '4HydroxyDET_AmountMgG': '4-Hydroxy DET (mg/g)',
    '4Hydroxytryptamine_AmountMgG': '4-Hydroxytryptamine (mg/g)',
    '4PropanoyloxyDMT_AmountMgG': '4-Propanoyloxy DMT (mg/g)',
    '5MethoxyNMT_AmountMgG': '5-Methoxy NMT (mg/g)',
    'Norpsilocin_AmountMgG': 'Norpsilocin (mg/g)',
    # Map for Package columns
    'Norbaeocystin_AmountMgPkg': 'Norbaeocystin (mg/pkg)',
    'Psilocin_AmountMgPkg': 'Psilocin (mg/pkg)',
    'Psilocybin_AmountMgPkg': 'Psilocybin (mg/pkg)',
    'PsilocinEquivalent_AmountMgPkg': 'PsilocinEQ (mg/pkg)',
    # Map for Serving columns
    'Norbaeocystin_AmountMgSrv': 'Norbaeocystin (mg/srv)',
    'Psilocin_AmountMgSrv': 'Psilocin (mg/srv)',
    'Psilocybin_AmountMgSrv': 'Psilocybin (mg/srv)',
    'PsilocinEquivalent_AmountMgSrv': 'PsilocinEQ (mg/srv)',
}

# Function to load and rename columns
def load_and_rename():
    # Prompt the user to select a CSV file
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=[("CSV files", "*.csv")]
    )
    
    if file_path:
        try:
            # Load the CSV file into a pandas dataframe
            df = pd.read_csv(file_path)
            
            # Apply the column mapping
            df_renamed = df.rename(columns=column_mapping)
            
            # Save the renamed dataframe
            save_file(df_renamed)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to save the renamed dataframe
def save_file(df):
    # Prompt the user to select a location to save the renamed file
    save_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save Renamed CSV File"
    )
    
    if save_path:
        try:
            # Save the renamed dataframe to the selected path
            df.to_csv(save_path, index=False)
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving: {str(e)}")

# Set up the GUI
root = tk.Tk()
root.title("CSV Column Renamer")

# Create a button to load and rename the CSV file
rename_button = tk.Button(root, text="Load and Rename CSV", command=load_and_rename)
rename_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()

