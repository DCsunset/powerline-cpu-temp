# powerline-cpu-temp

`powerline-cpu-temp` is a Powerline segment to show CPU temperature.

## Installation

Using pip:

```
pip3 install powerline-cpu-temp
```

Or clone this repository and run:

```
python3 setup.py install
```

## Usage

First, it is required to add `cpu_temp` and `cpu_temp_gradient` highlight groups in the colorscheme configurations:
(You can easily customize the color scheme by changing the highlight group settings.)

```json
{
	"cpu_temp": { "fg": "gray8", "bg": "gray0", "attrs": [] },
	"cpu_temp_gradient": { "fg": "green_yellow_orange_red", "bg": "gray0", "attrs": [] }
}
```

Then add the following settings to the Powerline configuration file:

```json
{
	"function": "powerline_cpu_temp.cpu_temp"
}
```

You can specify the arguments:

```json
{
	"function": "powerline_cpu_temp.cpu_temp",
	"args": {
		"format": "{value:.0f}°C",
		"threshold_good": 50,
		"threshold_bad": 90
	}
}
```

Available arguments:

* `format`(`string`): format string, receives `value` as an argument

* `threshold_good` (`float`): threshold for gradient level 0:
temperature below this value will have this gradient level.

* `threshold_bad` (`float`): threshold for gradient level 100:
temperature above this value will have this gradient level.
Temperature between `threshold_good` and `threshold_bad` receive gradient level that indicates relative position in this interval:
(`100 * (cur-good) / (bad-good)`).

## Dependencies

* [psutil](https://github.com/giampaolo/psutil)
