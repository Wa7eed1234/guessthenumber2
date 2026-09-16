# Number sequence exercise

Console exercise that prints the next value in [2, 23, 34], or a random list member for another input.

## Run locally

Use Python 3. From the repository directory:

```bash
python main.py
```

No third-party Python packages are imported by this example.

## Current status and known limitations

Input 34 causes IndexError; decide wraparound or an explicit last-item message. Handle non-integer input.

## Review status

Documentation drafted from repository source on 13 September 2026. This review did not run the application or certify it for production.

## Cleanup applied

- Last item wraps to the first; invalid integer input handled.

These updates supersede the corresponding original review findings. Other limitations remain open.
