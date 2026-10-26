# GetQueueStatsResponse

Successful response


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `review_stats`                                                | [models.ReviewStats](../models/reviewstats.md)                | :heavy_check_mark:                                            | N/A                                                           |
| `top_reviewers`                                               | List[[models.TopReviewer](../models/topreviewer.md)]          | :heavy_check_mark:                                            | Reviewers with the most resolved items, most first. Up to 10. |
| `trends`                                                      | [models.Trends](../models/trends.md)                          | :heavy_check_mark:                                            | N/A                                                           |