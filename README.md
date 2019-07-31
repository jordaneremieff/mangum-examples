# mangum-example

**Work in Progress / Experimental**

An example [Mangum](https://github.com/erm/mangum) deployment of a [Starlette](https://starlette.io) application that uses [asgi-s3](https://github.com/erm/asgi-s3) to serve static files.

**Requirements**: Python 3.7+


## Tutorial

### Step 1 - Install the requirements

```shell
python3.7 -m venv venv
. venv/bin/activate
pip install mangum[full] asgi-s3
```

**Note**: This repository contains a `requirements.txt` that is for the application build, the steps above are for creating the local virtual environment that includes the CLI dependencies.

### Step 2 - Create an S3 bucket for the static files

The static files will be served using a middleware provided in `asgi-s3`, this package also includes some command-line tools for creating and syncing the static files bucket.

Running the following command will create a new S3 bucket (optionally you may specify a bucket name and region):

```shell
s3 create-bucket
```

Note the bucket name and region name returned in the output and create a new file `.env` in the config directory:

```shell
# Don't commit this to source control.
# Eg. Include ".env" in your `.gitignore` file.
BUCKET_NAME=bucket-name
REGION_NAME=region-name
```

Replacing the `bucket-name` and `region-name` values with the details from the command output.

### Step 3 - Create a new deployment configuration
    
Run the following command to answer a series of questions about the project to define a new configuration:

```shell
mangum init
```

**Note**: An S3 bucket will be required for storing the packaged application. An existing S3 bucket name may be provided, otherwise one will be generated.


For this tutorial, enter the following when prompted for the first two questions (use defaults for the rest):

```shell
Enter the name of the directory containing the project code: app
Enter a name for the project: mangum
```

After defining the configuration a `config.json` file will be generated, the current directory should now look this:

```shell

├── app
│   └── static
│   └── templates
│   └── asgi.py
├── .env
├── config.json
└── requirements.txt
```


### Step 4 - Create a local build

Run the following command to create a local application build:

```shell
mangum build
```

This will create a `build/` directory containing the application code and any dependencies included in `requirements.txt`.

### Step 5 - Package the local build

Run the following command to package the local build:

```shell
mangum package
```

This wraps the AWS CLI's `package` command, it uses the definitions in `config.json` to produce a `packaged.yaml` file and a `template.json` file.

### Step 6 - Sync the static files

Run the following command to sync the static files with the S3 bucket created previously:

```shell
s3 sync-bucket <bucket-name> <static dir>
```

### Step 6 - Deploy the packaged build

Run the following command to deploy the packaged build:

```shell
mangum deploy
```

This wraps the AWS CLI's `deploy` command. It may take a few minutes to complete. If successful, the endpoints for the deployed application will be displayed in the console:

![Console](https://raw.githubusercontent.com/erm/mangum-example/master/docs/images/deployed.png)

Then enter the endpoint from the console into your browser to see:

![Page](https://raw.githubusercontent.com/erm/mangum-example/master/docs/images/page.png)

