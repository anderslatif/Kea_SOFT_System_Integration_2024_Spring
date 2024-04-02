
<div class="title-card" style="color: cyan;">
    <h1>Infrastructure as Code (IaC)</h1>
</div>

---

# Ways to work with cloud services

From okay to best:

1. Console UI (Clicking)

2. CLI / API (Shell, Bash)

3. SDK/CDK (Software/Cloud Development Clip) (Custom code scripts in programming languages)

4. IaC (Framework for provisioning of resources, Declarative, Prescriptive)

Pros and cons of each?

---

# Ways to work with cloud services - Pros and cons

| Method    | Cons                                                   | Pros                                                                                             |
|-----------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Console UI| Not suitable for scaling, prone to manual errors       | Quick setup for experiments, easy access to resources for immediate management                   |
| CLI / API | Requires scripting for automation, potential for script-based errors | Flexible for both development and production environments, enables automation and integration    |
| SDK/CDK   | Need for coding skills, potential overhead for setup and maintenance | Facilitates complex deployments, integrates seamlessly with existing development workflows        |
| IaC       | Requires understanding of syntax and structure, overhead in template management | Ensures consistent environments, ideal for both development and production, supports CI/CD processes |

The table is sorted by the least ideal option first. Why not just always choose IaC then?

---

# Best method is...?

The further down the list we go:

* the steeper is the learning curve. 

* the time sink to get started grows larger.

---

# Suggestion: Try out a positive mindset just for today

What I am introducing today is hard. 

You will be tested as programmers on your general philosophy when facing hard challengnes. 

Do you find joy in the challenge, smiling when things don't work simply because you've uncovered an intriguing problem to solve?

My goal is to equip you for a real complex problem that you might face at larger companies. 

> Embrace the complexity, for it's in the toughest challenges that the most rewarding growth occurs.

---

# Motivational

No one says infrastructure would be easy but...

We **desire** it for the *reproducibility, scalability, maintainability and consistent infrastructure across environments.* that it promises.

...and hopefully, it will prove to be worth every drop of sweat in the end. 

IaC is for developers who excel in the face of challenges and relish the opportunity to solve complex problems.

Stay motivated; problems and roadblocks are stepping stones to mastery.

---

# The disaster scenario

Imagine that your entire infrastructure is destroyed. 

It could happen because of a disgruntled employee or due to multiple types of accidents. 

As a company you should ask yourself:

- how prepared you are for the disaster scenario. 

- how long will it take you to recover?

In the past, there are many cases of companies being forced into bankruptcy because they couldn't recreate years of work in time to gain lost revenue from failing infrastructure.

IaC aims to solve that. It is a lot of  work but worth the hassle. 


---

# Why IaC?

* Cross-platform

* Sandboxing

* Testability

* Version control your infrastructure and add comments to it

* Reproducibility (the works on my machine problem)

* Indempotency

---


# X as Code

<div>
    <img src="./assets/X_as_Code.png" alt="X as Code" style="height: 40vh;"/>
</div>


Context: GitOps

Source: https://youtu.be/f5EpcWp0THw?list=PLy7NrYWoggjxKDRWLqkd4Kbt84XEerHhB&t=49

---

<!-- todo finish and add image and links -->

# IaC tools - Cloud Provider Specific - I

**Azure**

Bicep: A domain-specific language for declaratively deploying Azure resources.

Azure Resource Manager (ARM) Templates: A service provided by Microsoft Azure to deploy and manage Azure resources in a consistent manner using JSON templates.

**AWS**

AWS CloudFormation: An AWS service that gives developers and businesses an easy way to create a collection of related AWS and third-party resources, provision and manage them in an orderly and predictable fashion.

---

# IaC tools - Cloud Provider Specific - II

**Google Cloud**: 

Google Cloud Deployment Manager: A service provided by Google Cloud that enables the management of cloud resources using declarative templates.

---

# IaC tools - Cloud Provider Agnostic - I

We are interested in a tool that isn't too proprietary and which doesn't bolt us down to a certain cloud provider. 

Very large companies use several cloud providers as once. Only these tools can manage that setup:

