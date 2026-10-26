# GetAnalyticsAuthorsAuthor


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `author_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | The author ID from your system. Use it with the authors endpoints. |
| `name`                                                             | *Nullable[str]*                                                    | :heavy_check_mark:                                                 | The author name, if known.                                         |
| `flagged`                                                          | *int*                                                              | :heavy_check_mark:                                                 | Flagged requests from this author in the window.                   |