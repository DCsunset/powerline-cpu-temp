import psutil

def cpu_temp(pl, format="{value:.0f}°C", threshold_good=50, threshold_bad=90):
    '''Return cpu temperature.

    :param str format:
        format string, receives ``value`` as an argument
    :param float threshold_good:
        threshold for gradient level 0: temperature below this
        value will have this gradient level.
    :param float threshold_bad:
        threshold for gradient level 100: temperature  above this
        value will have this gradient level. Load averages between
        ``threshold_good`` and ``threshold_bad`` receive gradient level that
        indicates relative position in this interval:
        (``100 * (cur-good) / (bad-good)``).

    Divider highlight group used: ``background:divider``.

    Highlight groups used: ``cpu_temp_gradient`` (gradient) or ``cpu_temp``.
    '''

    temp = psutil.sensors_temperatures()['coretemp'][0].current
    if temp < threshold_good:
        gradient_level = 0
    elif temp < threshold_bad:
        gradient_level = (temp - threshold_good) * 100.0 / (threshold_bad - threshold_good)
    else:
        gradient_level = 100
    return [
        {
            'contents': format.format(value=temp),
            'gradient_level': gradient_level,
            'highlight_groups': ['cpu_temp_gradient', 'cpu_temp'],
            'divider_highlight_group': 'background:divider'
        }
    ]
