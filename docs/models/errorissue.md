# ErrorIssue


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `message`                                          | *str*                                              | :heavy_check_mark:                                 | What is wrong.                                     |
| `path`                                             | List[[models.Path](../models/path.md)]             | :heavy_minus_sign:                                 | Location of the invalid field in the request body. |
| `code`                                             | *Optional[str]*                                    | :heavy_minus_sign:                                 | Validation rule that failed.                       |