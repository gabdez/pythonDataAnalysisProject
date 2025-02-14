# Python for Data Analysis Project A5
A5 Project of "Data for python analysis"

## Contributors
Alexis JAMBUT - Gabriel FERNANDEZ CASA

## Project description
- Analyse a given dataset
- Powerpoint presentation on this dataset
- A python script with data visualisation and modelisation
- A Flask/Django API that render prediction of our model

## Dataset
https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity

## Dataset Prediction Goal
With this dataset, our goal will be to predict the popularity of an article (according to the number of shares of an article) thanks to the different features of the dataset.
We decided to take the classification approach of this problem by creating two class (popular > 1400 shares / unpopular < 1400 shares) based on number of shares of an article.

## Result

After some data processing and data normalisation. We run some classifier models

* Knn
* Random forest
* Adaboost
* Gradient boost

We get thoose results:
|        | knn        | Random forest           | Adaboost |  Gradient boost
| ------------- | ------------- |:-------------:| -----:| -----:|
| Accuracy      | 0.60 | 0.66 | 0.65 | 0.66 |
| ROC      | 0.61      |   0.72 |   0.71 |  0.72 |

Our best model get 66% of good prediction. Its not that good but we can see with the ROC that it can be improve up to 0.72.
This 66% of prediction maybe mean that the dataset have not enought features to get good prediction accuracy.

We use Random forest classifier in our api.

## API

Run the server api in local `python api.py`

Endpoints of our API:

* `/predict_popularity/<int:article_id>` -> return the prediction and if the prediction is good or not ` {"is_truly_popular": true,"message": "Prediction exacte","prediction": true}`
* `/max_article_nbr` -> return the max article number possible to predict

You can run our `request.py` to directly ask your api running in local

## Dataset description

The attributes of data are described as follows:-

     0. url: URL of the article
     1. timedelta: Days between the article publication and
                                       the dataset acquisition
     2. n_tokens_title:                Number of words in the title
     3. n_tokens_content:              Number of words in the content
     4. n_unique_tokens:               Rate of unique words in the content
     5. n_non_stop_words:              Rate of non-stop words in the content
     6. n_non_stop_unique_tokens:      Rate of unique non-stop words in the
                                       content
     7. num_hrefs:                     Number of links
     8. num_self_hrefs:                Number of links to other articles
                                       published by Mashable
     9. num_imgs:                      Number of images
    10. num_videos:                    Number of videos
    11. average_token_length:          Average length of the words in the
                                       content
    12. num_keywords:                  Number of keywords in the metadata
    13. data_channel_is_lifestyle:     Is data channel 'Lifestyle'?
    14. data_channel_is_entertainment: Is data channel 'Entertainment'?
    15. data_channel_is_bus:           Is data channel 'Business'?
    16. data_channel_is_socmed:        Is data channel 'Social Media'?
    17. data_channel_is_tech:          Is data channel 'Tech'?
    18. data_channel_is_world:         Is data channel 'World'?
    19. kw_min_min:                    Worst keyword (min. shares)
    20. kw_max_min:                    Worst keyword (max. shares)
    21. kw_avg_min:                    Worst keyword (avg. shares)
    22. kw_min_max:                    Best keyword (min. shares)
    23. kw_max_max:                    Best keyword (max. shares)
    24. kw_avg_max:                    Best keyword (avg. shares)
    25. kw_min_avg:                    Avg. keyword (min. shares)
    26. kw_max_avg:                    Avg. keyword (max. shares)
    27. kw_avg_avg:                    Avg. keyword (avg. shares)
    28. self_reference_min_shares:     Min. shares of referenced articles in
                                       Mashable
    29. self_reference_max_shares:     Max. shares of referenced articles in
                                       Mashable
    30. self_reference_avg_sharess:    Avg. shares of referenced articles in
                                       Mashable
    31. weekday_is_monday:             Was the article published on a Monday?
    32. weekday_is_tuesday:            Was the article published on a Tuesday?
    33. weekday_is_wednesday:          Was the article published on a Wednesday?
    34. weekday_is_thursday:           Was the article published on a Thursday?
    35. weekday_is_friday:             Was the article published on a Friday?
    36. weekday_is_saturday:           Was the article published on a Saturday?
    37. weekday_is_sunday:             Was the article published on a Sunday?
    38. is_weekend:                    Was the article published on the weekend?
    39. LDA_00:                        Closeness to LDA topic 0
    40. LDA_01:                        Closeness to LDA topic 1
    41. LDA_02:                        Closeness to LDA topic 2
    42. LDA_03:                        Closeness to LDA topic 3
    43. LDA_04:                        Closeness to LDA topic 4
    44. global_subjectivity:           Text subjectivity
    45. global_sentiment_polarity:     Text sentiment polarity
    46. global_rate_positive_words:    Rate of positive words in the content
    47. global_rate_negative_words:    Rate of negative words in the content
    48. rate_positive_words:           Rate of positive words among non-neutral
                                       tokens
    49. rate_negative_words:           Rate of negative words among non-neutral
                                       tokens
    50. avg_positive_polarity:         Avg. polarity of positive words
    51. min_positive_polarity:         Min. polarity of positive words
    52. max_positive_polarity:         Max. polarity of positive words
    53. avg_negative_polarity:         Avg. polarity of negative  words
    54. min_negative_polarity:         Min. polarity of negative  words
    55. max_negative_polarity:         Max. polarity of negative  words
    56. title_subjectivity:            Title subjectivity
    57. title_sentiment_polarity:      Title polarity
    58. abs_title_subjectivity:        Absolute subjectivity level
    59. abs_title_sentiment_polarity:  Absolute polarity level
    60. shares:                        Number of shares (target)
