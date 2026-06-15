# Edge Case

## Empty student list for `/stats`

The edge case I identified is when the database contains no students and the `/stats` endpoint is requested.

Without handling this case, the backend would try to calculate the average using `sum(marks) / count`, where `count` is `0`. This would cause a division by zero error. Calling `min()` or `max()` on an empty list would also cause an error.

In my implementation, I check whether `count == 0` before calculating the statistics. If there are no marks, `/stats` returns:

- `count`: `0`
- `average`: `0`
- `min`: `null`
- `max`: `null`

I chose `null` for `min` and `max` because there is no minimum or maximum mark when there are no students.