# TopReviewer


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `user_id`                                               | *str*                                                   | :heavy_check_mark:                                      | ID of the reviewer                                      |
| `name`                                                  | *str*                                                   | :heavy_check_mark:                                      | Name of the reviewer                                    |
| `review_count`                                          | *float*                                                 | :heavy_check_mark:                                      | Number of items reviewed                                |
| `average_time_per_review`                               | *float*                                                 | :heavy_check_mark:                                      | Average review time in milliseconds                     |
| `accuracy_score`                                        | *Optional[float]*                                       | :heavy_minus_sign:                                      | Optional accuracy score based on review quality metrics |
| `top_actions`                                           | List[[models.TopAction](../models/topaction.md)]        | :heavy_check_mark:                                      | Most common actions taken by this reviewer              |