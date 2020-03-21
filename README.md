# PWN-Prod - v0.1
## Description
A CLI client that automates the process of poking and prodding at a binary to find patterns in input behavior
## Usage
### Example
`python3 [-l | -r] [PROCESS] -c [CHARLIST]`
### Arguments
```
-l, --local - takes one argument specifying the path of the local process to prod
-r, --remote - takes two arguments specifying the url and the port of the process to prod
  Either -l or -r must be used. They are mutually exclusive and required.
-c, --characterlist - optional, defaults to ./strings/common-chars.txt, specifies the path of the newline (\n) delimited list to pwn with
```