[Terraform](https://www.terraform.io/): Define cloud and on-prem resources with versionable files.

[Pulumi](https://www.pulumi.com/): Infrastructure as code in general-purpose languages like JavaScript, Python, etc.

[Serverless Framework](https://www.serverless.com/): Uses declarative YAML to define services with support for many cloud providers. 

<span style="font-size: small;">Note: Not to be confused with serverless functions or the concept of a serverless cloud service.</span>


---

# IaC tools - Cloud Provider Agnostic - II

[Ansible](https://www.ansible.com/): Automates cloud provisioning and config management with YAML.

We will pick Terraform for being the most widely used of all.

---

# IaC tools - The definition of IaC

But a quick note about the definition of IaC and how we use it:

1. [Broad_Definition] IaC: Any tool that allows us to define something related to our infrastracture as code.

Example: 

Configuration Management Tools are also called IaC eventhough their focus is on what to do once the resource has been provisioned. 

Configuration Management Tools are listed and discussed [in a later section](#configuration-management-tools).

2. [Narrow_Definition] IaC: A specific type of tool that allows us to provision cloud resources.

Even though `1` is technically correct definition which encompassess `2`, from here on out, I will colloquially use IaC in the narrow sense of definition `2`;

Ansible is the exception, it can do both. 

<span style="font-size: small;">While we are on the topic of definitions: Provisioning translates best to "Oprettelse" or "Udrulning".</span>

---

# Terraform

Maintains a dependency graph which is useful to know what order to create or destroy in. 

Keeps track through a state through the Terraform state file.

Collaborate and keep track of changes to your infrastructure in VCS. 

Declarative: Define the infrastructure you want, it manages how to achieve that.

---

# Declarative vs. Prodcedural - Procedural example

Bash example

```bash
#!/bin/bash
mkdir logs
INSTANCE_ID=$(aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --query 'Instances[0].InstanceId' --output text)
echo "Instance ID: $INSTANCE_ID" > ./logs/logs.txt
```

Find the the problem above?

---

# Problem: Indempotency

> Wikipedia: Idempotence is the property of certain operations […] whereby they can be applied multiple times 
without changing the result beyond the initial application.

https://en.wikipedia.org/wiki/Idempotence

If the scripts fails then you have to restart from scratch.

If one thing fails then everything fails. In this case we didn't think to check if the folder already exists. 

In the declarative approach we don't have to concern ourselves with all the edge cases that might happen.

---

# Declarative vs. Prodcedural - Declarative example


Terraform (HCL) example:

```terraform
resource "aws_instance" "example" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
  }
```

We just write what we want. 

Continues where it left off even despite potential failures in the middle of the process.

---


# HCL (HashiCorp Configuration Language)

Terraform can be defined as either HCL or JSON. But HCL is commonly used because it is:

* Descriptive: Aims to be a readable JSON-like alternative to JSON

Generally about HCL, it is:

* A domain-specific langauge designed for IaC.
* Declarative: Focused on the desired end state
* Non-Imperative: Specifies 'what' is needed, not 'how' to accomplish it.
* Idempotent: Applying the same configuration multiple times results in the same state, without unintended side effects.

---

# Declarative vs. Prodcedural - Pros and cons

| Aspect       | Declarative                                     | Procedural                                     |
|--------------|-------------------------------------------------|------------------------------------------------|
| **Focus**    | What the end state should be.                   | How to achieve the end state.                  |
| **Idempotency** | Naturally idempotent, can be applied multiple times with the same outcome. | Requires careful scripting to achieve idempotency. |
| **Ease of Use** | Higher level of abstraction, easier for defining complex infrastructure. | Requires detailed step-by-step scripting, potentially more complex for large infrastructures. |


---





<div class="title-card" style="color: cyan;">
    <h1>Finally hands-on!</h1>
</div>


---

# Install Terraform

https://developer.hashicorp.com/terraform/install?product_intent=terraform

Success criterion: You can run the following and see the version number:

```bash
$ terraform --version
```

---

# Install and log in to `az`

`az` is the Azure CLI. By logging in locally Terraform can get access to our cloud.

https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build

```bash
$ az login
```

Verify the login:

```bash
$ az account show
```

---

# About the Azure CLI

Allows you to Interact with Azure directly through the terminal. 

You never have to use the portal again!

New Feature! Azure CLI interactive mode:

[![Azure CLI Interactive mode](http://img.youtube.com/vi/GqpwiyYsNIw/0.jpg)](https://youtu.be/GqpwiyYsNIw?t=663)

---

# Clarification: Terraform under the hood

Though possible to provision everything through `az`, this is not how Terraform does it.

Terraform uses `az` to generate a user token for authorization.

This token is used to validate against what they call [Azure REST APIs](https://learn.microsoft.com/en-us/rest/api/azure/).

---

<div class="title-card" style="color: cyan;">
    <h1>First Terraform project - Let's test it out</h1>
</div>

---

# Let's create our first Terraform project

In an empty folder run:

```bash
$ terraform init
```

It complains about a missing configuration file. Let's create `main.tf`. Then run init again.

---

# .tf files and VSCode Extensions

The `.tf` file extension is used for Terraform. In VSCode there are extensions for syntax highlighting and Intellisense. 

The official one by Hashicorp seems to be universally hated. Instead, consider the one that is rated higher.

---



<div class="title-card" style="color: cyan;">
    <h1>Terraform Workflow</h1>
</div>


---

# Terraform workflow - I

<img src="./assets/terraform_workflow_1.png" alt="Terraform workflow stages" style="height: 45vh;">

Source: https://developer.hashicorp.com/terraform/tutorials/azure-get-started/infrastructure-as-code

---

# Terraform commands - overview

| Command                | Description                                          |
|------------------------|------------------------------------------------------|
| `terraform init`       | Initializes a Terraform configuration directory. Prepares your directory for other commands, installs necessary providers. |
| `terraform plan`       | Shows a preview of the actions Terraform plans to take based on the configuration files. Useful for reviewing changes before applying them. |
| `terraform apply`      | Applies the changes described by `terraform plan`. Provisions or updates infrastructure according to the Terraform configuration. |
| `terraform destroy`    | Removes all resources defined in the Terraform configuration, tearing down the managed infrastructure. |
| `terraform fmt`        | Automatically formats Terraform configuration files to a canonical format and style. |
| `terraform validate`   | Validates the syntax of the Terraform configuration files for correctness. |
| `terraform output`     | Displays the output variables defined in the configuration, useful for extracting important information like IP addresses. |
| `terraform refresh`    | Updates the local state file against real-world resources, realigning the state with the actual state of resources in the cloud. |
| `terraform import`     | Brings real-world infrastructure into Terraform management by adding it to the Terraform state file. |
| `terraform workspace`  | Manages different workspaces, allowing for managing separate states for the same configuration, useful for different environments (e.g., staging, production). |


---


# Terraform workflow - II

Let's look at the table again. 

Can you spot a command and guess which stage they relate to?

<img src="./assets/terraform_workflow_2.png" alt="Terraform workflow stages">

Source: https://developer.hashicorp.com/terraform/intro


---


# Terraform commands - Prepare

Run `terraform init` in an empty folder. Only need to run init once after the provider has been defined: 

```bash
$ terrraform init
```

Running validate before you apply is optional. This will tell you if your code is valid:

```bash
$ terrraform validate
```

Even more optional than validate. `fmt` will format your code and change indentation etc. to its preference. 

```bash
$ terrraform fmt
```

---

# Terraform commands - Apply

See the changes that will occur before applying them:

```bash
$ terrraform plan
```

Running apply will give you an overview once again. Type `yes` to enact them:

```bash
$ terrraform apply
```

Once finished look for this line and the numbers instead of X, Y, Z:

```
Apply complete! Resources: **X** added, **Y** changed, **Z** destroyed.
```

---

# Terraform commands - Inspect

See the changes that will occur before applying them:

```bash
$ terrraform show
```

Running apply will give you an overview once again. Type `yes` to enact them:

```bash
$ terrraform apply
```

---

# Terraform commands - Destroy

This will tear down your cloud services. 

```bash
$ terrraform destroy
```

As mentioned earlier, the smart thing about Terraform is that they take care of the dependency graph 
and will shut down services in the necessary order. 

---

# The Files of Terraform:

| File Type              | Description                                           |
|------------------------|-------------------------------------------------------|
| `*.tf` / `*.tf.json`   | Infrastructure definitions in HCL or JSON.            |
| `*.tfvars` / `*.tfvars.json` | Variable definitions for configurations.                |
| `.terraform.lock.hcl` | Tracks provider versions and dependencies.            |
| `outputs.tf`           | Defines output values from Terraform.                 |
| State Files (`terraform.tfstate`, `terraform.tfstate.backup`) | Maps configurations to real-world resources.            |

---

<div class="title-card" style="color: cyan;">
    <h1>Terraform Example 1 - Create a bare minimim configuration for a virtual machine </h1>
</div>

---


# Let’s get started

Create a new repo with Terraform as the .gitignore template

In the root directory create a `main.tf` file (by hand).

Initialize the current directory as a Terraform project:

```bash
$ terraform init
```

---

# Add `azurerm` as the provider

Azurerm = Azure Resource Manager. This tells Terraform that we want to deploy to Azure specific services. 

https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs

Click on USE PROVIDER:

<div>
    <img src="./assets/azurerm.png" alt="Azure provider for terraform azurerm" style="height: 33vh;"/>
</div>



---
<div class="title-card" style="color: cyan;">
    <h1>Terraform Workspaces</h1>
</div>

---

# Workspaces

Similar to branches. Each workspace is its own context. 

Type the following to see the possible optionsÆ

```bash
$ terraform workspace
```

Let's try to create, switch between and delete workspaces together.

---

# Why workspaces in Terraform?

Consider why...

---

# Why workspaces in Terraform?

Each workspace, when selected, maintains its own state, allowing for isolated management of resources.

The state is kept in `terraform.tfstate`file inside of the  `terraform.tfstate.d` directory. 

Try to observe how the file changes as you switch between workspaces. 

It requires a project where you have actually provisioned rsources. 

---

<div class="title-card" style="color: cyan;">
    <h1>Terraform - Advanced concepts</h1>
</div>

--- 

# Suggestion: Use auto-complete and/or alias as tf

These are suggestions you might consider to make your life easier while working with Terraform.

1. Suggestion: Install terraform auto-complete 
<!-- terraform -install-autocomplete -->

https://developer.hashicorp.com/terraform/tutorials/azure-get-started/install-cli#enable-tab-completion

2. Suggestion: Alias the `terraform` command so that you can invoke it by simply typing `tf`.

A sufficient amount of professional developers seem to be doing for it to make sense.

***nix**: add this to your terminal's RC file (could be ~/.bashrc, ~/.zshrc):`alias tf="terraform"`

**Windows**: Create a terminal profile if it doesn't exist, in either case open it

```powershell
$ if (!(Test-Path -Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
notepad.exe $PROFILE
```
You can now manually add this line to it and save:

```text
Set-Alias -Name tf -Value terraform
```







---

# Variables in Terraform

<!-- todo study the envvars image in this folder and create multiple slides -->

---

# Keep secrets

Put Terraform code in VCS but take out the secrets and store them elsewhere . 

HashiCorp vault:

https://www.hashicorp.com/products/vault

Azure has:

Azure Key Vault

Github Secrets:

---


<div class="title-card" style="color: cyan;">
    <h1>A peek into a real-world challenge that you might face in the future</h1>
</div>

--- 

# The state file

A reminder about the Terraform state file:

- Stored locally.

- Always in JSON. 

- Named terraform.tfstate

Is used to:

* keep track of references to existing resources 
* maintain the dependency graph between services

It is stored locally by default, though everyone in a team should have the latest version.

---

# Why using a VCS is no good

You should not push the state file into git because it risks:

* mergeing two versions of the file incorrectly, resulting in an invalid file.

* exposing secrets about your system which can compromise security.

---

# The state file - The glaring problem

The state file must be up to date when running `terraform apply`, otherwise "state drift" will lead to big problems. 

If a change happens outside of Terraform then state drift can be ammened with `terraform refresh`.

A **major** downside with Terraform is how there ufortunately is no standardized way to deal with state file. 

Note: This problem is easily solved with coordination in your groups but let's look at how they deal with them in large companies. But you might face this problem after convincing your next job to try out Terraform. 

---

# The state file - Potential problems

These problems occur in large SRE or operations teams:

**Locking**

Ensures single concurrent access. 

**Version Consistency**

Ensuring users apply changes against the latest state version.

**Provide a write mechanism**

Consider a CI/CD pipeline where runners are destroyed after use. If the pipeline updates the infrastructure then it should be able to save the state changes.

---

# Common Solution - Using cloud storage with lock support - I

Storing it only solves half of the problem. 

A full solution must provide a locking mechanism so that only 1 developer can change the same workspace at a time. 

Though any cloud storage solution that provides a locking mechanism could do (might require some scripting to call lock and unlock) consider what it would mean to you if a state file remains locked because of an error. 

---

# Common Solution - Using Cloud Storage with Lock Support - II

- [Terraform Cloud](https://www.hashicorp.com/products/terraform?product_intent=terraform)

- [Google Cloud Storage](https://cloud.google.com/docs/terraform/resource-management/store-state)

- AWS S3 with DynamoDB (for lock handling)

- [Azure Storage Account](https://learn.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage?tabs=azure-cli#4-understand-state-locking)

Remember that the problem is that there is no standardized, agreed-upon way to solve this issue. 

---

# How other IaC tools deal with state

What sets the competing IaC tools apart is how they deal with state. 

One example is Bicep which stores its state files entirely in cloud by default. 

Downside: Then you are locked into using Azure as your cloud provider. 
 

| IaC Tool    | State Management                                  | Default Storage               | Self-manage Options              |
|-------------|---------------------------------------------------|-------------------------------|----------------------------------|
| Terraform   | Causes the problems we have seen                  | Local filesystem              | AWS S3, Azure Blob, GCS, etc.    |
| Pulumi      | Cloud-based with history, auditing, rollbacks     | Pulumi Service (Cloud)        | Local, AWS S3, Azure Blob, GCS   |
| Chef        | Stores state as attributes on Chef server         | Chef Server                   | Local mode, Chef Automate        |
| Puppet      | Compiles catalogs representing desired state      | Puppet Master/Server          | Local filesystem, PuppetDB       |


But Terraform is [still the most used IaC tool](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-other-tools) and an industry standard. 

---



<div class="title-card" style="color: cyan;">
    <h1>Terrafform - Limitations and downsides</h1>
</div>


---

# Limitation for us, students

Azure for Students intentionally doesn't support the creation or management of a **Service Principal**.

[Learn more])https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret)

Creating a Service Principal would allow us to programatically authenticate ourselves instead of using `az login` which opens a browser.

If only... Then we would be able to run Terraform in CI. For instance, a Github Action that uses Terraform to automatically provision a new test environment for every build on a speocific branch. That would be **close to pro**!

---


# Limitations - What Terraform is not

When you have a fresh VM what is it that you always do? Upgrade, install, setup etc.

Terraform only provisions cloud services and does not change the internal state of VMs for instance. 

Several tools that promises indempotency in this regard exist...

Can you think of use cases where one might prefer to use Configuration Management Tools?

---

# Top 5 Configuration Management Tools - I

<table>
  <tr>
    <td><img src="./assets/logos_configuration_management_tools/ansible_logo.png" alt="ansible logo" style="height:5vh;"><br><a href="https://www.ansible.com/">Ansible</a><br>Automates cloud provisioning, configuration management, and application deployments.</td>
    <td><img src="./assets/logos_configuration_management_tools/puppet_logo.png" alt="puppet logo" style="height:5vh;"><br><a href="https://www.puppet.com/">Puppet</a><br>Manages infrastructure as code, providing automation and deployment capabilities.</td>
    <td><img src="./assets/logos_configuration_management_tools/chef_logo.png" alt="chef logo" style="height:5vh;"><br><a href="https://www.chef.io/">Chef</a><br>Turns infrastructure into code to automate server deployment and configuration.</td>
  </tr>
  <tr>
    <td><img src="./assets/logos_configuration_management_tools/salt_logo.png" alt="salt logo" style="height:5vh;"><br><a href="https://saltproject.io/">Salt</a><br>Offers powerful automation, orchestration, and configuration management in one.</td>
    <td><img src="./assets/logos_configuration_management_tools/CFEngine_logo.png" alt="CFEngine logo" style="height:5vh;"><br><a href="https://cfengine.com/">CFEngine</a><br>Provides automated configuration and maintenance of large-scale IT systems.</td>
  </tr>
</table>

Ordered by most popular first


---

# Reflect on Configuration Management Tools 

I've only worked with Ansible, personally. 

What do you think the benefits for configuration management tools are? 

---

# Benefits of configuration management tools

- **Automation**: Reduces manual effort and errors.
- **Time Saving**: Does not require a person to react to different outcomes.
- **Consistency**: Ensures uniform configurations across environments.
- **Scalability**: Manages large-scale infrastructure efficiently.
- **Version Control**: Track changes via versioning.
- **Security**: Enforces security policies and standards.
- **Recovery**: Aids in quick disaster recovery.
- **Collaboration**: Enhances DevOps collaboration.

---


# Limitation: Why is Terraform so slow?

It is true that Terraform can hog your computer's resources.
But know that the heavy lifting happens on the cloud provider's side. 

It might feel sluggish but it is because it takes time for Azure to provision or tear down new resources.

Consider the alternative of having to manually provision services a hundred times! Or how before cloud it took days if not months to get new hardware approved, purchased and then setup.

But it's a nice exercise to dream up a future where IaC tools are easier and everything is faster. What would your dream IaC tool be like? If any, what would the syntax be like? How would it work?


---

# Conclusion

Discuss: Running Terraform wasn't easy so why is it still worth it? 
