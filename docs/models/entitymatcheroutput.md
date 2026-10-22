# EntityMatcherOutput

Entity matcher policy.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `type`                                                             | *Literal["entity_matcher"]*                                        | :heavy_check_mark:                                                 | N/A                                                                |
| `probability`                                                      | *float*                                                            | :heavy_check_mark:                                                 | N/A                                                                |
| `flagged`                                                          | *bool*                                                             | :heavy_check_mark:                                                 | N/A                                                                |
| `flagged_fields`                                                   | List[*str*]                                                        | :heavy_minus_sign:                                                 | N/A                                                                |
| `matches`                                                          | List[[models.SubmitContentMatch](../models/submitcontentmatch.md)] | :heavy_check_mark:                                                 | N/A                                                                |