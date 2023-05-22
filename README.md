# roundabout
Minimal redis like features in native python
Intended to be used within a single python project to share data between threads and processes in a more user friendly way.

Goals.  

In-Memory Data Storage: Store all data in memory, allowing for fast data access and retrieval.

Key-Value Store: A key-value store, where every data entry is identified with a unique key. 

Data Structures: A range of data structures, including strings, hashes, lists, sets, and sorted sets.

Json Data Structure: Json like structure with retreival of keys and subkeys

Pub/Sub Messaging: Support for Pub/Sub messaging, allowing subscription to specific message channels and push real-time updates 

Simple to use and understand

TODO.  
pub sub example. 
  Can we use pydantic to define events?
list example
hash example
set example

Future ideas.  
external api
strong typing for data?
event trigger/rules
