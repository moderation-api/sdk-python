# DeleteWordlistResponse

Wordlist deleted successfully


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | ID of the deleted wordlist                                            |
| `deleted`                                                             | *bool*                                                                | :heavy_check_mark:                                                    | Whether the wordlist was deleted                                      |
| `detached_channel_ids`                                                | List[*str*]                                                           | :heavy_check_mark:                                                    | IDs of the channels that used the wordlist. It was removed from them. |