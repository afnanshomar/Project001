"""
The function get_sum_metrics takes two arguments:
a prediction and a list of metrics to apply to the prediction
(say, for instance, the accuracy or the precision).
Note that each metric is a function, not a number.
The function should compute each of the metrics for the prediction and sum them.
It should also add to this sum three default metrics, in this case, adding 0, 1 or 2 to the prediction.
"""

def get_sum_metrics(prediction, metrics=None):
    if not metrics:
        metrics = []

    for i in range(3):
        metrics.append(gen_add_i(i))  # Append lambda functions to metrics

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(prediction)

    return sum_metrics

def gen_add_i(i):
    return lambda x: x + i
print(get_sum_metrics(0))
print(get_sum_metrics(1))
print(get_sum_metrics(2))
print(get_sum_metrics(3))
print(get_sum_metrics(0))
print(get_sum_metrics(1))
print(get_sum_metrics(2))


