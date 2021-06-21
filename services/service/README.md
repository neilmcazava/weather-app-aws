# BBC Weather Script & CI
This directory involves the script for the function and the development process.

## Setup Local Development

Have Docker running.

### Create environment

```bash
python3 -m venv env
```

### Activate environment

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Run Locally

```bash
yarn run invoke-local --function api
```

### Deactivate environment

```bash
deactivate
```

## Unit Tests

### Run

```bash
yarn run test
```

## To Deploy Service

- Default Region = *eu-west-1*
- Default Stage = *dev*

- CI Region = *eu-west-1*
- CI Stage = *test*

```bash
yarn run deploy [--region | --r <REGION>] [--stage | --s <STAGE>]
```

## Invoke Deployed Function

```bash
yarn run invoke --function api [--region | --r <REGION>] [--stage | --s <STAGE>]
```

## View Logs

```bash
yarn run logs --function api [--region | --r <REGION>] [--stage | --s <STAGE>]
```
