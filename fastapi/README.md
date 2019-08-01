# FastAPI example

A basic FastAPI application deployed to AWS Lambda & API Gateway.

### Step 1 - Install the requirements

```shell
python3.7 -m venv venv
. venv/bin/activate
pip install mangum[full]
```

### Step 2 - Modify the deployment configuration

A new `mangum.yml` config can be created using the `mangum init`, however this example already includes a `mangum.yml` file that may be edited, a `bucket_name` and a `region_name` will need to be defined:

```yaml
name: myapp
code_dir: app
handler: asgi.handler
region_name: ap-southeast-1
bucket_name: my-bucket-name
timeout: 300
```

### Step 3 - Create a local build

Run the following command to create a local application build:

```shell
mangum build
```

This will create a `build/` directory containing the application code and any dependencies included in `requirements.txt`.

### Step 4 - Package the local build

Run the following command to package the local build:

```shell
mangum package
```

This wraps the AWS CLI's `package` command, it uses the definitions in `mangum.yml` to produce a `packaged.yml` file and a `template.yml` file.

### Step 5 - Deploy the packaged build

Run the following command to deploy the packaged build:

```shell
mangum deploy
```

This wraps the AWS CLI's `deploy` command. It may take a few minutes to complete. If successful, the endpoints for the deployed application will be displayed in the console:

![Console](https://raw.githubusercontent.com/erm/mangum-example/master/docs/images/deployed.png)

Then enter the endpoint from the console into your browser to see:

![Page](https://raw.githubusercontent.com/erm/mangum-example/master/docs/images/fastapi_page.png)
