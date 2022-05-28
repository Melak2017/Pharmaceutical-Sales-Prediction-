import numpy as np
import pandas as pd


class CleanStoreDf:
    def __init__(self, df: pd.DataFrame, deep=False) -> None:
        """
        ------
        Returns a DataCleaner Object with the passed DataFrame Data set as its own DataFrame
        Parameters
        ------
        """
        if(deep):
            self.df = df.copy(deep=True)
        else:
            self.df = df

    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        ----------
        Returns a DataFrame where the specified columns in the list are removed
        Parameters
        ----------

        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def separate_date_column(self, date_column: str, drop_date=True) -> pd.DataFrame:
        try:
            date_index = self.df.columns.get_loc(date_column)
            self.df.insert(date_index + 1, 'Year', self.df[date_column].apply(
                lambda x: x.date().year))
            self.df.insert(date_index + 2, 'Month', self.df[date_column].apply(
                lambda x: x.date().month))
            self.df.insert(date_index + 3, 'Day',
                           self.df[date_column].apply(lambda x: x.date().day))

            if(drop_date):
                self.df = self.df.drop(date_column, axis=1)

        except:
            print("Failed to separate the date to its components")

    def change_column_to_date_type(self, col_name: str) -> None:
        try:
            self.df[col_name] = pd.to_datetime(self.df[col_name])
        except:
            print('failed to change column to Date Type')

    def remove_nulls(self) -> pd.DataFrame:
        return self.df.dropna()

    def add_season_col(self, month_col: str) -> None:
        # helper function
        def get_season(month: int):
            if(month <= 2 or month == 12):
                return 'Winter'
            elif(month > 2 and month <= 5):
                return 'Spring'
            elif(month > 5 and month <= 8):
                return 'Summer'
            else:
                return 'Autumn'

        try:
            month_index = self.df.columns.get_loc(month_col)
            self.df.insert(month_index + 1, 'Season',
                           self.df[month_col].apply(get_season))

        except:
            print("Failed to add season column")

    def change_columns_type_to(self, cols: list, data_type: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns data types are changed to the specified data type
        Parameters
        ----------
        cols:
            Type: list
        data_type:
            Type: str
        Returns
        -------
        pd.DataFrame
        """
        try:
            for col in cols:
                self.df[col] = self.df[col].astype(data_type)
        except:
            print('Failed to change columns type')

        return self.df

    def remove_single_value_columns(self, unique_value_counts: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a DataFrame where columns with a single value are removed
        Parameters
        ----------
        unique_value_counts:
            Type: pd.DataFrame
        Returns
        -------
        pd.DataFrame
        """
        drop_cols = list(
            unique_value_counts.loc[unique_value_counts['Unique Value Count'] == 1].index)
        return self.df.drop(drop_cols, axis=1, inplace=True)

    def remove_duplicates(self) -> pd.DataFrame:
        """
        ---------
        Returns a DataFrame where duplicate rows are removed
        Parameters
        ----------
        """
        removables = self.df[self.df.duplicated()].index
        return self.df.drop(index=removables, inplace=True)

    def fill_numeric_values(self, missing_cols: list, acceptable_skewness: float = 5.0) -> pd.DataFrame:
        """
        ----------
        Returns a DataFrame where numeric columns are filled with either median or mean based on their skewness
        Parameters
        ----------

        """
        df_skew_data = self.df[missing_cols]
        df_skew = df_skew_data.skew(axis=0, skipna=True)
        for i in df_skew.index:
            if(df_skew[i] < acceptable_skewness and df_skew[i] > (acceptable_skewness * -1)):
                value = self.df[i].mean()
                self.df[i].fillna(value, inplace=True)
            else:
                value = self.df[i].median()
                self.df[i].fillna(value, inplace=True)

        return self.df

    def add_columns_from_another_df_using_column(self, from_df: pd.DataFrame, base_col: str, add_columns: list) -> pd.DataFrame:
        try:
            new_df = self.df.copy(deep=True)
            from_df.sort_values(base_col, ascending=True, inplace=True)
            for col in add_columns:
                col_index = from_df.columns.tolist().index(col)
                new_df[col] = new_df[base_col].apply(
                    lambda x: from_df.iloc[x-1, col_index])

            return new_df

        except:
            print('Failed to add columns from other dataframe')

    def fill_non_numeric_values(self, missing_cols: list, ffill: bool = True, bfill: bool = False) -> pd.DataFrame:
        """
        ----------
        Returns a DataFrame where non-numeric columns are filled with forward or backward fill
        Parameters
        ----------

        """
        for col in missing_cols:
            if(ffill == True and bfill == True):
                self.df[col].fillna(method='ffill', inplace=True)
                self.df[col].fillna(method='bfill', inplace=True)

            elif(ffill == True and bfill == False):
                self.df[col].fillna(method='ffill', inplace=True)

            elif(ffill == False and bfill == True):
                self.df[col].fillna(method='bfill', inplace=True)

            else:
                self.df[col].fillna(method='bfill', inplace=True)
                self.df[col].fillna(method='ffill', inplace=True)

        return self.df

    def create_new_columns_from(self, new_col_name: str, col1: str, col2: str, func) -> pd.DataFrame:
        """
        ----------
        Returns a DataFrame where a new column is created using a function on two specified columns
        Parameters
        ----------
        """
        try:
            self.df[new_col_name] = func(self.df[col1], self.df[col2])
        except:
            print("failed to create new column with the specified function")

        return self.df

    def fix_outlier(self, column: str) -> pd.DataFrame:
        """
        ---------
        Returns a DataFrame where outlier of the specified column is fixed
        Parameters
        ----------

        """
        self.df[column] = np.where(self.df[column] > self.df[column].quantile(
            0.95), self.df[column].median(), self.df[column])

        return self.df

    def fix_outlier_columns(self, columns: list) -> pd.DataFrame:
        """
        ---------
        Returns a DataFrame where outlier of the specified columns is fixed
        Parameters
        ---------
        """
        try:
            for column in columns:
                self.df[column] = np.where(self.df[column] > self.df[column].quantile(
                    0.95), self.df[column].median(), self.df[column])
        except:
            print("Cant fix outliers for each column")

        return self.df

    def save_clean_data(self, name: str):
        """
        ----------
        The objects dataframe gets saved with the specified name 
        Parameters
        ----------
        """
        try:
            self.df.to_csv(name, index=False)

        except:
            print("Failed to save data")

    def optimize_df(self) -> pd.DataFrame:
        """
        Returns the DataFrames information after all column data types are optimized (to a lower data type)
        Parameters
        ----------
        None
        Returns
        -------
        pd.DataFrame
        """
        data_types = self.df.dtypes
        optimizable = ['float64', 'int64']
        try:
            for col in data_types.index:
                if(data_types[col] in optimizable):
                    if(data_types[col] == 'float64'):
                        # downcasting a float column
                        self.df[col] = pd.to_numeric(
                            self.df[col], downcast='float')
                    elif(data_types[col] == 'int64'):
                        # downcasting an integer column
                        self.df[col] = pd.to_numeric(
                            self.df[col], downcast='unsigned')

            return self.df

        except:
            print('Failed to optimize')
