def clean_data(raw_df):
    # Take a copy of raw_data
    processed_data = raw_df

    # Columns to fill with 'None'
    fill_with_none = [
        'Alley','MasVnrType','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2',
        'FireplaceQu','GarageType','GarageFinish','GarageQual','GarageCond','PoolQC','Fence','MiscFeature'  
    ]

    # Columns to fill with 0s
    fill_with_zero = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']

    # Fill/ Transform data with NA values
    processed_data[fill_with_zero] = processed_data[fill_with_zero].fillna(0)
    processed_data[fill_with_none] = processed_data[fill_with_none].fillna('None')
    processed_data.Electrical = processed_data.Electrical.fillna(processed_data.Electrical.mode())

    return(processed_data)