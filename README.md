# aws_profiles.py

This application selects from a list of AWS named profiles and sets your environment
up correctly. Assumes the aws profiles are in $HOME/.aws/credentials and in the
AWS ini config file standard.
This is useful when you have a lot of named profiles and cant remember thier names

See AWS Named Profile documentation for information about .aws/credentials
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

## Prerequisites
* bash
* python 3+
* `pick` python library installed
* AWS named profiles configured in $HOME/.aws/credentials

## Usage

Pretty simple right now. 

./aws_profiles.py

## TODOs 

Pull requests are welcome. Here are a few things we could do

1. Get a better tty (currently limited to 80 chars wide)
2. Allow this tool to create new and/or configure existing profiles
3. Expand the list of regions from the pick list.. Maybe make dynamic with `aws
	 ec2 describe-regions`
4. Change the $PS1 prompt so that we can remember which profile we're using
5. Integrate with saml2aws if configured to prompt for credentials if required
6. Adapt this for use with non unix/bash systems


## Example usage
```
./aws_profiles.py

 Select an AWS profile

   css-aws1
   css-lab1
*  css-lab2

 Select an AWS region

 * us-east-1
   us-east-2
   us-west-1
   us-west-2
```

Now our environment should be configured
```
$ env | grep AWS
AWS_PROFILE=css-lab2
AWS_DEFAULT_REGION=us-east-1
```

And we can run AWS commands
```
$ aws s3 ls
2018-04-05 14:34:14 cf-templates-1q7XXXXst6s-us-east-2
2018-04-05 14:29:49 trax-terraform-state-e3XXX7a
```

And when we are done, just exit the shell
```
$ exit
```

# aws_clear.py

wipes out the contents of the saml profile from ~/.aws/credentials
It's sort of a logout function for saml2aws
