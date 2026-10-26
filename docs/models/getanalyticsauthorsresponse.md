# GetAnalyticsAuthorsResponse

Successful response


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `range`                                                                                                 | [models.GetAnalyticsAuthorsRangeResponse](../models/getanalyticsauthorsrangeresponse.md)                | :heavy_check_mark:                                                                                      | The time window of the numbers.                                                                         |
| `channel_id`                                                                                            | *Nullable[str]*                                                                                         | :heavy_check_mark:                                                                                      | The channel the numbers are for. Null when they are for all channels.                                   |
| `authors`                                                                                               | List[[models.GetAnalyticsAuthorsAuthor](../models/getanalyticsauthorsauthor.md)]                        | :heavy_check_mark:                                                                                      | The authors with the most flagged requests, largest first. Requests without an author are not included. |