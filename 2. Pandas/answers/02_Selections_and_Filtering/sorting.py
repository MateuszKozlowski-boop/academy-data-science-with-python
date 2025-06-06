
# 1 and 2
(
    chickweight
    .sort_values(by='rownum', ascending=False)
    .head(25)
)

# 3
(
    chickweight
    .sort_values(by=['weight', 'chick'], ascending=[True, False])
)
