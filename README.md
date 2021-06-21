# BBC Weather Script & CI

Deploy a lambda to return current temperature in Lerwick, Shetland.


### Important!
Please have **AWS CREDENTIALS** ready.

### For Local Development
Go to **./services/service/README.md** for local development process.


## Environment

This project uses...
- [yarn](https://classic.yarnpkg.com/lang/en/) (v1.22.10) For dependencies management together with

- [Lerna](https://lerna.js.org/) (v3.22.1) for monorepo management.

- [python](https://www.python.org/about/gettingstarted/) (v3.8) For AWS Lambda scripting.

- [docker](https://docs.docker.com/get-started/) (v19.03.8) For local development. 

- [github-actions](https://docs.github.com/en/actions) For CI/CD pipeline.


## File Structure
```
/
├─ .github/                     - github action as ci/cd
    └─ workflows/               - directory for different ci/cd pipelines
        └─ deploy.yaml          - ci pipeline for each commit [main]
└─ services/
    ├─ common/                  - common services used by micro services
    └─ service/                 - deploys cloud service
        └─ src/                 - scripts for lambda function
        └─ tests/               - unit tests for scripts
    └─ config.yml               - common configuration for services
```


## Set Credentials for Local Deployment

```bash
export AWS_PROFILE="<PROFILE_NAME>"
```

## Add Secrets on Github Repository for CI/CD

 - AWS_ACCESS_KEY_ID
 - AWS_SECRET_ACCESS_KEY

## Install Dependencies

Install `yarn` globally:

```bash
npm i -g yarn
```

In root of the project install dependencies:

```bash
yarn run install
```

## Usage

### Deploy

- Default Region = *eu-west-1*
- Default Stage = *dev*

- CI Region = *eu-west-1*
- CI Stage = *test*

```bash
yarn run deploy [--region | --r <REGION>] [--stage | --s <STAGE>]
```

### *Check serverless output for function **endpoint** and **name***

### Run

```bash
curl -X GET https://<API_ID>.execute-api.<REGION>.amazonaws.com/
```

### Remove:

```
yarn run remove [--region | --r <REGION>] [--stage | --s <STAGE>]
```
