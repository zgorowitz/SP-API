import os
import pandas as pd


def load_csv(file_path):
   return pd.read_csv(file_path)


# open all files in folder and join them
def load_sellerboard_data(folder_path):
   dfs = []
   for filename in os.listdir(folder_path):
       if filename.endswith('.csv'):
           file_path = os.path.join(folder_path, filename)
           df = pd.read_csv(file_path, sep=';')
           dfs.append(df)
   return pd.concat(dfs).reset_index(drop=True)


#### Add category file
def merge_dataframes(sellerboard, df_label, df_parent):
   merged_df = pd.merge(sellerboard, df_label[['ASIN', 'LABEL']], on='ASIN', how='left')
   merged_df = pd.merge(merged_df, df_parent[['ASIN', 'Parent']], on='ASIN', how='left')
   return merged_df


#### Add calculated columns to the DataFrame.
def add_columns(df):
   df['Date'] = pd.to_datetime(df['Date'])
   df['TotalSales'] = df['SalesOrganic'] + df['SalesPPC']
   df['TotalUnits'] = df['UnitsPPC'] + df['UnitsOrganic']
   df['Month'] = df['Date'].dt.month
   df['Week'] = df['Date'].dt.isocalendar().week
   df['day'] = df['Date'].dt.day
   return df




def print_merge_stats(df):
   total_rows = df.shape[0]
   merged_rows = df['LABEL'].notna().sum()
   missing_rows = df['LABEL'].isna().sum()
   print(f"Total rows: {total_rows}")
   print(f"Merged rows: {merged_rows}")
   print(f"Missing rows: {missing_rows}")


def clean_columns(df):
   df = df[df['Marketplace'] == 'Amazon.com']
   df = df.drop('Marketplace', axis=1)
   df['Spend'] = df['SponsoredProducts'].abs()


   return df
  


#### File paths
def main():
   category_file = "/Users/zalmangorowitz/Documents/python/python_files/Category.csv"
   parent_file = "/Users/zalmangorowitz/Documents/python/python_files/Parent Child.csv"
   sellerboard_folder = "/Users/zalmangorowitz/Documents/sellerboard"


   # Load data
   df_label = load_csv(category_file)
   df_parent = load_csv(parent_file)
   sellerboard = load_sellerboard_data(sellerboard_folder)


   # Filter & Add columns
   sellerboard = clean_columns(sellerboard)
   final_df = add_columns(merged_df)
   # print("------------------Seller board----------------")


   # Merge dataframes
   merged_df = merge_dataframes(sellerboard, df_label, df_parent)


   # Print merge statistics
   print_merge_stats(merged_df)


   # print("\n------------------Final DataFrame----------------")
   # print(final_df.head(1))
   final_df.to_csv('output.csv', index=False)
if __name__ == "__main__":
   main()

