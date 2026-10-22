# GetWordlistResponse

Successful response


## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `id`                          | *str*                         | :heavy_check_mark:            | ID of the wordlist            |
| `name`                        | *Nullable[str]*               | :heavy_check_mark:            | N/A                           |
| `words`                       | List[*str*]                   | :heavy_check_mark:            | Words in the wordlist         |
| `created_at`                  | *str*                         | :heavy_check_mark:            | Creation date of the wordlist |
| `organization_id`             | *str*                         | :heavy_check_mark:            | ID of the organization        |
| `user_id`                     | *Nullable[str]*               | :heavy_check_mark:            | N/A                           |
| `strict`                      | *bool*                        | :heavy_check_mark:            | Strict mode                   |