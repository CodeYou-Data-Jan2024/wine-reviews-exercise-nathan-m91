import pandas as pd

wine_reviews = pd.read_csv("C:/Users/moose/Documents/Projects/Wine Reviews/wine-reviews-exercise-nathan-m91/winemag-data-130k-v2.csv", index_col=0)
data = wine_reviews[['country', 'points']]
csv_data = data.groupby('country').aggregate(count=('points', 'size'), points=('points', 'mean'))
csv_data['points'] = csv_data['points'].round(1)
final = csv_data.sort_values(by='count', ascending=False).reset_index()
final_df = pd.DataFrame(final)
final_df.to_csv('reviews-per-country.csv')
print(final_df)