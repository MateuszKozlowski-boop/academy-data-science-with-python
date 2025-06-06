
def filter_weight_greater_than_250(df):
    return df["weight"] > 250

(
    chickweight  
    .loc[chickweight['chick'] == 25]
    .set_index('rownum')       
    .loc[filter_weight_greater_than_250] 
)
