import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.Parse(open("user.avsc").read())

writer = DataFileWriter(open("users.avro","wb"),DatumWriter(),schema)
writer.append({"name":"Sridhar","favourite_number":13})
writer.append({"name":"Iyer","favourite_number":6,"favourite_color":"Black"})
writer.close()

reader = DataFileReader(open("users.avro","rb"),DatumReader())
for user in reader:
    print(user)
reader.close()
