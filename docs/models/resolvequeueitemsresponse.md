# ResolveQueueItemsResponse

Successful response


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `resolved`                                 | *int*                                      | :heavy_check_mark:                         | Number of items resolved.                  |
| `not_found_ids`                            | List[*str*]                                | :heavy_check_mark:                         | Item IDs that do not exist in the project. |