# TopReviewer


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `user_id`                                                               | *Nullable[str]*                                                         | :heavy_check_mark:                                                      | The user ID of the reviewer. `null` for items resolved with an API key. |
| `name`                                                                  | *Nullable[str]*                                                         | :heavy_check_mark:                                                      | The name of the reviewer.                                               |
| `review_count`                                                          | *int*                                                                   | :heavy_check_mark:                                                      | Number of items the reviewer resolved in the period.                    |