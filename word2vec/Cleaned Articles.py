import pandas as pd
import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and numbers, keep only alphabetic characters and spaces
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_abstracts_from_csv(input_csv, output_csv, text_column='abstract'):
    # Load CSV
    df = pd.read_csv("Articles - 2020.csv")
    
    # Clean abstracts
    df[text_column] = df[text_column].apply(clean_text)
    
    # Save cleaned data to a new CSV
    df.to_csv(output_csv, index=False)
    print(f"Cleaned data saved to {output_csv}")

# Example usage:
# clean_abstracts_from_csv('input_abstracts.csv', 'cleaned_abstracts.csv')
