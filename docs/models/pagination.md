# Pagination

Where this page is in the full list.


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `page`                           | *int*                            | :heavy_check_mark:               | The current page, starting at 1. |
| `page_size`                      | *int*                            | :heavy_check_mark:               | Number of items per page.        |
| `total`                          | *int*                            | :heavy_check_mark:               | Total number of items.           |
| `total_pages`                    | *int*                            | :heavy_check_mark:               | Total number of pages.           |
| `has_more`                       | *bool*                           | :heavy_check_mark:               | Whether there is a next page.    |