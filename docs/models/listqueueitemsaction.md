# ListQueueItemsAction


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `id`                                        | *str*                                       | :heavy_check_mark:                          | Action ID                                   |
| `name`                                      | *str*                                       | :heavy_check_mark:                          | Action name                                 |
| `comment`                                   | *Optional[str]*                             | :heavy_minus_sign:                          | Action comment                              |
| `timestamp`                                 | *float*                                     | :heavy_check_mark:                          | Unix timestamp of when the action was taken |
| `reviewer`                                  | *Optional[str]*                             | :heavy_minus_sign:                          | Moderator userID                            |