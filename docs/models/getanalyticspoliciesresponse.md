# GetAnalyticsPoliciesResponse

Successful response


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `range`                                                                                    | [models.GetAnalyticsPoliciesRangeResponse](../models/getanalyticspoliciesrangeresponse.md) | :heavy_check_mark:                                                                         | The time window of the numbers.                                                            |
| `channel_id`                                                                               | *Nullable[str]*                                                                            | :heavy_check_mark:                                                                         | The channel the numbers are for. Null when they are for all channels.                      |
| `policies`                                                                                 | List[[models.GetAnalyticsPoliciesPolicy](../models/getanalyticspoliciespolicy.md)]         | :heavy_check_mark:                                                                         | The policy labels with the most flagged requests, largest first.                           |