# SuspendAuthorRequestBody


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `reason`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Why the action was taken. Saved with the action and sent in the webhook event. |
| `duration`                                                                     | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | How long the suspension lasts, in milliseconds. Defaults to 24 hours.          |