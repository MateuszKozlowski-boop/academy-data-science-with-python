
(
    chickweight
    .groupby("time")
    ["weight"]
    .min()
)