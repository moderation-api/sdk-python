# GetQueueStatsResponse

Successful response


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `review_stats`                                       | [models.ReviewStats](../models/reviewstats.md)       | :heavy_check_mark:                                   | N/A                                                  |
| `action_stats`                                       | List[[models.ActionStat](../models/actionstat.md)]   | :heavy_check_mark:                                   | N/A                                                  |
| `top_reviewers`                                      | List[[models.TopReviewer](../models/topreviewer.md)] | :heavy_check_mark:                                   | List of top reviewers and their statistics           |
| `trends`                                             | [models.Trends](../models/trends.md)                 | :heavy_check_mark:                                   | N/A                                                  |