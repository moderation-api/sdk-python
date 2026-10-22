# Evaluation

The evaluation of the content after running the channel policies.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `flagged`                                                                           | *bool*                                                                              | :heavy_check_mark:                                                                  | Whether the content was flagged by any policy.                                      |
| `flag_probability`                                                                  | *float*                                                                             | :heavy_check_mark:                                                                  | The probability that the content should be flagged.                                 |
| `severity_score`                                                                    | *float*                                                                             | :heavy_check_mark:                                                                  | The severity score of the content. A higher score indicates more severe content.    |
| `unicode_spoofed`                                                                   | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether the content was flagged for Unicode spoofing.                               |
| `shadow_flagged`                                                                    | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether the content would have been flagged by analyze-only policies (flag: false). |