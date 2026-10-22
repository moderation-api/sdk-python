# CreateAuthorMetadata

Additional metadata provided by your system. We recommend including any relevant information that may assist in the moderation process.


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `email_verified`                              | *OptionalNullable[bool]*                      | :heavy_minus_sign:                            | Whether the author's email is verified        |
| `phone_verified`                              | *OptionalNullable[bool]*                      | :heavy_minus_sign:                            | Whether the author's phone number is verified |
| `identity_verified`                           | *OptionalNullable[bool]*                      | :heavy_minus_sign:                            | Whether the author's identity is verified     |
| `is_paying_customer`                          | *OptionalNullable[bool]*                      | :heavy_minus_sign:                            | Whether the author is a paying customer       |
| `__pydantic_extra__`                          | Dict[str, *Any*]                              | :heavy_minus_sign:                            | N/A                                           |