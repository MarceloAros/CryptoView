from flask import Flask, jsonify
fort = open ("data.txt")
dater = fort.read()
print (jsonify(dater))