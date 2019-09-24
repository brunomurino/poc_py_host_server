# Proof of Concept for a host server

## Goal
The goal of this project is to do a proof of concept of a web server (flask) that can interact with a db (mysql) through HTTP requests.

## Design
The ideia is to have UI where the user can enter 2 numbers and choose between 2 operations (multiplication or division).

The user would then click a button to send a post request to the server.
Based on the operation chosen by the user the server would call different python scripts to transform the 2 number.

The user would then be taken to another page where the result of the above transformation would be displayed

## Current status
The web pages already exist and can send a single post request (can't differentiate functions yet)
Can connect to mysql server from web server but no script/function defined to act on it. Just started a draft in "test.py".

## Steps being worked on
Make web server test connection (until timeout) with mysql server to detect if the functionality is live.