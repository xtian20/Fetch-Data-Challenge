def _check_duplicated_data_on_column(df, columns_to_check=None):
    """
    This is a helper function used to get the total number of duplicated rows 
    for a given dataframe against specified column(s).

    :param df: The dataframe to check.
    :type df: dataframe
    :param columns_to_check: The columns to check against for duplication.
    :type columns_to_check: list
    :return: The count of duplicated rows
    """
    return df.duplicated(subset=columns_to_check).sum()


def check_fully_duplicated(df):
    """
    This function is used to check if there exist fully duplicated data.
    If exists fully duplication, return the examples of duplicated data.

    :param df: The dataframe to check.
    :type df: dataframe
    :return: First ten rows of duplicated data.
    """
    fully_duplicate = _check_duplicated_data_on_column(df)
    if fully_duplicate == 0:
        print("There's no fully duplicated data.")
    else:
        print(
            f"There exists {fully_duplicate} fully duplicate."
        )
        df_copy = df.copy()
        # df.drop_duplicates(keep="first", inplace=True)
        print("\nDuplicated example:")
        return (
            df_copy[df_copy.duplicated(keep=False)]
            .sort_values(by=df_copy.columns.tolist())
            .head(10)
        )
    

def check_partial_duplicated(df, columns_to_check):
    """
    This function is used to check if there exist partial duplicated data.
    i.e. Data duplicated in specified column(s).

    :param df: The dataframe to check.
    :type df: dataframe
    :param columns_to_check: The columns to check against for duplication.
    :type columns_to_check: list
    :return: Duplicated data or None.
    """
    partial_duplicate = _check_duplicated_data_on_column(df, columns_to_check)
    if partial_duplicate > 0:
        duplicated_rows = df[df.duplicated(subset=columns_to_check, keep=False)]  # Find rows where values in the specified columns are duplicated
        duplicated_values = duplicated_rows[columns_to_check].drop_duplicates().values.tolist()  # Extract unique duplicated values from the specified columns
        duplicated_values_cnt = len(duplicated_values)

        print(f"There exist {duplicated_values_cnt} duplicated values in field {columns_to_check}.")
        print("\nDuplicated example:")
        return df[df.duplicated(subset=columns_to_check, keep=False)].sort_values(by=columns_to_check).head(10)
    else:
        print(f"Values in {columns_to_check} are completely unique.")
    


def check_data_missing(df):
    """
    This function returns the information about a given dataframe,
    including its shape, and the missing data percentage in each column.

    :param df:  The dataframe to check.
    :type df: dataframe
    :return: None
    """
    rows, cols = df.shape[0], df.shape[1]

    all_null_cnt = df.isna().sum().sum()
    if all_null_cnt == 0:
        print("No null values exist.")
    else:
        print(f"Dataframe exist null values. Let's dive deeper: ")
        for col in df.columns:
            null_cnt = df[col].isna().sum()
            if null_cnt > 0 and null_cnt != rows:
                null_pct = round((null_cnt / rows) * 100, 2)
                print(f"\tColumn {col} ({df[col].dtype}) has {null_pct}% null values.")
            elif null_cnt == rows:
                print(f"\tColumn {col} ({df[col].dtype}) values is completely missing.")
            else: 
                print(f"\tColumn {col} ({df[col].dtype}) has no null values.")
    