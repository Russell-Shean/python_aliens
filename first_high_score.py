# create high score file
import pandas
from datetime import date


# define dictionary of scores

high_scores_dict = {
	'date': [date.today(), date.today()],
	'score': [0, 200],
	'level': [1, 1]
}


# convert to a pandas dataframe
high_scores_df = pandas.DataFrame(high_scores_dict)


# write dataframe out as a csv file
high_scores_df.to_csv("high_score.csv", index = False)