# GetAnalyticsVolumesResponse

Successful response


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `range`                                                                                  | [models.GetAnalyticsVolumesRangeResponse](../models/getanalyticsvolumesrangeresponse.md) | :heavy_check_mark:                                                                       | The time window of the numbers.                                                          |
| `channel_id`                                                                             | *Nullable[str]*                                                                          | :heavy_check_mark:                                                                       | The channel the numbers are for. Null when they are for all channels.                    |
| `bucket`                                                                                 | [models.Bucket](../models/bucket.md)                                                     | :heavy_check_mark:                                                                       | The size of each entry in `volumes`.                                                     |
| `volumes`                                                                                | List[[models.Volume](../models/volume.md)]                                               | :heavy_check_mark:                                                                       | Counts over time, oldest first. Buckets with no requests are included with zeros.        |