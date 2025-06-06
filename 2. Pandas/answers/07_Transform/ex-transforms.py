(
    chickweight
    .assign(mean_weight_diet=lambda df: df.groupby("diet")['weight'].transform('mean'),
            mean_weight_diet_time=lambda df: df.groupby(["diet", "time"])['weight'].transform('mean'),
            num_chickens_diet=lambda df: df.groupby("diet")["chick"].transform(lambda x: x.nunique())
           )
)
