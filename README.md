# awsovpn

Manage an OpenVPN instance in your private EC2 cloud using this script. 


## Usage

Create an OpenVPN EC2 instance and configure it for VPN access:

```bash
awsovpn up
```

Terminate the OpenVPN EC2 instance and remove all EC2 resources mangaed by this script:

```bash
awsovpn down
```



## Installation

Install via pip

```bash
pip install awsovpn
```

## Configure

### Method 1: awscli configuration

If you have [awscli](https://aws.amazon.com/cli/) installed and configured, then awsovpn can utilize this same configuration. Just use `--profile PROFILE` to specify an AWS configuration profile. 

```bash
awsovpn --profile myprofile up
``````

### Method 2: environment variables

Create a `.env` file or set the following environment variables: 

```text
AWS_REGION=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_PROFILE=
```

### Method 3: use arguments

You can also pass credential configuration as arguments:

e.g.

```bash
awsovpn --region REGION --access-key-id ACCESS_KEY_ID --secret-access-key SECRET_ACCESS_KEY
```



## Development

Regenerate requirements.txt form requirements.in

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

Install the package in 'edit' mode. Now you can invoke the package using the name `word` as defined by `setup.py`.

```bash
pip install -e .
```


### Publish to PyPi

```bash
python3 -m pip install --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
```
