# UnresolveQueueItemResponse

Successful response


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `success`                                                                | *bool*                                                                   | :heavy_check_mark:                                                       | N/A                                                                      |
| `status`                                                                 | [models.UnresolveQueueItemStatus](../models/unresolvequeueitemstatus.md) | :heavy_check_mark:                                                       | `pending` waits for review. `resolved` is reviewed.                      |
| `unresolved_at`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | When the item was unresolved (ISO 8601).                                 |