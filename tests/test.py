import os, sys
#Modify the lib path
lib_path = os.path.abspath('../HIN/')
sys.path.append(lib_path)
import network, schema, base_node
schema = schema.NetworkSchema()
schema.add_attr("color")
schema.add_attr("feel")
schema.add_relation("color", "feel")
schema.add_relation("color", "color")
if not schema.has_relation("color", "feel") :
    print "add_relation failed"
if not schema.has_attr("color") :
    print "add_attr failed"

schema.rm_attr("feel")
if schema.has_attr("feel") :
    print "rm_attr failed"
if schema.has_relation("color", "feel") :
    print "rm_attr failed to invalidate relations"

print "all good"



