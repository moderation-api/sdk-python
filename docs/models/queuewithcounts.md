# QueueWithCounts


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | The queue ID.                                          |
| `name`                                                 | *str*                                                  | :heavy_check_mark:                                     | The queue name.                                        |
| `description`                                          | *Nullable[str]*                                        | :heavy_check_mark:                                     | The queue description.                                 |
| `is_default`                                           | *bool*                                                 | :heavy_check_mark:                                     | Whether this is the default queue of the project.      |
| `unresolved_items_count`                               | *int*                                                  | :heavy_check_mark:                                     | Number of items that wait for review.                  |
| `resolved_items_count`                                 | *int*                                                  | :heavy_check_mark:                                     | Number of items that are resolved.                     |
| `total_items_count`                                    | *int*                                                  | :heavy_check_mark:                                     | Number of items in the queue, resolved and unresolved. |