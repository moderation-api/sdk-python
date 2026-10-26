# GetAnalyticsChannelsResponse

Successful response


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `range`                                                                                    | [models.GetAnalyticsChannelsRangeResponse](../models/getanalyticschannelsrangeresponse.md) | :heavy_check_mark:                                                                         | The time window of the numbers.                                                            |
| `channels`                                                                                 | List[[models.GetAnalyticsChannelsChannel](../models/getanalyticschannelschannel.md)]       | :heavy_check_mark:                                                                         | Requests and flags per channel. Channels with no requests in the window are not included.  |