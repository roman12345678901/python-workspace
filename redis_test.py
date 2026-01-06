import redis 

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

#setup test key with expiration of 10 seconds
r.set("roma_test", "prime_form", ex=10)

# Retrieve and print the value of the test key
print ("Значение", r.get("roma_test"))

