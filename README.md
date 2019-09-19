### Change owner of S3 objects

The solution is a POC for following 
##### Problem statement:
Let's consider - there are 3 AWS account.
`Account A` is the owner of a S3 bucket called `demo-bucket`
`Account B` has permission to write data into (say, 1 million objects)`demo-bucket` of `Account A`
Now `Account C` is intended to read the data from `demo-bucket`.

Since, `Account B` writes the data into `demo-bucket`, so they become the owner of the data. Where as `Account A` is the owner of the bucket but it can not provide access to objects of the bucket to `Account C`, since it's not the owner of objects.

##### Solution
The problem can be solved by several ways, here is one solution how it can be achievable using AWS lambda.

In `Account A` we can run lambda function which will copy the object from one directory to other directory inside the same bucket or we can copy it completely different bucket. In this solution - I have used different bucket. 
So, when the objects will land into `demo-bucket`, the objects will be copied into another bucket `demo-bucket-1`. Now `Account A` is the owner of bucket and each object inside bucket. So you can control the access through bucket policy. The access can be granted to N no. of accounts through bucket policy.
