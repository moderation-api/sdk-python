# GetAccountResponse

Account details retrieved successfully


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | ID of the account                                              |
| `paid_plan_name`                                               | *str*                                                          | :heavy_check_mark:                                             | Name of the paid plan                                          |
| `text_api_quota`                                               | *float*                                                        | :heavy_check_mark:                                             | Text API quota                                                 |
| `remaining_quota`                                              | *float*                                                        | :heavy_check_mark:                                             | Remaining quota                                                |
| `current_project`                                              | [Optional[models.CurrentProject]](../models/currentproject.md) | :heavy_minus_sign:                                             | N/A                                                            |