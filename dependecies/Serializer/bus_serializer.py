def bus_response_serializer(data):
   return{
      "bus_id" : data.bus_id ,
       "bus_no":data.bus_no,
       "driver_name":data.driver_name,
       "conductor_name":data.conducter_name,
       "conductor_contact":data.conducter_contact
   }
def bus_login_serializer(data):
   return{
      "bus_id": data.bus_id,
   }


def bus_location_serializer(data):
   return{
      "bus_id":data.bus_id,
      "latitude":data.latitude,
      "longitude":data.longitude,
      "shard_id":data.shard_id
   }

def bus_status_serializer(data):
   return{
      "bus_id":data.bus_id,
      "status":data.status,
      "bus_no":data.bus_no
   }

def bus_route_response_serializer(data):
   return{
      "bus_id":data.bus_id,
      "stop1":data.stop1,
      "stop2":data.stop2,
      "stop3":data.stop3,
      "stop4":data.stop4,
      "stop5":data.stop5
   }