import pandas as pd
import numpy as np


class DataPreview:

    '''
    functions to get some information about the data
    '''

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def show_datatypes(self) -> pd.DataFrame:
        return self.df.dtypes

    def show_data_description(self) -> pd.DataFrame:
        return self.df.describe()

    def show_data_information(self) -> pd.DataFrame:
        return self.df.info()

    def show_statistical_info(self) -> pd.DataFrame:
        return self.df.agg(['mean'])

    def show_correlation(self) -> pd.DataFrame:
        return self.df.corr()

    def collective_grouped_mean(self, colomnName: str) -> pd.DataFrame:
        groupby_colomnName = self.df.groupby(colomnName)
        return groupby_colomnName.mean()

    def list_coloumn_names(self) -> pd.DataFrame:
        return self.df.columns

    '''
    Functions for explorations of dataset columns
    '''

    def percent_missing(self, df: pd.DataFrame):

        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        # print("The Store dataset contains", round(
        # ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

        return print("The dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

    def missing_values_table(self):
        # Total missing values
        mis_val = self.df.isnull().sum()

        total_entries = self.df.shape[0]
        # Percentage of missing values
        missing_percentage = []
        for col_missing_entries in mis_val:
            value = str(
                round(((col_missing_entries/total_entries) * 100), 2)) + " %"
            missing_percentage.append(value)
        # Rename the columns

        missing_df = pd.DataFrame(mis_val, columns=['total_missing_values'])
        missing_df['missing_percentage'] = missing_percentage
        missing_df = missing_df.rename(
            columns={0: 'Missing Values', 1: '% of Total Values'}).sort_values(
            'total_missing_values', ascending=False).round(1)

        # mis_val_table_ren_columns = mis_val_table_ren_columns[
        # mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        # '% of Total Values', ascending=False).round(1)

        return missing_df

    def get_duplicates(self):
        return self.df[self.df.duplicated()]
