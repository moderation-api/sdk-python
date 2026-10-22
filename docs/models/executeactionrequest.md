# ExecuteActionRequest

Input parameters


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `action_key`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | ID or key of the action to execute                                          |
| `content_ids`                                                               | List[*str*]                                                                 | :heavy_minus_sign:                                                          | IDs of the content items to apply the action to. Provide this or authorIds. |
| `author_ids`                                                                | List[*str*]                                                                 | :heavy_minus_sign:                                                          | IDs of the authors to apply the action to. Provide this or contentIds.      |
| `value`                                                                     | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Optional value to provide with the action                                   |
| `queue_id`                                                                  | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Optional queue ID if the action is queue-specific                           |
| `duration`                                                                  | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | Optional duration in milliseconds for actions with timeouts                 |