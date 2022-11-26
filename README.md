# AirBnB Clone

## Introduction

Alright!!! It is game time! And we want to ball with an AirBnB clone project. The goal of the project is to deploy on our server a simple copy of the [AirBnB website](https://www.airbnb.com/).

After a few months,we should have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Final product

![final product](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5cbdb19c68bd8ddf356c14de85a57a43a7d604aa9c7368b8bea530fd319ebe6b)

## Steps

The application will be built one step after another. Each step will link to a concept detailed below:

### The console

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won’t have to pay attention (take care) of how our objects are stored.

This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

The console will be a tool to validate this storage engine

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=291a029dddb05d603823276b6b5fa9b1b535dab85f690ce37e6d8011b6ca29f4)

### Web static

- learn HTML/CSS
- create the HTML of our application
- create template of each object

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=56aef54f646720f8417e2ccb55a88db1ff5d2bdcb1a525d007b14d1aae77e5c8)

### MySQL storage

- replace the file storage by a Database storage
- map our models to a table in database by using an O.R.M.
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c8160c6815bd9d02e81dbb13db6c95116a9f4e6d9dfd26fbb9d1574ff2f03fa7)

### Web framework - templating

- create our first web server in Python
- make our static HTML file dynamic by using objects stored in a file or database
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=13b064ef91aa856d0a4f3500d91c4781f7496c2d783f88fb752c48d6976ec5bb)

### RESTful API

- expose all our objects stored via a JSON web interface
- manipulate our objects via a RESTful API
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5818c816aca3439aa874924f57980295fa00326d6d9991e15684f10403ebd0aa)

###  Web dynamic

- learn JQuery
- load objects from the client side by using your own RESTful API
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221126T162836Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=685edb156dbe7e0149f33ef3f5c8addf48a1ae12088753b1a21ef6cca940f47d)

## Files and Directories

- models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory will contain all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
	- attributes: id, created_at and updated_at
	- methods: save() and to_json()
- models/engine directory will contain all storage classes (using the same prototype). For the moment we will have only one: file_storage.py.
