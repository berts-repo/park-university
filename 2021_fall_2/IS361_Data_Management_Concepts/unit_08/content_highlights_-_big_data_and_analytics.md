# Unit 8: Content Highlights - Big Data and Analytics

The purpose of this document is to highlight the main points on Big Data and Analytics, and complement some of the textbook explanations. It is recommended to first read this week’s assigned chapters from the textbook, and then come back to this document for further commentary.

The highlights of this week’s readings are:

Big Data is defined as data that shares the following three characteristics (or three V’s as they are called):

Volume: the amount of data is very vast.

Variety: the data comes from a varied set of sources. These include standard databases, non-structured data, text, audio, images, video, sensor data, and geographic information.

Velocity: data is produced at very high speed.

The textbook mentions another two Vs: Veracity and Value, meaning that the data should be of quality and relevant to the users, but the instructor believes these are characteristics of the manipulation of the data, rather than an intrinsic characteristic.

Because of the variety of information than can be obtained from big data, it is not possible to have a model that will cover all possible information when can obtain from the data. This means that we cannot write an ERD powerful enough to capture the richness of the data. Therefore systems that handle big data must create a “schema on read”. The structure of the data will be created the moment the data is available. There are two current approaches to obtain this schema: JavaScript Object Notation (JSON) and Extended Markup Language (XML). Both are languages that can be used to describe the organization of data that is being received from the sources of big data.

Once we can obtain schemas from big data, we need to be able to manipulate it to obtain information. For this we use “Not only SQL” or NoSQL. This is software that store big data and helps to manage it. This is the equivalent of our DBMS in structured databases, but for big data. The textbook describes 4 kinds of NoSQL databases management systems that are currently being used. Each one store data in different ways and with different capabilities.

Even though we can create programs to handle each piece of big data, we also need the ability to do it rapidly. It is of no use to know how to obtain some information if this information is only going to be available after a long period of time. The large amount of items in big data requires an approach to speed calculations up. This approach is Hadoop. Hadoop is an algorithm that breaks calculations to be performed in big data into a set of smaller tasks to be performed in sections of this data by a cluster of computers. Each computer in the cluster is independent of each other and receives a set of the calculations and a section of the big data to process. All computers in the cluster work in parallel to perform their calculations in their section of the data. When they finish, all their results are compiled and a final response is created for the whole system. An example that comes to mind is the following: How can we find what search is trendy right now in Google? We could collect all queries made in the last hour and find which is the topic more requested. Given the number of Google users all over the world, this could take quite a while, if done by one single machine. However, if we use a cluster of computers and we give each computer data from a world region, each computer may find the trendiest topic in each region. All compute this data in parallel, and at the end another set of computers match the results of different regions to obtain the final result.

Finally, this chapter presents some real computer architectures that implement some of the approaches explained above in real big data. It will be worthwhile for you to review the list of areas where these approaches made and will continue making an impact.
