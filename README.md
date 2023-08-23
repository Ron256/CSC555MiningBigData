# CSC555MiningBigData

This repository houses the Introduction to fundamentals of distributed file systems and map-reduce technology (e.g., Hadoop) projects; tuning map-reduce performance in a distributed network. Algorithms and tools for mining massive data sets and discussion of current challenges. Applications in clustering, similarity search, classification, data warehousing (e.g., Hive), machine learning (e.g., Mahout)

There are projects implemented in each of the above topics of distributed file systems and map-reduce technology. 

Assignment 1 focused on:

1. on understanding the replication factor and storage cost of a file in Hadoop Distributed FileSystem.

2. I then wrote python code to read a text file and computed a total word count using a dictionary.

3. Created a subroutine function that created three different word count dictionaries, splitting the words at 
randoms between the three dictionaries. Each time a word was processed,  chose at random which word count dictionary to add to it, which meant that some words would appear in multiple dictionaries simultaneously.

4. Wrote a python code to merge the three dictionaries into one and verified that it matched the dictionary in 2 above.


5. Wrote a python code that would deterministically assign each word to one of the three dictionaries.

6. Using urllib, wrote a python code that measured the speed of reading from the web and writing to a file on the local file system. The code reads and writes some amount of data, time the operation and computes the read or write rate (in MBytes/sec)

Assignment 2 focused on:

1. describing the implementation of a MapReduce job using either my own words or pseudo code.

2. Understanding the Fail-over-recovery of a Mapper task

3. Understanding the execution of a job with the use of reducers.

4. Understanding how Hadoop Worker nodes function

5. Setup a Hadoop cluster of one node on AWS.

6. Copied files to HDFS for processing.

7. Used HIVE to run a few queries over the Hadoop framework. 

Assignment 3 focused on:

1. Describing the implementation of the SQL queries in MapReduce.

2. Creating HIVE tables

3. Creating a Python transformation function used to load the HIVE table

4. HIVE Scripts to load the HIVE tables.

5. Downloading and installing Pig

6. Using Pig to load HDFS files.

Assignment 4 focused on:

1. Implementation of the SQL queries using Hadoop Streaming.

2. Downloading and installing HBase

3. Creating HBase tables on top of the HDFS.

Assignment 5 focused on:

1. Understanding Key-Value store, Column-oriented store, Document-oriented store, graph database, relational databases, streaming engine.

2.Computing the page rank for the nodes in this graph.

3. Creating a custom Map Reduce job by converting the custom SQL queries into Map Reduce by implementing a JoinMapper and Reducer.

4. Used Mahout to run the page rank algorithm.

Assignment 6 focused on:

1. the application of Spark and Storm
2. Implemented Streaming queries to compute the 4-value windowed average that moves 2 tuples at atime.
3. Ran KMeans Clustering Mahout to cluster the data into 8 clusters with up to 10 iterations

Final Project focused on:

1. Implementing the given SQL queries using Pig.

2. Implementing the given SQL queries using Hadoop streaming

3. Implementing KMeans clustering on the randomly generated data. 



