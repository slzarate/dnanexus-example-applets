This example shows packaging a precompiled binary in the `resources/` directory of an app(let).

## Options for Precompiling Binary
In this applet, the SAMtools binary was precompiled on an Ubuntu 14.04 machine. A user can do this compilation on an Ubuntu 14.04 machine of their own, or can utilize the Cloud Workstation to build and compile a tool. On the Cloud Workstation, the user has full access to download the SAMtools source code and compile in the worker environment, ensuring the binary will run on future workers.

See [Cloud Workstation](https://wiki.dnanexus.com/Developer-Tutorials/Cloud-Workstations) for more information.
## Resources Directory
The SAMtools precompiled binary is placed in the `<Applet dir>/resources/` directory. Any files found in the `resources/` directory will be packed, uploaded to the platform, and then unpacked so that they will be present in the root directory of workers. In our case:
```
├── Applet dir
│   ├── src
│   ├── dxapp.json
│   ├── resources
│       ├── usr
│           ├── bin
│               ├── < samtools binary >
```
When this applet is run on a worker the `resources/` directory will be placed in the worker's root `/`:
```
/
├── usr
│   ├── bin
│       ├── < samtools binary >
├── home
│   ├── dnanexus
│   	├── applet script
```
We are able to access the SAMtools command because the respective binary is visible from our `$PATH`
`/usr/bin/` is part of the `$PATH` variable, so in our script, we can reference the samtools command directly, <!--SECTION: Run samtools view -->


See [The resources/ directory and its use](https://wiki.dnanexus.com/Developer-Tutorials/App-Build-Process#The-resources/-directory-and-its-use) for more information.

<!-- INCLUDE: ## Applet Script -->
<!-- FUNCTION: FULL SCRIPT -->